/**
 * Build an allowlisted learner folder without publishing it or copying private source history.
 * Usage: node scripts/build-learner-package.mjs <new-output-directory>
 * Requires Node.js 22+. Refuses existing destinations so unrelated files cannot enter an archive.
 */
import { readFile, mkdir, writeFile, lstat, realpath } from 'node:fs/promises';
import { resolve, relative, dirname, sep, isAbsolute } from 'node:path';
import { fileURLToPath } from 'node:url';
import { createHash } from 'node:crypto';
import { spawnSync } from 'node:child_process';
import { safeRelativePath } from './validate-repo.mjs';

const root = fileURLToPath(new URL('../', import.meta.url));
const slash = value => value.split(sep).join('/');

export async function buildLearnerPackage(destination) {
  if (!destination) throw new Error('Supply a new output directory.');
  const output = resolve(destination);
  const selected = JSON.parse(await readFile(resolve(root, 'learner/package-files.json'), 'utf8'));
  if (!Array.isArray(selected) || new Set(selected).size !== selected.length) throw new Error('Invalid package allowlist.');
  const selectedSet = new Set(selected);
  const prepared = [];
  const canonicalRoot = await realpath(root);
  for (const name of selected) {
    // An allowlist is a distribution boundary, so reject traversal and private areas before reading.
    if (!safeRelativePath(name) || /^(?:\.git|\.local|\.private)\//.test(name) || /(?:^|\/)\.env/.test(name)) throw new Error(`Unsafe package entry: ${name}`);
    const source = resolve(root, name);
    const stat = await lstat(source);
    const canonicalSource = await realpath(source);
    const inside = relative(canonicalRoot, canonicalSource);
    if (!stat.isFile() || stat.isSymbolicLink() || isAbsolute(inside) || inside.startsWith(`..${sep}`) || inside === '..') throw new Error(`Package source escapes repository: ${name}`);
    let content = await readFile(source, 'utf8');
    if (name.endsWith('.md')) {
      // Preserve usable included links while avoiding inaccessible instructor-only dependencies.
      content = content.replace(/\[([^\]]+)\]\(([^\s)]+)\)/g, (whole, label, target) => {
        if (/^(https?:|mailto:|#)/i.test(target)) return whole;
        const targetPath = slash(relative(root, resolve(dirname(source), decodeURIComponent(target.split('#')[0]))));
        return selectedSet.has(targetPath) ? whole : `${label} (instructor reference, not included)`;
      });
    }
    const privateKeyMarker = '-----BEGIN ' + 'PRIVATE KEY-----';
    if (/docs\.google\.com\/document|webcast\/present\?|github_pat_[A-Za-z0-9_]{30,}|gh[pousr]_[A-Za-z0-9]{30,}/.test(content) || content.includes(privateKeyMarker)) throw new Error(`Restricted content in learner file: ${name}`);
    prepared.push({ name, content });
  }
  // Exclusive directory creation fails before writing if a previous package or user folder exists.
  await mkdir(dirname(output), { recursive: true });
  await mkdir(output);
  const rows = [];
  for (const { name, content } of prepared) {
    const target = resolve(output, name);
    await mkdir(dirname(target), { recursive: true });
    await writeFile(target, content, { encoding: 'utf8', flag: 'wx' });
    rows.push({ path: name, sha256: createHash('sha256').update(content).digest('hex') });
  }
  const revision = spawnSync('git', ['-C', root, 'rev-parse', 'HEAD'], { encoding: 'utf8' });
  const status = spawnSync('git', ['-C', root, 'status', '--porcelain'], { encoding: 'utf8' });
  const metadata = { sourceRevision: revision.status === 0 ? revision.stdout.trim() : null, sourceHadUncommittedChanges: status.status === 0 ? Boolean(status.stdout.trim()) : null, nativeYamlIncluded: false, tenantExecuted: false, files: rows };
  await writeFile(resolve(output, 'package-manifest.json'), `${JSON.stringify(metadata, null, 2)}\n`, { flag: 'wx' });
  await writeFile(resolve(output, 'PACKAGE-STATUS.md'), '# Course materials\n\nStart with [START-HERE.md](START-HERE.md). The module guides support independent practice.\n\n**Native YAML sample: MISSING.** The inspection procedure is included, but a genuine sanitized native capture must be supplied before the promised export follow-up is complete. No native export is fabricated here.\n\n**Tenant execution: NOT VERIFIED.** Expected outputs and synthetic examples are labelled. Use your approved environment and permissions.\n\nThese original course materials are prepared for authorized course distribution. No public or open-source license is granted.\n', { flag: 'wx' });
  return { output, files: rows.length + 2, nativeYamlIncluded: false };
}

if (process.argv[1] && resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  try { console.log(JSON.stringify(await buildLearnerPackage(process.argv[2]))); }
  catch (error) { console.error(`Learner package failed: ${error.message}`); process.exitCode = 1; }
}
