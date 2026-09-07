import { readFile } from 'node:fs/promises';
import { resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { createStudyPlan } from '../src/study-plan.mjs';

const root = fileURLToPath(new URL('../', import.meta.url));
try {
  if (process.argv.length > 3) throw new Error('Usage: node scripts/run-study-plan.mjs [input.json]');
  const path = process.argv[2] ? resolve(process.argv[2]) : resolve(root, 'contoso-ai901-agent/tools/example-input.json');
  const raw = await readFile(path, 'utf8');
  if (Buffer.byteLength(raw) > 16_384) throw new Error('Input fixture must be no larger than 16 KiB.');
  console.log(JSON.stringify(createStudyPlan(JSON.parse(raw)), null, 2));
} catch (error) {
  console.error(`Study-plan demo failed: ${error.message}`);
  process.exitCode = 1;
}
