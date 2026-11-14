<p align="center">
  <a href="skills/codebase-setup/SKILL.md"><img src="https://img.shields.io/badge/standard-AgentSkill-00cc5c?style=flat-square&labelColor=0a0a0a" alt="standard: AgentSkill" /></a>
  <a href="CHANGELOG.md"><img src="https://img.shields.io/badge/version-0.1.0-00cc5c?style=flat-square&labelColor=0a0a0a" alt="version: 0.1.0" /></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-00cc5c?style=flat-square&labelColor=0a0a0a" alt="license: MIT" /></a>
</p>

# codebase-setup

`codebase-setup` is an Agent Skill that sets up a clean, runnable baseline for new or existing repositories: runnable source code, linting and formatting, automated tests, CI workflows, container configuration, standard documentation, and agent instructions.

It computes changes by comparing the repository's current state against the target configuration:

```text
Target Baseline = Archetype × Stack × Depth × Modules
Current State   = evidence from repository + runtime environment
Gap             = Target − Current
Setup           = ordered, consented closure of Gap
```

The skill inspects existing manifests, PRDs, and chat context to generate a setup plan, then applies only the changes needed to close the gap.

---

## Features

- Three operating modes: `scaffold` for new directories, `harden` for existing repositories, and `audit-only` for non-modifying reviews.
- Detects the project archetype (application, service, CLI, library, monorepo, or skill package) and selects appropriate tooling.
- Verifies tool commands and options against official documentation or `--help` output rather than relying on static assumptions.
- Pauses for approval before installing toolchains, global utilities, or package dependencies, and before writing initial source code.
- Merges configurations and respects existing project conventions instead of overwriting custom files without permission.
- Previews `AGENTS.md` and Google Stitch compliant `DESIGN.md` before creating them.
- Provides standard templates for licenses, contributing guidelines, and security policies.
- Validates every setup step with actual exit codes, isolating new issues from pre-existing repository errors.

---

## Operating modes

| Mode | When to use | Behavior |
| :--- | :--- | :--- |
| `scaffold` | Target directory is empty or starting a new project | Runs official scaffolding tools with user approval |
| `harden` | Repository already contains code or manifests | Adds missing tooling, tests, CI, and docs without overwriting source code |
| `audit-only` | Assessing gaps or running a repository check | Inspects the workspace without writing files or installing packages |

---

## Scope matrix

| Axis | Supported values |
| :--- | :--- |
| Archetype | application, service/API, library/CLI, monorepo, skill package, docs/content, generic |
| Stack | JavaScript/TypeScript, Python, Go, other ecosystems, generic |
| Depth | minimal, standard (default), strict |
| Modules | structure, quality, tests, delivery, docs, community, design, agent context |

Toolchains are discovered at runtime. The skill checks the repository, validates flags against local commands or official documentation, and logs exact references in the final setup report.

---

## Installation

### Via plugin marketplace (Claude Code, Codex, Antigravity)

**Claude Code:**
```text
/plugin marketplace add dexter826/codebase-setup
/plugin install codebase-setup@codebase-setup
```

**Codex:**
```bash
codex plugin marketplace add dexter826/codebase-setup
codex plugin add codebase-setup@codebase-setup
```

**Antigravity:**
```bash
agy plugin install https://github.com/dexter826/codebase-setup
```

---

### Via skills CLI

**Install into current project:**
```bash
npx skills add dexter826/codebase-setup
```

**Install globally:**
```bash
npx skills add dexter826/codebase-setup -g -y
```

---

### Manual git installation

Copy `skills/codebase-setup` into your agent's skills directory. This installs the runtime payload (`SKILL.md`, `references/`, and `assets/templates/`) without repository overhead.

**Global on Unix/macOS (`~/.agents/skills`):**
```bash
tmp=$(mktemp -d) && git clone --depth 1 https://github.com/dexter826/codebase-setup.git "$tmp" && mkdir -p ~/.agents/skills && rm -rf ~/.agents/skills/codebase-setup && cp -R "$tmp/skills/codebase-setup" ~/.agents/skills/codebase-setup && rm -rf "$tmp"
```

**Project-local on Unix/macOS (`.agents/skills`):**
```bash
tmp=$(mktemp -d) && git clone --depth 1 https://github.com/dexter826/codebase-setup.git "$tmp" && mkdir -p .agents/skills && rm -rf .agents/skills/codebase-setup && cp -R "$tmp/skills/codebase-setup" .agents/skills/codebase-setup && rm -rf "$tmp"
```

**Global on Windows PowerShell (`$HOME\.agents\skills`):**
```powershell
$tmp = Join-Path $env:TEMP "codebase-setup-repo"
Remove-Item -Recurse -Force $tmp -ErrorAction SilentlyContinue
git clone --depth 1 https://github.com/dexter826/codebase-setup.git $tmp
New-Item -ItemType Directory -Force -Path "$HOME\.agents\skills" | Out-Null
Remove-Item -Recurse -Force "$HOME\.agents\skills\codebase-setup" -ErrorAction SilentlyContinue
Copy-Item -Recurse "$tmp\skills\codebase-setup" "$HOME\.agents\skills\codebase-setup"
Remove-Item -Recurse -Force $tmp
```

---

## Usage examples

The skill runs whenever you ask an agent to scaffold, configure, or standardize a repository.

```text
Set up a new web app using React, TypeScript, and Vite with tests and GitHub Actions CI.
```

```text
Harden this repository: add linting, formatting, test runners, and AGENTS.md. Do not touch existing code in src/.
```

```text
This repository lacks a Dockerfile and .env.example. Add them without altering pyproject.toml.
```

```text
Read the PRD in docs/ and scaffold the baseline structure, but do not implement product features yet.
```

Before changing any files, the skill presents a plan showing modified paths, scheduled commands, and protected areas. It prompts for confirmation on significant actions and finishes with a verification report covering every executed command.

---

## Package structure

```text
codebase-setup/
├── skills/codebase-setup/           # Skill runtime payload
│   ├── SKILL.md                     # Main router and orchestration workflow
│   ├── assets/templates/            # Standard templates (AGENTS.md, DESIGN.md, etc.)
│   └── references/                  # Specialized topic reference guides
├── evals/                           # Evaluation scenarios and test fixtures
├── assets/                          # Brand identity and logo suite
├── plugin.json                      # Multi-platform plugin configuration
└── README.md, CHANGELOG.md, LICENSE # Documentation and licensing
```

---

## Requirements and safety

- Compatible with coding agents that support the AgentSkills specification.
- Requires read access to the target repository and write access to the workspace.
- Network access is only needed when installing packages or checking online documentation.

Safety guardrails:
- Global tools are never installed without explicit confirmation.
- Shell profiles and system `PATH` remain untouched.
- Git commits are only made when requested.
- Secrets and tokens are excluded from reports and generated configs.

---

## License

MIT. See [LICENSE](LICENSE) for details.
