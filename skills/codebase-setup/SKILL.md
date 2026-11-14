---
name: codebase-setup
description: >-
  Set up or harden any codebase — new or existing — into a working baseline with
  runnable source, quality gates, tests, CI, container/env configuration,
  developer docs, and AI agent context. Use this skill whenever the user asks to
  set up, scaffold, initialize, standardize, onboard, or harden a project or
  repository, including requests phrased as "setup project", "setup dự án",
  "khởi tạo dự án", "dựng base project", "tạo base", "chuẩn hóa repo",
  "cài tooling", "thêm lint/test/CI", or when the user provides a PRD/SRD and
  expects a project skeleton. Also use it when an existing repo lacks linting,
  tests, CI, container or environment configuration, a README, or AGENTS.md —
  even if the user does not name the skill. Do not use it for feature
  implementation, README-only rewrites, UX copywriting, or skill-content authoring.
license: MIT
metadata:
  author: "dexter826"
  version: "0.1.0"
---

# Codebase Setup

Bring any repository — new or existing — to a working baseline: runnable source, quality gates, tests, delivery automation, developer documentation, and AI agent context.

The skill is **state-driven**, not input-driven. It closes the gap between a target baseline and the repository's current state:

```
Target Baseline = Archetype × Stack × Depth × Modules
Current State   = evidence from repository + environment
Gap             = Target − Current
Setup           = ordered, consented closure of Gap
```

## Core Principles

- **Evidence over assumptions.** Read the repository, manifests, lockfiles, CI, and toolchain before asking factual questions. Every command, path, and version must trace to a file, a runtime check, current official documentation, or an explicit user decision.
- **Facts vs decisions.** Detect facts silently. Ask only for decisions. Apply safe defaults only when they are reversible and low-risk. Never default on irreversible actions.
- **Consent before irreversible actions.** Show the command, target, and side effects before installing tools, scaffolding source, adding dependencies, overwriting files, or creating AGENTS.md.
- **Additive by default.** Merge configs, add scripts, and preserve existing conventions. Existing user code wins over templates.
- **Minimal baseline.** Add what the repository needs, not every tool the skill knows. Do not gold-plate.
- **Verify before claiming.** Only report a command as passing if it actually ran and passed.
- **Hand off when appropriate.** This skill sets up structure and gates. It does not author skill content, write a deep README, or implement product features.

## Workflow

### Phase 0 — Intake

Build a **Setup Brief** from every available source: the request, prior conversation, attached documents, the repository, and the environment. Read [references/intake-and-brief.md](./references/intake-and-brief.md).

The Brief is the single source of truth for the rest of the run. Normalize at least:

- goal, target directory, mode
- archetype, stack, depth, modules
- constraints, decisions already made, assumptions, open questions
- target baseline, current state, gaps

Do not invent missing fields. Mark them as open questions or explicit assumptions. Setup creates structure and gates; it does not implement the features a document describes.

### Phase 1 — Classify

1. **Mode**: `scaffold` when the target is empty or new; `harden` when a repository already exists; `audit-only` when the user only wants an assessment.
2. **Archetype**: detect signals from the repository and the request. If signals are ambiguous, ask.
3. **Stack**: detect manifests, lockfiles, and existing configuration. If unknown, use `generic` and ask.
4. **Depth**: default to `standard`; use `minimal` or `strict` when requested.

Read [references/discovery-and-gap.md](./references/discovery-and-gap.md) for detection signals and [references/baseline-and-depth.md](./references/baseline-and-depth.md) for what each archetype, depth, and module requires. Record the evidence behind each classification.

### Phase 2 — Discover

Inspect, without modifying:

- manifests, lockfiles, workspace definitions
- entrypoints, routes, exports, CLI bins
- existing lint/format/typecheck/test configuration
- CI/CD, container, compose, and environment configuration
- docs, README, license, changelog, and agent instruction files
- runtime versions, package manager or task runner, git state
- existing conventions the setup must preserve

Produce a current-state inventory and a list of conventions worth keeping.

### Phase 3 — Gap Analysis

Compare the baseline intent with the current state. Produce an ordered gap list. Each gap needs:

- what is missing or stale
- the action that closes it
- risk and reversibility
- dependencies on other gaps

Skip capabilities that are already satisfied. Do not add tools the repository does not need.

### Phase 4 — Plan and Consent

Present a plan before writing:

- files to create and modify
- commands to run, with target directories and side effects
- assumptions and unresolved questions
- what will not be touched

Read [references/consent-and-safety.md](./references/consent-and-safety.md) for the decision policy and consent gates. For existing repositories, confirm the plan before applying it. For new empty repositories, still show the plan; AGENTS.md always gets its own preview and consent.

### Phase 5 — Bootstrap (scaffold only)

Run the bootstrap gates in order. Skip a gate when it has nothing to do.

1. **Toolchain** — check required tools and versions. If something is missing, show the required version and detection command.
2. **Global tool** — if a system-wide install is unavoidable, preview the OS-specific command and ask separately. Never install global tools silently.
3. **Source Init** — prefer the ecosystem's official scaffolder or generator. Research the current command and flags with `--help` before showing it. Preview the command and side effects. For a non-empty directory, ask whether to scaffold in a subdirectory, merge, or abort.
4. **Dependency** — preview dependency additions, separating scaffolder dependencies from baseline dependencies. Add dependencies through the package manager; do not hardcode versions in manifests.

A declined gate is recorded and skipped; continue with the unaffected work.

### Phase 6 — Apply Baseline

Apply in this order:

1. structure and entrypoints
2. quality tooling (lint, format, typecheck, hooks)
3. test skeleton
4. delivery (CI, container, compose, environment example)
5. documentation and agent context

Rules:

- Additive and merge-first. Never overwrite a custom file without consent.
- Add scripts to the existing manifest instead of replacing it.
- Preserve existing formatter, linter, and test choices unless the user asks to migrate.
- Do not edit lockfiles by hand.
- Do not create secrets or copy secret values. Use an environment example with names and safe placeholders.
- Document commands and versions from research in the report; do not invent them.

### Phase 7 — Verify

Run the verification commands that apply, in this order:

1. install (if dependencies changed and approved)
2. lint / format check
3. typecheck
4. tests
5. build
6. optional checks that fit the archetype (container build, link check, package validation, security scan)

Record command, exit code, result (`pass` / `fail` / `skipped`), and the reason for any skip. Separate setup-caused failures from pre-existing failures. Fix setup-caused failures; report pre-existing ones without silently repairing them.

Read [references/verification-and-report.md](./references/verification-and-report.md).

### Phase 8 — Report and Handoff

Report:

- mode, archetype, stack, depth
- files created and modified
- commands run and their results
- consent log
- verification results
- pending or manual steps
- handoffs

Handoffs:

| Need | Skill |
| --- | --- |
| Author or evaluate skill content | `skill-creator` |
| Deep README generation or refresh | `readme-generator` |
| Deep UI generation / design system styling | `frontend-design` or `tailwind-design-system` |
| Product requirements still fuzzy | product brainstorming skill |
| Feature implementation | normal development workflow |

## Research Protocol

The repository is the first source of truth; current official documentation is the second.

1. Read manifests, lockfiles, scripts, and existing configuration before proposing anything.
2. Identify the package manager or task runner from the lockfile or configuration.
3. Identify the existing quality, test, build, and delivery commands.
4. For a missing capability, consult current official documentation, `--help`, or release notes.
5. Prefer the official scaffolder or the ecosystem's current convention over a hand-written approximation.
6. Verify flags and versions at runtime. Do not rely on memorized commands.
7. Record the source and version used in the report.
8. Ask when several valid approaches exist or the official path is unclear.

A researched command with a recorded source is evidence; a memorized command is a guess.

## Decision Policy

| Class | Handling |
| --- | --- |
| Fact | Detect silently from artifacts or runtime |
| Decision | Ask once, with recommended defaults |
| Safe default | Apply only if reversible and low-risk; state it in the Brief |
| Irreversible / high-risk | Explicit consent; never default |

## AGENTS.md Policy

The canonical template is [assets/templates/AGENTS.md](./assets/templates/AGENTS.md). Use it as-is; change only the title to `# AGENTS.md`.

- Always show the proposed content and ask before creating the file, even when it does not exist.
- Never append project-specific sections automatically.
- If `AGENTS.md` already exists, always ask: keep, replace, merge, or skip.
- If `CLAUDE.md`, `.cursorrules`, or `copilot-instructions.md` exists, ask how to avoid duplicate or conflicting instructions.
- In non-interactive runs without explicit authorization, skip the file and report it as pending consent.
- Never modify the template body.

## DESIGN.md Policy (Frontend / UI Archetypes)

For user-facing applications (`application` archetype with UI components), propose a `DESIGN.md` based on the [Google Stitch / Google Labs standard](./assets/templates/DESIGN.md).

- **Scope:** Exclusive to UI applications (React, Vue, Svelte, iOS, Android, web). Never propose or create `DESIGN.md` for backend APIs, CLI tools, libraries without UI, or skill packages.
- **Structure:** Machine-readable design tokens (palette, typography, spacing units, elevation) in YAML front matter + 8 human-readable Markdown sections explaining design intent, WCAG contrast, and Do's & Don'ts.
- **Consent:** Always preview the proposed design tokens and rules; wait for user approval before creating the file.
- **Handoff:** `codebase-setup` establishes the baseline tokens and design rules. For extensive UI component generation, hand off to `frontend-design` or `tailwind-design-system`.

## Non-Interactive Runs

If the user has explicitly pre-authorized a group, treat that as consent for the group. Global tool installs always require separate authorization. Everything not authorized is skipped and reported as pending. State assumptions in the final report. Never claim an action was performed if it was skipped.

## Output Contract

Use this report structure unless the user asks for a different format:

```markdown
# Setup Report

## Summary
Mode · Archetype · Stack · Depth

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

## Reference Map

| Read | When |
| --- | --- |
| [references/intake-and-brief.md](./references/intake-and-brief.md) | Any input: vague requests, prior context, PRDs, conflicting documents |
| [references/discovery-and-gap.md](./references/discovery-and-gap.md) | Determining mode, current state, research protocol, and gaps |
| [references/baseline-and-depth.md](./references/baseline-and-depth.md) | Choosing the baseline, depth, and modules |
| [references/consent-and-safety.md](./references/consent-and-safety.md) | Planning, consent gates, overwrites, failure handling |
| [references/verification-and-report.md](./references/verification-and-report.md) | Deciding what to run and how to report |

## Non-Goals

- Generating product features from a PRD.
- Replacing official framework scaffolders.
- Acting as a package manager.
- Authoring SKILL.md content or evals.
- Writing a deep README when `readme-generator` is available.
- Migrating an existing architecture.
- Managing secrets or deployment credentials.
