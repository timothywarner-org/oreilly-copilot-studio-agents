/**
 * Optional offline reference for the course's bounded study-plan tool.
 * This module has no network, file-system, or credential access.
 * The limits are synthetic teaching choices, not Microsoft exam requirements.
 */
export const FOCUS_CODES = Object.freeze([
  'ai-concepts', 'ai-workloads', 'foundry-solutions',
]);

/** @typedef {{days:number, minutesPerDay:number, focus:string[]}} PlanInput */

/**
 * Reject malformed input before producing a plan.
 * @param {unknown} input
 * @returns {asserts input is PlanInput}
 */
export function validateInput(input) {
  if (input === null || typeof input !== 'object' || Array.isArray(input)) {
    throw new TypeError('Input must be an object.');
  }
  const fields = ['days', 'minutesPerDay', 'focus'];
  if (Object.keys(input).some(key => !fields.includes(key)) ||
      fields.some(key => !Object.hasOwn(input, key))) {
    throw new TypeError('Supply exactly days, minutesPerDay, and focus.');
  }
  if (!Number.isInteger(input.days) || input.days < 1 || input.days > 14) {
    throw new RangeError('days must be an integer from 1 through 14.');
  }
  if (!Number.isInteger(input.minutesPerDay) || input.minutesPerDay < 10 || input.minutesPerDay > 120) {
    throw new RangeError('minutesPerDay must be an integer from 10 through 120.');
  }
  if (!Array.isArray(input.focus) || input.focus.length < 1 || input.focus.length > 3 ||
      new Set(input.focus).size !== input.focus.length ||
      Array.from(input.focus).some(code => typeof code !== 'string' || !FOCUS_CODES.includes(code))) {
    throw new RangeError('focus must contain one to three unique supported focus codes.');
  }
}

/**
 * Construct a suggestion; no enrollment, email, persistence, or external action occurs.
 * @param {unknown} input
 * @returns {{kind:string, sideEffects:never[], totalMinutes:number, sessions:object[]}}
 */
export function createStudyPlan(input) {
  validateInput(input);
  const read = Math.floor(input.minutesPerDay * 0.4);
  const practice = Math.floor(input.minutesPerDay * 0.4);
  const review = input.minutesPerDay - read - practice;
  return {
    kind: 'study-plan-suggestion',
    sideEffects: [],
    totalMinutes: input.days * input.minutesPerDay,
    sessions: Array.from({ length: input.days }, (_, index) => ({
      day: index + 1,
      focus: input.focus[index % input.focus.length],
      minutes: input.minutesPerDay,
      allocation: { read, practice, review },
      sourceIds: ['ai901-guide'],
      guidance: 'Read an official explanation, answer original practice questions, and review misconceptions.',
    })),
  };
}
