# Official guidance and adaptation

Reviewed on 2026-10-28. Read these sources when maintaining this skill, not on every project task. They inform the method; they do not override user decisions or project authority.

| Primary source | Applied guidance |
| --- | --- |
| [Anthropic: Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices) | Concise instructions, conditional references, domain routing and task-based evaluation. This skill links its references directly from the entrypoint. |
| [Claude Code: Project memory](https://code.claude.com/docs/en/memory) | Keep always-loaded guidance selective. Imported files can load eagerly; splitting into imports alone does not provide on-demand reading. |
| [Anthropic: Effective context engineering](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents) | Retrieve relevant context as needed and persist important state outside the context window. |
| [Anthropic: skill-creator](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md) | Exercise realistic tasks and improve instructions from observed outcomes. |
| [Anthropic: doc-coauthoring](https://github.com/anthropics/skills/blob/main/skills/doc-coauthoring/SKILL.md) | Test understanding with a fresh reader. Here the reader is an AI; human editorial workflow is not adopted. |
| [OpenAI: Build skills](https://learn.chatgpt.com/docs/build-skills) | Codex UI metadata and explicit-only invocation through `agents/openai.yaml` and `allow_implicit_invocation: false`. |

AI-only consumption, English-first prose, immediate confirmation writeback, single ownership and current-knowledge retention are this user's approved choices. They are not presented as universal Anthropic mandates. Project paths, technology stacks, business rules and stage gates stay in their owning projects.

The instruction body is reusable across projects. Host invocation settings are not interchangeable: this installation configures Codex. Supporting a different host requires checking that host's manual-invocation mechanism rather than assuming it reads `agents/openai.yaml`.
