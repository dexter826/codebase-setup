<p align="center">
  <a href="skills/codebase-setup/SKILL.md"><img src="https://img.shields.io/badge/standard-AgentSkill-00cc5c?style=flat-square&labelColor=0a0a0a" alt="standard: AgentSkill" /></a>
  <a href="CHANGELOG.md"><img src="https://img.shields.io/badge/version-0.1.0-00cc5c?style=flat-square&labelColor=0a0a0a" alt="version: 0.1.0" /></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-00cc5c?style=flat-square&labelColor=0a0a0a" alt="license: MIT" /></a>
</p>

# codebase-setup

`codebase-setup` is an Agent Skill that brings any repository — new or existing — to a working, production-grade baseline: runnable source, quality gates, automated testing, CI pipelines, container/environment configuration, standard engineering documentation, and AI agent context.

The skill operates **by state**, not by static recipes:

```text
Target Baseline = Archetype × Stack × Depth × Modules
Current State   = evidence from repository + runtime environment
Gap             = Target − Current
Setup           = ordered, consented closure of Gap
```

Whether triggered by a brief prompt, chat context, PRD/SRD documents, or an existing messy codebase, the skill extracts verifiable facts to compile a unified **Setup Brief**. From that point on, the entire workflow executes deterministically against the state gap.

---

## Key Features

- **Three operating modes**: `scaffold` for new or empty directories, `harden` for existing codebases, and `audit-only` for non-modifying assessments.
- **Archetype-aware**: Classifies repositories into application, service/API, library/CLI, monorepo, skill package, docs/content, or generic.
- **Stack-agnostic & dynamic research**: Inspects manifests, lockfiles, and existing configs; queries current official documentation and CLI `--help` at runtime instead of relying on stale, hardcoded recipes.
- **Four discrete consent gates**: Toolchain, global tools, source initialization, and dependencies. Empty groups are skipped; global installs strictly require explicit, separate confirmation.
- **Additive by default**: Merges configuration files, adds scripts, and preserves established project conventions; overwriting custom files always requires explicit approval.
- **Governed `AGENTS.md` & `DESIGN.md`**: Always previews content and asks before creating files (`AGENTS.md` for agent instructions, Google Stitch compliant `DESIGN.md` for frontend/UI applications).
- **Industry standard file templates**: Built-in canonical templates for `README.md`, `LICENSE`, `CHANGELOG.md`, `.editorconfig`, `CONTRIBUTING.md`, and `SECURITY.md`.
- **Evidence-based reporting**: Reports `pass` only for commands that actually ran and exited with zero; clearly isolates setup-induced failures from pre-existing repository issues.

---

## Operating Modes

| Mode | When to use | Behavior |
| :--- | :--- | :--- |
| **`scaffold`** | Target directory is empty or starting a new project | Runs official ecosystem scaffolder with consent |
| **`harden`** | Repository already has code/manifests but lacks tooling | Adds missing gates, tests, CI, docs; never re-initializes source |
| **`audit-only`** | User requests gap assessment or health check | Zero filesystem writes, zero dependency installs |

---

## Scope Matrix

| Axis | Supported Values |
| :--- | :--- |
| **Archetype** | application · service/API · library/CLI · monorepo · skill package · docs/content · generic |
| **Stack** | JavaScript/TypeScript · Python · Go · other ecosystems · generic |
| **Depth** | minimal · standard (default) · strict |
| **Module** | structure · quality · tests · delivery · docs · community · design · agent context |

Specific toolchains are not hardcoded. The skill examines the repository first, verifies commands and flags with official documentation or `--help`, and records exact sources in the final setup report.

---

## Installation

### Via Plugin Marketplace (Claude Code, Codex, Antigravity)

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

### Via Skills CLI (Recommended)

**Install into current project:**
```bash
npx skills add dexter826/codebase-setup
```

**Install globally (silent confirmation):**
```bash
npx skills add dexter826/codebase-setup -g -y
```

---

### Manual Git Installation

Copy the `skills/codebase-setup` folder into your agent's skills directory to install only the runtime payload (`SKILL.md`, `references/`, `assets/templates/`) without repository overhead.

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

## Usage Examples

The skill activates automatically whenever you ask an agent to scaffold, initialize, standardize, or harden a codebase.

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

Before making any changes, the skill presents an execution plan outlining files to create/modify, commands to run, and untouched boundaries. High-risk actions prompt for consent. Upon completion, it outputs a verification report with a complete consent log.

---

## Package Structure

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

## Requirements & Safety Guarantees

- Compatible with coding agents implementing the **AgentSkills** specification.
- Requires read permissions for the target repository and write permissions for the project workspace.
- Network access required only when installing dependencies, invoking official scaffolders, or checking current documentation.

**Safety boundaries:**
- Never installs global system tools without explicit authorization.
- Never mutates system `PATH` or user shell profile configuration.
- Never commits to version control without direct instruction.
- Never exposes secrets or parses private credentials into reports or generated code.

---

## License

MIT License. See [LICENSE](LICENSE) for details.
