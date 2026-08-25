---
name: browser-testing
description: Run local web smoke or regression tests with Playwright, browser MCP, or the project's existing browser-test runner; use when the task mentions browser testing, E2E, UI flows, screenshots, traces, console errors, or network failures.
---

# Browser testing

## Run order

1. **Discover** the project root, package manager, existing test scripts, Playwright/Cypress config, and documented environment variables.
   - Completion: the exact start command, test command, target URL, and required test data are known or reported as blocked.
2. **Start** the project using an existing script. Prefer the repository's package manager and bind only to localhost.
   - Completion: the target URL responds and the process id/log path is recorded.
3. **Test** the requested journeys.
   - Prefer existing deterministic Playwright/Cypress tests.
   - If exploratory interaction is needed and the `playwright` MCP server is available, use its accessibility snapshot, navigation, interaction, console, and network tools.
   - Use a fresh browser context for each independent scenario.
   - Completion: every requested scenario is passed, failed, or explicitly blocked.
4. **Collect evidence** for every failure: failing step, URL, screenshot, trace/video when available, console errors, failed requests, response status, and relevant test output.
   - Completion: another agent can reproduce the failure from the report and artifacts.
5. **Clean up** browser contexts and the started process. Preserve test artifacts; do not preserve personal browser state.
   - Completion: no process started by this run remains unless the user explicitly requested it.

## Safety and scope

- Treat the target as local/test by default. Stop before using a production URL or real user account.
- Use test credentials supplied through environment variables or an existing test storage state. Never print or commit secrets, cookies, or storage state.
- Prefer an isolated Playwright context. Never attach to the user's personal Chrome profile unless explicitly requested.
- Reuse existing dependencies and scripts. Do not install packages or change application code during a test run.
- Do not repair source code. Report a minimal reproduction; a separate implementation agent may fix it.
- Keep test data disposable and identify any data that the run created.

## Failure classification

Classify each failure as exactly one of:

- **application**: the application behavior or response is wrong;
- **test**: the locator, assertion, fixture, or test setup is wrong;
- **environment**: dependency, port, browser, service, credential, or external-system failure;
- **blocked**: a required command, URL, account, or requirement is missing.

Do not call a test passed merely because the page loaded. Verify the requested observable outcome.

## Report format

Return this compact report:

```text
Status: passed | failed | blocked
Target: <local URL>
Command: <start/test command>

Checks:
- [passed|failed|blocked] <scenario> — <one-line result>

Failures:
- Class: application | test | environment | blocked
  Step: <reproducible action>
  Expected: <expected result>
  Actual: <actual result>
  Evidence: <artifact paths or logs>

Artifacts:
- <path>

Next action: <single best next step>
```

If no requested scenario is supplied, run the smallest safe smoke check: open the target, verify the primary page, exercise one non-destructive core action, and report what was not covered.
