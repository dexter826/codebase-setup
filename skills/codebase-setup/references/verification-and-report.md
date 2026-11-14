# Verification and Report

The skill only claims what it actually ran. This file defines the evidence rules and the report contract.

## Verification order

1. Dependency installation, if dependencies changed and the gate was approved
2. Lint
3. Format check
4. Typecheck
5. Tests
6. Build
7. Optional checks that fit the archetype, such as container build, link check, package validation, or security scan

Run the cheapest checks first. Stop a branch when a prerequisite fails; do not run tests against a broken install.

## Command discovery

Use the commands the repository already defines:

- task scripts in the manifest or task runner
- documented commands in the contribution guide or CI workflow
- ecosystem conventions for the detected stack

If a command is missing, determine the current official way from the tool's documentation or `--help`, then show it before running. If several valid options exist, ask instead of inventing.

Record the source of any command that was not already present in the repository.

## Evidence rules

For every command, record:

| Field | Example |
| --- | --- |
| Command | exact command and arguments |
| Exit code | `0` |
| Result | `pass` / `fail` / `skipped` |
| Reason for skip | missing tool, declined gate, network unavailable |
| Output summary | test and check counts, not full logs |

Rules:

- A command that was not run is `skipped`, never `pass`.
- A command that failed is `fail`, even if the failure looks unrelated.
- Pre-existing failures are reported separately and not silently fixed.
- Setup-caused failures are fixed and re-run.
- Do not summarize a failing command as "mostly working".
- Do not omit a failed command from the report.

## Classifying failures

| Failure | Cause | Action |
| --- | --- | --- |
| Missing dependency | Setup incomplete | Fix the install; rerun |
| Wrong script name | Setup used a non-existent command | Correct the script or the report |
| Lint error in generated boilerplate | Setup-created file | Fix the generated file |
| Lint error in user code | Pre-existing | Report; do not modify user code |
| Test failure in a sample test | Setup-created test | Fix or remove the sample; rerun |
| Test failure in user tests | Pre-existing | Report |
| Build failure caused by missing configuration | Setup incomplete | Add the missing configuration or guidance; do not invent secrets |
| Network failure | Environment | Report and provide the manual command |
| Tool missing | Environment | Report and provide the install command |

## Report template

```markdown
# Setup Report

## Summary
- Mode:
- Archetype:
- Stack:
- Depth:

## Created
- path — purpose

## Modified
- path — change

## Commands
- command — result

## Consent log
- Gate — approved / skipped / manual

## Verification
- command — pass / fail / skipped (reason)

## Pending / manual steps
- item — reason — suggested command
```

## Verification without execution

Sometimes the environment prevents execution: no network, no tool, no permission. In that case:

- Do not claim the check passed.
- Provide the exact command and expected outcome.
- Mark it as pending in the report.
- Do not create a fake result file.

## Re-running verification

After fixing a setup-caused failure, rerun the failed command and the commands that depend on it. Do not rerun unrelated expensive checks unless the user asks.
