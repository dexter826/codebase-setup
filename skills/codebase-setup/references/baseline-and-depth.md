# Baseline and Depth

## Baseline is intent, not a file list

A baseline is the set of capabilities a repository should have. It is not a fixed list of files, tools, or versions. The concrete implementation comes from:

1. the repository's existing conventions
2. the ecosystem's current official guidance
3. the user's decisions
4. the selected depth and modules

Use this file to decide **what the repository needs**. Research the current way to provide it at runtime. Never copy a static file list or command catalog from the skill.

## Archetypes

| Archetype | Baseline intent |
| --- | --- |
| application | A runnable user-facing app with a dev/build path, quality checks, tests, delivery, docs, and agent context |
| service-api | A runnable API or worker with configuration, tests, delivery, environment documentation, and agent context |
| library-cli | Package metadata, public entrypoints, a build or distribution path, tests, docs, and agent context |
| monorepo | A workspace graph, root orchestration, per-package needs, delivery, docs, and agent context |
| skill-package | Package metadata, a skill skeleton, an evaluation entry point, docs, and agent context; software tooling only when the package has scripts |
| docs-content | A content tree, navigation, validation, docs, and agent context; no application runtime |
| generic | An interview-driven baseline; add only what the user confirms |

For any archetype, ask: *what must be true for a new contributor to run, change, test, and ship this repository?* That answer is the baseline.

## Depth

| Depth | Intent |
| --- | --- |
| minimal | Make the repository understandable and runnable; no optional quality tooling |
| standard | Make the repository safe to change: quality checks, tests, and automated verification |
| strict | Make the repository safe to ship: hooks, coverage, container or release workflows, and stronger gates |

Source Init is not a depth option:

- `scaffold` mode always includes source initialization.
- `harden` mode never re-initializes source.

## Modules

| Module | Intent | Key Artifacts & Standards |
| --- | --- | --- |
| structure | A layout and entrypoints that match the archetype and the ecosystem | Directory skeleton, manifests, CLI bins |
| quality | Lint, format, typecheck, cross-editor consistency, and optional hooks | Linter, formatter, typechecker, `.editorconfig` (EditorConfig standard) |
| tests | A test runner and at least one meaningful test | Test framework config, baseline tests |
| delivery | CI, container or release automation, and environment examples | CI workflows, Dockerfile/Compose, `.env.example` (12-Factor App) |
| docs | Project homepage, license, version log, and contribution/security policies | `README.md` (CommonMark/GFM), `LICENSE` (SPDX), `CHANGELOG.md` (Keep a Changelog + SemVer) |
| community | Contribution workflow and security vulnerability reporting | `CONTRIBUTING.md` (Contributor workflow), `SECURITY.md` (OpenSSF / GitHub standard) |
| design | Persistent design system manifest and UI design tokens for AI agents | `DESIGN.md` (Google Stitch / Google Labs `design.md` standard) |
| agent_context | Agent instructions from the canonical template | `AGENTS.md` (canonical template) |

Modules are cumulative. Tests assume quality. Delivery assumes the project can build.

## Applicability

| Module | application | service-api | library-cli | monorepo | skill-package | docs-content | generic |
| --- | --- | --- | --- | --- | --- | --- | --- |
| structure | yes | yes | yes | yes | yes | yes | yes |
| quality | yes | yes | yes | yes | optional | optional | ask |
| tests | yes | yes | yes | yes | optional | optional | ask |
| delivery | yes | yes | yes | yes | optional | optional | ask |
| docs | yes | yes | yes | yes | yes | yes | yes |
| community | strict | strict | yes | yes | optional | optional | ask |
| design | yes (UI only) | no | no | ask | no | no | ask |
| agent_context | yes | yes | yes | yes | yes | yes | yes |

`optional` means: add only if the repository has code or scripts that benefit. A Markdown-only package does not need a code lint/test toolchain.  
`design` is exclusive to user-facing frontend/UI applications (`application` archetype with React, Vue, Svelte, Angular, iOS, Android, Desktop) or when UI design tokens are explicitly requested. Never add `DESIGN.md` to backend services or CLI tools.

## What not to add

- A tool the repository already has, unless the user asks to migrate.
- A framework the user did not choose.
- A database, ORM, queue, or auth provider that was not confirmed.
- A monorepo layout for a single app.
- A container workflow that the deployment target does not use.
- Coverage thresholds on a codebase with no tests.
- Multiple overlapping agent-context files.
- Empty directories that the ecosystem does not use.

## Implementation note

The concrete files, commands, and tool choices are discovered at runtime:

- preserve what the repository already uses
- consult the ecosystem's current official documentation
- verify CLI flags with `--help`
- ask when several valid options exist
- record the chosen source and version in the report

This keeps the baseline durable while the ecosystem changes.
