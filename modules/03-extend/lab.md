# Extend exercise: inspect the contract and the effect

**Three minutes. No account required.** Answer in the [worksheet](worksheet.md) before opening the
[worked example](worked-example.md).

1. A colleague requests a **responsible-ai** study session. Name the input and the two outputs of
   [GetStudySession](../../contoso-ai901-agent/tools/get-study-session.md).
2. They request **quantum** instead. Predict the direct flow result and the missing-focus conversation.
3. They request an AI-901 study signup. Explain the confirmation required and the two external results
   you would inspect before claiming that the row and announcement both exist.

The study-session flow returns text without external writes. The signup example creates a row after
fresh confirmation. The [independent event flow](../../contoso-ai901-agent/signup-trigger-2026-09-08.md)
then posts to **Contoso Ltd Community > General**. Saving a signup is not an exam booking.

**Optional after class:** Build and test GetStudySession using its recipe. Then inspect the signup
event design. If you reproduce the write path, use your own approved list, channel, and synthetic data.
Check every successful operation in its destination before retrying an ambiguous result.

**Transfer:** Explain when an [MCP connection, another agent, or a human referral](../../contoso-ai901-agent/tools/extension-decisions.md)
would add useful capability. A connection alone does not establish permission or a completed action.
