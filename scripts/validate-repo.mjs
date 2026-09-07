/** Offline integrity checks. This is not a comprehensive secret scanner or a tenant test. */
import { readdir, readFile, lstat } from 'node:fs/promises';
import { resolve, relative, dirname, sep, extname } from 'node:path';
import { fileURLToPath } from 'node:url';
import { spawnSync } from 'node:child_process';

const root = fileURLToPath(new URL('../', import.meta.url));
const ignoredDirectories = new Set(['.git', '.local', '.private', 'node_modules']);
const textExtensions = new Set(['.md', '.json', '.mjs', '.ps1', '.yml', '.yaml', '.txt']);

export function safeRelativePath(value) {
  return typeof value === 'string' && value.length > 0 &&
    !value.includes('\\') && !value.startsWith('/') && !value.includes(':') &&
    value.split('/').every(part => part !== '..' && part !== '.' && part.length > 0);
}

async function listFiles(directory, files = []) {
  for (const entry of await readdir(directory, { withFileTypes: true })) {
    if (ignoredDirectories.has(entry.name)) continue;
    const path = resolve(directory, entry.name);
    if (entry.isSymbolicLink()) throw new Error(`Unexpected symlink: ${relative(root, path)}`);
    if (entry.isDirectory()) await listFiles(path, files);
    else if (entry.isFile()) files.push(path);
  }
  return files;
}

export async function validateRepository(base = root) {
  const errors = [];
  const assert = (condition, message) => { if (!condition) errors.push(message); };
  const load = async path => JSON.parse(await readFile(resolve(base, path), 'utf8'));
  const files = await listFiles(base);
  const course = await load('course.json');
  const metadata = await load('repo-metadata.json');
  const alignment = await load('curriculum/alignment.json');
  const cases = (await load('evals/cases.json')).cases;
  const template = await load('evals/results.template.json');
  const sourceManifest = await load('contoso-ai901-agent/knowledge/sources.json');
  const packageInfo = await load('package.json');
  const coreTool = await load('contoso-ai901-agent/tools/get-study-session.json');
  const coreRecipe = await readFile(resolve(base, 'contoso-ai901-agent/tools/get-study-session.md'), 'utf8');
  const teachingSlides = await load('instructor/teaching-slides.json');
  const learnerFiles = await load('learner/package-files.json');
  // The authored contract and paste-ready recipe must agree even though neither executes a flow.
  assert(coreTool.name === 'GetStudySession' && coreTool.sessionMinutes === 30, 'Unexpected core study-session contract.');
  assert(coreTool.input.allowedValues.join('|') === 'responsible-ai|workloads|foundry', 'Core focus choices changed without curriculum review.');
  for (const focus of coreTool.input.allowedValues) {
    assert(typeof coreTool.plans[focus] === 'string' && coreRecipe.includes(coreTool.plans[focus]), `Core plan differs between fixture and recipe: ${focus}`);
  }
  assert(coreTool.supportedStatus !== coreTool.unsupported.status, 'Core tool must distinguish success from unsupported input.');
  assert(teachingSlides.slides.every(slide => slide.title && slide.lines.length && slide.notes), 'Teaching slides need visible content and speaker notes.');
  assert(new Set(learnerFiles).size === learnerFiles.length, 'Duplicate learner-package entry.');
  for (const entry of learnerFiles) {
    assert(safeRelativePath(entry), `Unsafe learner-package path: ${entry}`);
    try { await lstat(resolve(base, entry)); } catch { errors.push(`Missing learner-package source: ${entry}`); }
  }
  const requiredModuleIds = ['01-inception', '02-build', '03-extend', '04-operate'];
  assert(course.id === 'oreilly-copilot-studio-agents-2026-09-08', 'Wrong course identity.');
  assert(course.modules.map(m => m.id).join('|') === requiredModuleIds.join('|'), 'Expected exactly the four approved modules.');
  assert(course.objectives.length === 4, 'Expected exactly four learning objectives.');
  assert(new Set(course.objectives.map(o => o.id)).size === 4, 'Objective IDs must be unique.');
  const objectiveIds = new Set(course.objectives.map(o => o.id));
  const proposal = await readFile(resolve(base, 'sources/proposal-curriculum.md'), 'utf8');
  for (const objective of course.objectives) {
    assert(proposal.includes(objective.text), `Objective text does not match the proposal: ${objective.id}`);
  }
  assert(course.codingRequiredForLearners === false, 'The core learner route must remain no-code.');
  const scheduled = course.modules.reduce((sum, m) => sum + m.scheduledMinutes, 0) + course.wrapUpMinutes;
  assert(scheduled === 240, 'Public delivery schedule must total 240 minutes.');
  assert(metadata.private === true && packageInfo.private === true, 'Private preparation guards must remain true.');
  assert(metadata.owner === 'timothywarner-org', 'Unexpected GitHub owner.');
  assert(metadata.name === packageInfo.name, 'Package and repository names disagree.');
  assert(metadata.defaultBranch === 'main', 'Expected main as default branch.');
  assert(metadata.homepage === course.courseUrl, 'Homepage must be the course advertisement.');
  assert(metadata.description.length <= 350, 'About description is too long.');
  assert(metadata.topics.length <= 20 && new Set(metadata.topics).size === metadata.topics.length, 'Invalid/duplicate GitHub topics.');
  for (const topic of metadata.topics) assert(/^[a-z0-9][a-z0-9-]{0,49}$/.test(topic), `Invalid topic: ${topic}`);
  assert(packageInfo.license === 'UNLICENSED', 'Do not silently introduce a public redistribution license.');
  assert(!packageInfo.dependencies && !packageInfo.devDependencies, 'Scaffold tooling is dependency-free.');
  const caseIds = new Set(cases.map(c => c.id));
  assert(caseIds.size === cases.length && cases.length === 12, 'Expected 12 unique agent scenarios.');
  for (const c of cases) {
    assert(objectiveIds.has(c.objectiveId), `Unknown objective in case ${c.id}.`);
    assert(c.input && c.expectedBehavior && c.requiredEvidence.length, `Incomplete case ${c.id}.`);
  }
  for (const m of course.modules) {
    assert(m.instructionAndPracticeMinutes + m.breakMinutes === m.scheduledMinutes, `Timing mismatch: ${m.id}`);
    for (const filename of ['README.md', 'lab.md', 'worksheet.md']) {
      try { await lstat(resolve(base, m.path, filename)); } catch { errors.push(`Missing ${m.path}/${filename}`); }
    }
    for (const id of m.learningObjectiveIds) assert(objectiveIds.has(id), `Unknown objective in ${m.id}.`);
    try {
      const guide = await readFile(resolve(base, `instructor/${m.id}-guide.md`), 'utf8');
      const objective = course.objectives.find(item => item.id === m.learningObjectiveIds[0]);
      assert(guide.includes(objective.text), `Instructor guide does not preserve the objective: ${m.id}`);
    } catch { errors.push(`Missing instructor guide: ${m.id}`); }
  }
  assert(alignment.length === 4 && new Set(alignment.map(a => a.objectiveId)).size === 4, 'Incomplete alignment map.');
  for (const row of alignment) {
    assert(objectiveIds.has(row.objectiveId), `Unknown alignment objective: ${row.objectiveId}`);
    assert(safeRelativePath(row.modulePath), 'Unsafe module path.');
    assert(course.modules.some(m => m.path === row.modulePath), `Unknown alignment path: ${row.modulePath}`);
    assert(row.evaluationCaseIds.length > 0, 'Each outcome requires evidence cases.');
    for (const id of row.evaluationCaseIds) assert(caseIds.has(id), `Unknown evidence case: ${id}`);
    try { await lstat(resolve(base, row.learnerArtifact)); } catch { errors.push(`Missing artifact: ${row.learnerArtifact}`); }
  }
  assert(template.agentTested === false && template.runAt === null, 'Never ship fabricated agent-test results.');
  assert(template.results.length === cases.length, 'Result template must cover all cases.');
  for (const row of template.results) {
    assert(caseIds.has(row.caseId) && row.status === 'NOT RUN' && row.observedResponse === null && row.evidence === null,
      'Every shipped agent-result row must remain NOT RUN without invented evidence.');
  }
  for (const source of sourceManifest.sources) {
    if (source.kind === 'local-file') {
      assert(safeRelativePath(source.path), 'Unsafe knowledge source path.');
      try { await lstat(resolve(base, source.path)); } catch { errors.push(`Missing knowledge fixture: ${source.path}`); }
    }
  }
  let linksChecked = 0;
  for (const path of files) {
    const rel = relative(base, path).split(sep).join('/');
    if (!textExtensions.has(extname(path)) && !rel.startsWith('.')) continue;
    const text = await readFile(path, 'utf8');
    if (extname(path) === '.json') {
      try { JSON.parse(text); } catch { errors.push(`Invalid JSON: ${rel}`); }
    }
    if (extname(path) === '.md') {
      // Validate local paths; anchors and remote availability are explicitly not checked here.
      const links = [...text.matchAll(/!?\[[^\]]*\]\(([^\s)]+)(?:\s+"[^"]*")?\)/g)];
      for (const match of links) {
        const url = match[1];
        if (/^(?:https?:|mailto:|#)/i.test(url)) continue;
        const raw = decodeURIComponent(url.split('#')[0]);
        if (!raw) continue;
        const target = resolve(dirname(path), raw);
        const within = relative(base, target);
        assert(within !== '..' && !within.startsWith(`..${sep}`), `Link escapes repo: ${rel} → ${url}`);
        try { await lstat(target); } catch { errors.push(`Broken local link: ${rel} → ${url}`); }
        linksChecked++;
      }
    }
    // Match token formats, not the literal environment variable names used in documentation.
    const classic = new RegExp('gh' + '[pousr]_[A-Za-z0-9]{30,}');
    const fine = new RegExp('github' + '_pat_[A-Za-z0-9_]{30,}');
    assert(!classic.test(text) && !fine.test(text), `Possible GitHub credential in ${rel}.`);
    assert(!text.includes('-----BEGIN ' + 'PRIVATE KEY-----'), `Private key in ${rel}.`);
    assert(!/https:\/\/[^\s/@]+:[^\s/@]+@github\.com/i.test(text), `Credential-bearing remote URL in ${rel}.`);
    assert(!text.includes('webcast/' + 'present?'), `Presenter link in ${rel}.`);
    assert(!text.includes('8075 ' + 'Sawyer Brown'), `Personal postal address in ${rel}.`);
  }
  const tracked = spawnSync('git', ['-C', base, 'ls-files', '-z'], { encoding: 'utf8' });
  if (tracked.status === 0) {
    for (const rel of tracked.stdout.split('\0').filter(Boolean)) {
      assert(!/^(?:\.private|\.local)\//.test(rel), `Private/local file is tracked: ${rel}`);
      assert(!/(?:^|\/)\.env(?:$|\.)/.test(rel) || rel.endsWith('.env.example'), `Environment file is tracked: ${rel}`);
    }
  }
  return { errors, filesChecked: files.length, localLinksChecked: linksChecked, agentExecuted: false };
}

if (process.argv[1] && resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  try {
    const result = await validateRepository();
    if (result.errors.length) {
      console.error(result.errors.map(e => `FAIL: ${e}`).join('\n'));
      process.exitCode = 1;
    } else {
      console.log(`PASS: ${result.filesChecked} files; ${result.localLinksChecked} local links; 4 objectives; 4 modules; 240-minute schedule.`);
      console.log('Scope: local integrity checks only. Agent execution, remote links, and tenant readiness are NOT verified.');
    }
  } catch (error) {
    console.error(`Repository validation failed: ${error.message}`);
    process.exitCode = 1;
  }
}
