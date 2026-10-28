---
name: lord-doc-knowledge-governance
description: "Govern AI-consumed project knowledge when explicitly invoked to initialize a fact directory, capture confirmed decisions, resume work, update affected knowledge, or check retrieval. Manual invocation only."
---

# lord-文档知识治理

Maintain durable project knowledge that an AI can locate, interpret, verify and use across sessions. This skill contains cross-project methods; each project owns its knowledge and constraints.

## Activation and scope

Use only after explicit user invocation. `agents/openai.yaml` disables implicit invocation in Codex. Once invoked, maintain knowledge throughout the authorized task, including after compaction; do not require another invocation for each writeback. An unrelated task does not inherit activation. Do not install hooks, schedules or always-on rules to bypass manual activation.

Use the named project and knowledge root. Otherwise inspect the current project's instructions and entrypoint; ask only if the intended target remains ambiguous. Preserve existing layout, permissions, user decisions and unrelated edits. Invocation authorizes the requested knowledge work, not source changes, repository-wide reorganization or Git delivery. Resolve routine structure choices without asking the user to manage files.

## AI-only quality contract

AI is the sole direct consumer of maintained knowledge. Evaluate accurate retrieval, interpretation, continuity, implementation and verification. Human readability, teaching value, narrative flow and visual polish are not quality criteria. Preserve complete semantics rather than minimizing tokens at their expense. User-facing conversation still follows the user's language.

Use concise English for maintained prose. Preserve exact business terms, quotations, UI literals, source identifiers and necessary original-language passages. Default to Markdown; use JSON, Schema or another native format when an actual programmatic consumer needs it. Do not maintain duplicate representations or translations.

## Read and organize

Start from a short entrypoint that routes by question or task to the current owner and explains when to stop. Read the selected subject and necessary dependencies; use scoped exact search when the route is incomplete. Expand for a concrete unanswered question or dependency, not to read the entire corpus for reassurance.

Organize by coherent responsibilities and project domains. Keep related conditions together; split when different questions can select different units. Add indexes when they reduce search, without a fixed tree, file count or byte limit. Avoid chains of indexes that provide no selection value. Link shared contracts instead of copying them into consumers. Keep repository-local links portable and give external references their provenance and applicability.

Each claim has one canonical owner. Indexes and resume pointers may carry routing summaries, but do not maintain another editable copy of rules, status or results. Distinguish at the point of use:

| Knowledge | Establishes |
| --- | --- |
| Approved requirement | Desired behavior and acceptance conditions |
| Chosen design | Current approach, rationale and effective exclusions |
| Implementation or verification fact | Observed state with a scoped source or result |
| Reference or proposal | Input for consideration; no implicit adoption |
| Current work | Unresolved work, blockers and next action |

Source evidence describes implementation; it cannot silently replace an approved target. Record a target/implementation gap explicitly. Resolve conflicting evidence by scope and source; ask for an actual unresolved product choice while continuing independent work.

## Select the needed operation

- Creating or updating knowledge, recording a confirmation, or restoring task continuity: read [Maintenance](references/maintenance.md), only the relevant section.
- Checking a new structure, affected routes, or implementation readiness: read [Verification](references/verification.md). Use affected checks, not an automatic full audit.
- Reviewing this skill's methodology or adapting it to another host: read [Official guidance](references/sources.md). No web access is needed for routine project use.

## Completion

Persist important confirmations before continuing dependent discussion or handing off. Inspect the saved result and verify affected routes. Report the entrypoint, material changes and unresolved decisions or evidence gaps concisely. Stop when the authorized knowledge work and its relevant checks are complete; document completion does not imply implementation or user acceptance.
