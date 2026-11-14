# Discovery and Gap

Discovery determines the **current state**. Gap analysis compares it with the **baseline intent**.

## Mode detection

| Evidence | Mode |
| --- | --- |
| Target directory is missing or empty | `scaffold` |
| Target contains a manifest, source tree, or project configuration | `harden` |
| The user explicitly asks for review or assessment only | `audit-only` |
| A non-empty directory contains only unrelated files | Ask: scaffold in a subdirectory, harden in place, or abort |
| Signals conflict | Ask; do not assume |

`audit-only` never writes files or runs installs.

## Archetype signals

Use multiple signals. One weak signal is not enough.

| Archetype | Signals |
| --- | --- |
| application | UI framework, browser entrypoint, app/pages/routes, UI dependencies |
| service-api | API framework, routes/controllers, server entrypoint, API spec, worker entrypoint |
| library-cli | package exports, bin/console entrypoint, publish metadata, CLI framework |
| monorepo | workspace manifest, multiple packages or apps, workspace-aware build tool |
| skill-package | plugin/skill package metadata, a skill directory with `SKILL.md`, evaluation fixtures |
| docs-content | documentation framework, content tree as the main artifact, no application runtime |
| generic | none of the above, or insufficient evidence |

When two archetypes are plausible, ask which is primary or whether the repository is a monorepo.

## Stack signals

| Stack family | Common signals |
| --- | --- |
| JavaScript/TypeScript | `package.json`, TypeScript config, a JS lockfile |
| Python | `pyproject.toml`, `requirements.txt`, Python sources, a Python lockfile |
| Go | `go.mod`, `go.sum`, Go sources |
| Other | language-specific manifest, shebang, task runner, CI commands |

This table is a starting point, not a closed list. Detect from the repository, not from assumptions.

## Research protocol

The repository is the first source of truth. The ecosystem's current documentation is the second.

1. Read manifests, lockfiles, scripts, and existing configuration before proposing anything.
2. Identify the package manager or task runner from the lockfile or configuration.
3. Identify the existing quality, test, build, and delivery commands.
4. For a missing capability, consult the official documentation, CLI `--help`, or release notes for the current recommended approach.
5. Prefer the official scaffolder or the ecosystem's current convention over a hand-written approximation.
6. Verify flags and versions at runtime. Do not rely on memorized commands.
7. Record the source and version used in the report.
8. Ask when several valid approaches exist or the official path is unclear.

Do not invent a command, version, package name, or flag. A researched command with a recorded source is evidence; a memorized command is a guess.

## Discovery checklist

Inspect without modifying:

### Repository identity
- manifests, lockfiles, workspace definitions
- top-level layout
- git state

### Runtime and build
- language/runtime version files
- package manager or task runner
- dev, build, start, and test commands
- entrypoints and public modules

### Quality
- existing lint, format, typecheck, and test configuration
- coverage and hooks
- conventions the setup must preserve

### Delivery
- CI workflows
- container and compose configuration
- environment examples and configuration loaders
- deployment targets

### Documentation and agent context
- README, docs tree, contribution guidance, license, changelog
- AGENTS.md, CLAUDE.md, and other agent instruction files

### Environment
- installed tool versions
- shell and OS
- network availability
- permissions to install or write

## Current-state inventory

```markdown
## Existing
- Manifests:
- Lockfiles:
- Package manager / task runner:
- Scripts:
- Entrypoints:
- Quality tooling:
- Tests:
- CI:
- Container setup:
- Environment examples:
- Docs:
- Agent files:
- Git state:

## Conventions worth preserving
- ...

## Unknowns
- ...
```

## Gap analysis

1. State the baseline intent from the archetype, depth, and selected modules.
2. Remove capabilities already satisfied by the current state.
3. Remove capabilities that do not apply to the archetype or depth.
4. Order the remaining gaps by dependency:
   - structure before quality
   - quality before tests
   - tests before CI
   - delivery and docs last
5. Classify each gap:
   - `create` — new file or directory
   - `merge` — add to an existing file
   - `replace` — requires explicit consent
   - `command` — install, scaffold, or verify
   - `handoff` — belongs to another workflow or the user

Every gap must trace to a baseline intent. If it does not, it is gold-plating and should be dropped.

## Idempotency

A second run must not duplicate work:

- if a capability is already present, skip it
- if a configuration is partial, merge only the missing pieces
- if a dependency is already present, do not add it again
- if a gate was skipped, keep it skipped unless the user asks to retry
- re-discover after the repository changes

## Ambiguity

Ask when:

- the mode is unclear
- two archetypes are plausible
- the stack cannot be detected
- an existing configuration is custom and the baseline would conflict
- a document contradicts the repository
- the target path is missing

Do not ask when the answer is readable from the repository or the environment.
