# Consent and Safety

This file defines how the skill decides, asks, executes, and fails.

## Decision classes

| Class | Rule | Examples |
| --- | --- | --- |
| Fact | Detect from artifacts or runtime; do not ask | Package manager from a lockfile; framework from a manifest; installed tool versions |
| Decision | Ask once, with a recommended option | Stack, archetype, depth, modules, monorepo layout, test framework |
| Safe default | Apply only when reversible and low-risk; state it | CI provider matching the hosting platform; environment example naming |
| Irreversible / high-risk | Explicit consent; never default | Overwrite a custom config, install a global tool, delete files, change an entrypoint |

If a choice is both a decision and high-risk, treat it as high-risk.

## Plan preview

Before writing or running anything that changes the repository, show:

```markdown
## Setup plan

### Will create
- path — purpose

### Will modify
- path — change

### Will run
- command — target — side effects

### Will not touch
- path or area — reason

### Assumptions

### Open questions
```

Keep it scannable. Do not bury commands in prose.

## Consent gates

Actions are grouped by risk. Skip empty groups without a prompt.

### Gate 1 — Toolchain

Show the required tool and version, what is installed, the detection command, and what will fail if it stays missing. If the tool is present, do not ask.

### Gate 2 — Global tool

System-wide installs always get a separate gate, even when other groups are pre-authorized.

Show why a project-local option is insufficient, the OS-specific command, the impact, and a manual alternative. Never run a global install without an explicit yes for this gate. Never edit `PATH` or shell profiles.

### Gate 3 — Source Init

Show the exact command, target directory, what the scaffolder creates, and side effects such as git initialization, automatic dependency installation, lockfile creation, or overwrite prompts. State whether the flags were verified with `--help`.

For a non-empty directory, ask first: scaffold into a subdirectory, merge into the current directory, or abort. Never use a force or overwrite flag without explicit consent.

### Gate 4 — Dependency

Show dependencies added by the scaffolder, additional baseline dependencies, the exact add or install command, and whether versions are resolved by the package manager. Do not hardcode versions. Do not edit the lockfile by hand.

## AGENTS.md and DESIGN.md gates

`AGENTS.md` and `DESIGN.md` always get their own preview and consent, even on an empty repository.

- **`AGENTS.md`**: Show the exact proposed content and the target path. Options: approve, request edits, skip. If the file already exists, ask: keep, replace, merge, or skip. If `CLAUDE.md`, `.cursorrules`, or `copilot-instructions.md` exists, ask how to avoid duplicate or conflicting instructions.
- **`DESIGN.md`**: Applies only to frontend/UI applications (`application` archetype with UI). Show the proposed YAML design tokens (palette, typography, spacing units) and core Do's and Don'ts based on the Google Stitch spec. Options: approve, adjust token values, skip. If `DESIGN.md` already exists, ask: keep, replace, merge, or skip.

## Overwrite gate

Any existing file that would be replaced needs explicit consent. Prefer, in order:

1. skip and report
2. merge
3. create a side-by-side alternative
4. replace only with confirmation

Never overwrite silently, including generated-looking files the user may have customized.

## Consent log

Record every gate in the final report:

| Gate | Decision | Command / file | Note |
| --- | --- | --- | --- |
| Toolchain | not needed | — | required runtime already present |
| Global tool | skipped | — | project-local option available |
| Source Init | approved | exact command | empty target directory |
| Dependency | approved | exact command | versions resolved by the package manager |
| AGENTS.md | approved | `AGENTS.md` | template unchanged |
| DESIGN.md | approved / skipped | `DESIGN.md` | UI apps only; Google Stitch standard tokens |

## Non-interactive runs

When the skill cannot ask:

- Apply only groups that were explicitly pre-authorized.
- Global installs require a separate, explicit authorization.
- `AGENTS.md` and `DESIGN.md` are skipped unless explicitly authorized.
- Existing-file overwrites are skipped.
- Everything skipped is reported as pending, with the manual command.
- State assumptions explicitly.

Never simulate consent. Never claim an action was performed if it was skipped.

## Failure handling

| Failure | Behavior |
| --- | --- |
| Missing tool | Skip the dependent branch; report the install command |
| Network failure | Stop the install; report; do not retry indefinitely |
| Scaffolder failure | Leave the target directory as intact as possible; report the command and error |
| Lint or test failure caused by setup | Fix the setup; rerun |
| Lint or test failure pre-existing | Report it; do not silently fix unrelated code |
| Partial write | Report exactly what was written and what was not |
| Conflicting config | Stop and ask before merging |

A failed branch does not invalidate completed work. The report must distinguish the two.

## Safety rules

- Additive and merge-first.
- Never delete user files without explicit consent.
- Never modify `.git` or create commits on the user's behalf.
- Never edit `PATH`, shell profiles, or global configuration.
- Never read or copy secret values into generated files or reports.
- Never invent commands, versions, environment variables, or package names.
- Never run a destructive command to "clean up" without asking.
- Prefer official scaffolders and package managers over hand-written framework files.
- Keep commands cross-platform; state which shell was assumed.
- If a command's flags are uncertain, run `--help` or ask instead of guessing.

## Command execution

- Quote paths with spaces.
- Prefer non-interactive flags.
- Set a reasonable timeout.
- Capture stdout and stderr for the report.
- Do not pipe secrets into commands.
- If a command requires elevation, stop and ask; do not attempt privilege escalation.
