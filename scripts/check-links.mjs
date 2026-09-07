/**
 * Optional network check for the external links in sources/link-register.md.
 *
 * This is deliberately NOT part of `npm run validate`. That gate is offline and
 * deterministic; this one reaches the public internet and can fail for reasons
 * that have nothing to do with the repository, such as rate limiting.
 *
 * Runs every URL twice, because a single 200 proves only that one request
 * succeeded. A link that passes once and fails once is reported as UNSTABLE
 * rather than quietly rounded up to PASS.
 *
 * Usage:
 *   node scripts/check-links.mjs                     # checks sources/link-register.md
 *   node scripts/check-links.mjs path/to/file.md     # checks any markdown file
 *   node scripts/check-links.mjs --json              # machine-readable summary
 */
import { readFile } from 'node:fs/promises';
import { resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = fileURLToPath(new URL('../', import.meta.url));
const CONCURRENCY = 6;
const TIMEOUT_MS = 25_000;
const PASSES = 2;
// A browser-shaped agent string; some documentation hosts refuse default fetch clients.
const USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ' +
  '(KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36';

export function extractUrls(markdown) {
  const found = new Set();
  for (const match of markdown.matchAll(/https?:\/\/[^\s)\]}"'<>,;|]+/g)) {
    found.add(match[0].replace(/[.,:;]+$/, ''));
  }
  return [...found].sort();
}

async function probe(url) {
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), TIMEOUT_MS);
  try {
    // GET rather than HEAD: several documentation hosts answer HEAD with 405.
    const response = await fetch(url, {
      method: 'GET',
      redirect: 'follow',
      signal: controller.signal,
      headers: { 'user-agent': USER_AGENT, accept: 'text/html,application/xhtml+xml,*/*' },
    });
    // Drain the body so the socket is released before the next request starts.
    await response.arrayBuffer().catch(() => undefined);
    return { status: response.status, finalUrl: response.url, ok: response.status === 200 };
  } catch (error) {
    return { status: 0, finalUrl: null, ok: false, error: error.name === 'AbortError' ? 'timeout' : error.message };
  } finally {
    clearTimeout(timer);
  }
}

async function runPass(urls) {
  const results = new Map();
  let cursor = 0;
  const workers = Array.from({ length: Math.min(CONCURRENCY, urls.length) }, async () => {
    while (cursor < urls.length) {
      const url = urls[cursor++];
      results.set(url, await probe(url));
    }
  });
  await Promise.all(workers);
  return results;
}

export async function checkLinks(markdown) {
  const urls = extractUrls(markdown);
  const passes = [];
  for (let pass = 0; pass < PASSES; pass++) {
    passes.push(await runPass(urls));
  }
  return urls.map(url => {
    const attempts = passes.map(p => p.get(url));
    const every200 = attempts.every(a => a.ok);
    const none200 = attempts.every(a => !a.ok);
    const verdict = every200 ? 'PASS' : none200 ? 'FAIL' : 'UNSTABLE';
    const redirected = attempts.some(a => a.finalUrl && a.finalUrl !== url);
    return { url, verdict, redirected, finalUrl: attempts.at(-1).finalUrl, attempts };
  });
}

if (process.argv[1] && resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  const asJson = process.argv.includes('--json');
  const target = process.argv.slice(2).find(a => !a.startsWith('--')) ?? 'sources/link-register.md';
  try {
    const markdown = await readFile(resolve(ROOT, target), 'utf8');
    const rows = await checkLinks(markdown);
    const counts = rows.reduce((acc, r) => ({ ...acc, [r.verdict]: (acc[r.verdict] ?? 0) + 1 }), {});
    if (asJson) {
      console.log(JSON.stringify({ target, checkedAt: new Date().toISOString(), passes: PASSES, counts, rows }, null, 2));
    } else {
      for (const row of rows) {
        if (row.verdict === 'PASS' && !row.redirected) continue;
        const detail = row.verdict === 'PASS'
          ? `redirects to ${row.finalUrl}`
          : row.attempts.map(a => a.status || a.error).join(' then ');
        console.log(`${row.verdict}: ${row.url}  (${detail})`);
      }
      console.log(`\n${target}: ${rows.length} links, ${PASSES} passes each.`);
      console.log(`PASS ${counts.PASS ?? 0} | UNSTABLE ${counts.UNSTABLE ?? 0} | FAIL ${counts.FAIL ?? 0}`);
      console.log('Scope: HTTP reachability only. This does not check that a page still says what it said.');
    }
    process.exitCode = (counts.FAIL ?? 0) + (counts.UNSTABLE ?? 0) > 0 ? 1 : 0;
  } catch (error) {
    console.error(`Link check failed: ${error.message}`);
    process.exitCode = 1;
  }
}
