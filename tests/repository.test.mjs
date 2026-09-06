import test from 'node:test';
import assert from 'node:assert/strict';
import { safeRelativePath, validateRepository } from '../scripts/validate-repo.mjs';

test('safe relative paths accept module paths', () => {
  assert.equal(safeRelativePath('modules/01-inception/README.md'), true);
});
test('unsafe or ambiguous paths are rejected', () => {
  for (const path of ['', '..', '../x', '/etc/passwd', 'C:/file', 'x\\y', 'x//y', './x', 'x/../y']) {
    assert.equal(safeRelativePath(path), false, path);
  }
});
test('course integrity checks pass without claiming to execute an agent', async () => {
  const result = await validateRepository();
  assert.deepEqual(result.errors, []);
  assert.equal(result.agentExecuted, false);
  assert.ok(result.localLinksChecked > 40);
});
