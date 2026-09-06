import test from 'node:test';
import assert from 'node:assert/strict';
import { createStudyPlan, validateInput, FOCUS_CODES } from '../src/study-plan.mjs';
const valid = () => ({ days: 3, minutesPerDay: 30, focus: ['cloud-concepts', 'management-governance'] });

test('reference plan has expected days, minutes, and no side effects', () => {
  const plan = createStudyPlan(valid());
  assert.equal(plan.kind, 'study-plan-suggestion');
  assert.equal(plan.sessions.length, 3);
  assert.equal(plan.totalMinutes, 90);
  assert.deepEqual(plan.sideEffects, []);
});
test('focus rotates predictably', () => {
  assert.deepEqual(createStudyPlan(valid()).sessions.map(s => s.focus),
    ['cloud-concepts', 'management-governance', 'cloud-concepts']);
});
test('every session allocation sums exactly, including awkward minute counts', () => {
  for (let minutes = 10; minutes <= 120; minutes++) {
    const s = createStudyPlan({ ...valid(), minutesPerDay: minutes }).sessions[0];
    assert.equal(s.allocation.read + s.allocation.practice + s.allocation.review, minutes);
    assert.ok(s.allocation.review >= 0);
  }
});
test('day bounds 1 and 14 are accepted', () => {
  for (const days of [1, 14]) assert.equal(createStudyPlan({ ...valid(), days }).sessions.length, days);
});
test('all supported focus codes are accepted', () => {
  assert.doesNotThrow(() => validateInput({ ...valid(), focus: [...FOCUS_CODES] }));
});
test('input is not mutated and output is deterministic', () => {
  const input = valid(); const before = structuredClone(input);
  assert.deepEqual(createStudyPlan(input), createStudyPlan(input));
  assert.deepEqual(input, before);
});
for (const [name, input] of [
  ['null', null], ['array', []], ['string', '3'], ['missing field', { days: 3, focus: ['cloud-concepts'] }],
  ['unknown field', { ...valid(), email: 'not-used' }],
  ['negative days', { ...valid(), days: -5 }], ['too many days', { ...valid(), days: 15 }],
  ['fractional days', { ...valid(), days: 2.5 }], ['string days', { ...valid(), days: '3' }],
  ['NaN days', { ...valid(), days: NaN }], ['infinite minutes', { ...valid(), minutesPerDay: Infinity }],
  ['too few minutes', { ...valid(), minutesPerDay: 9 }], ['too many minutes', { ...valid(), minutesPerDay: 500 }],
  ['fractional minutes', { ...valid(), minutesPerDay: 30.5 }], ['empty focus', { ...valid(), focus: [] }],
  ['duplicate focus', { ...valid(), focus: ['cloud-concepts', 'cloud-concepts'] }],
  ['unknown focus', { ...valid(), focus: ['other'] }], ['string focus', { ...valid(), focus: 'cloud-concepts' }],
]) test(`rejects ${name}`, () => assert.throws(() => createStudyPlan(input)));

test('rejects sparse focus arrays', () => {
  assert.throws(() => createStudyPlan({ ...valid(), focus: new Array(1) }));
});
