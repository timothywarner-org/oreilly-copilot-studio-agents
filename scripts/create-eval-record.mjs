import { mkdir, readFile, writeFile } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
import { resolve } from 'node:path';
const root = fileURLToPath(new URL('../', import.meta.url));
try {
  const target = resolve(root, '.local/agent-results.json');
  await mkdir(resolve(root, '.local'), { recursive: true });
  const template = await readFile(resolve(root, 'evals/results.template.json'), 'utf8');
  await writeFile(target, template, { encoding: 'utf8', flag: 'wx' });
  console.log('Created .local/agent-results.json; every agent case is NOT RUN.');
} catch (error) {
  console.error(error.code === 'EEXIST' ?
    'Refusing to overwrite existing .local/agent-results.json.' : error.message);
  process.exitCode = 1;
}
