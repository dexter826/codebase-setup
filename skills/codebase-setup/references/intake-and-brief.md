# Intake and Brief

Intake turns any input into one **Setup Brief**. It does not modify the repository and does not choose a stack by itself.

## Why one Brief

Different inputs — a vague request, an old conversation, a PRD, a repository, a machine — otherwise push the skill into different behaviors. The Brief normalizes all of them into the same fields, so the rest of the workflow is input-agnostic.

## Sources

| Source | Provides | Do not assume |
| --- | --- | --- |
| Request | Goal, target path, urgency, explicit stack or scope | That a missing stack is "obvious" |
| Conversation history | Decisions already made, constraints, preferences | That old decisions still apply after a contradiction |
| Documents (PRD, SRD, ADR, RFC) | Product type, users, flows, integrations, non-functional requirements, constraints, non-goals | That every product requirement belongs in the setup baseline |
| Repository artifacts | Current state, existing conventions, real commands | That an existing config is intentional or current |
| Environment | OS, shell, toolchain versions, network, permissions | That a tool is installed because a command exists in docs |

## Source priority

| Question | Priority |
| --- | --- |
| What is the current state? | Repository artifacts > environment > conversation > documents |
| What should the target be? | Latest explicit user decision > documents > conversation > safe defaults |
| What is the correct command or version? | Runtime `--help` / official docs > bundled knowledge > assumptions |
| What wins a conflict? | Surface it. Ask when the outcome is irreversible or high-risk. |

Record the winning source in the Brief.

## Setup Brief fields

```yaml
goal: ""
mode: scaffold | harden | audit-only
archetype: application | service-api | library-cli | monorepo |
           skill-package | docs-content | generic
stack:
  language: ""
  framework: ""
  package_manager: ""
depth: minimal | standard | strict
modules:
  structure: true
  quality: true
  tests: true
  delivery: true
  docs: true
  agent_context: true
constraints: []
decisions:
  - source: ""
    text: ""
assumptions: []
open_questions: []
target_baseline: []
current_state: []
gaps: []
```

A field is either populated, marked `unknown`, or listed under `open_questions`. Never fill it with a guess.

## Extraction rules

### Vague request

Extract the goal and target path. If the path is missing, ask. If the archetype or stack is missing, propose one option with a reason and ask for confirmation.

Do not read "setup project" as permission to choose a stack silently.

### Conversation history

Extract only decisions that were explicitly made and not later contradicted. Attach the source. If a later message conflicts, prefer the later message and record the conflict.

Do not re-ask what the conversation already answered. Do not treat exploratory brainstorming as a final decision unless the user confirmed it.

### Documents

Extract only setup-relevant facts:

- product type and primary users → archetype
- roles and permissions → authentication and authorization needs
- core flows → application or service shape
- integrations → payments, email, storage, search, queues
- non-functional requirements → performance, security, compliance, i18n
- constraints → stack, hosting, deadline, team, budget
- non-goals → what not to scaffold

Cite the section for every extracted fact. Summarize; do not dump the document. Setup creates structure, configuration, and gates; it does not implement the features described in the document.

### Repository artifacts

Extract facts, not intentions: manifests and lockfiles, workspace definitions, scripts and task runners, entrypoints, existing quality and test configuration, delivery configuration, documentation and agent files, runtime version files, git state.

### Environment

Check OS, shell, tool versions, network reachability, and permissions. These describe feasibility, not the target.

## Conflict handling

1. Name the conflicting sources and the exact disagreement.
2. Prefer the higher-priority source for the question being answered.
3. If the outcome is irreversible or high-risk, ask the user.
4. Record the resolution and its source in the Brief.

Do not silently pick a side.

## Question design

- Ask only for decisions that cannot be derived.
- Consolidate into one turn and group related choices.
- Give a recommended option and a one-line reason.
- Keep the list short; drop questions whose answers do not change the plan.
- If the user says "you decide", propose one option with rationale and ask for confirmation.

Good:

> "Single app or monorepo? Recommended: single app, because the requirements describe one web app and one API; a monorepo only pays off with two or more independently versioned packages."

Bad:

> "What do you want to use?" (no options, no default, no scope)

## Brief summary template

```markdown
## Goal

## Mode

## Target
- Path:
- Existing repository:
- Git state:

## Classification
- Archetype:
- Stack:
- Depth:
- Modules:

## Constraints

## Decisions already made
- [source]

## Assumptions

## Open questions

## Target baseline

## Current state

## Gaps
| ID | Gap | Action | Risk |
```

## Anti-patterns

- Dumping a document instead of extracting setup-relevant facts.
- Inventing a stack because the product type "usually" uses one.
- Asking for facts that are readable from the repository.
- Treating a brainstorm as a confirmed decision.
- Treating every feature in a document as something the setup must scaffold.
- Writing the Brief as a promise of work that has not been consented to.
