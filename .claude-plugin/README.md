# Claude Code extension boundary

Status: planned, not implemented or tested. Claude Code is unavailable for validation in the initial repository setup. This directory intentionally has no `plugin.json` or marketplace index.

When Claude Code support is requested:

1. Reuse `skills/<name>/` as the authoritative instruction source. Keep client-specific instructions conditional and avoid a second maintained copy of the same workflow.
2. Verify Claude Code invocation controls. Explicit-only skills require `disable-model-invocation: true` in their `SKILL.md` frontmatter. Codex's `agents/openai.yaml` does not enforce this in Claude Code. Check Codex parsing before sharing extra frontmatter, or prepare client-specific packaging if required.
3. Add `.claude-plugin/plugin.json` following the then-current manifest format, pointing to the shared skills. Add a marketplace index only when providing that installation route.
4. Verify discovery, explicit invocation, implicit-invocation blocking and applicable behavior scenarios in Claude Code before changing support status. Do not infer Claude web upload compatibility from Claude Code results.

References:

- [Claude Code skills and invocation controls](https://code.claude.com/docs/en/skills)
- [Claude Code plugin manifest](https://code.claude.com/docs/en/plugins-reference)

The root `CLAUDE.md` imports repository maintenance instructions only; it is not a skill adapter.
