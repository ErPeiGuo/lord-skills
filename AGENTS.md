# Repository maintenance

This repository owns reusable `lord-*` Agent Skills. Project business facts remain in their projects. Use concise English for AI instructions; preserve exact source terms. User-facing conversation follows the user's language.

## Ownership and scope

- Maintain shared skill instructions once under `skills/<skill-name>/`. Installed global folders are deployment copies, not parallel authorities.
- A skill may support one or several clients. Keep host-specific configuration and necessary procedures separate from shared guidance. Do not promise compatibility based only on a common file format.
- Each skill declares its invocation policy. Preserve the current knowledge-governance skill's explicit-only Codex policy. Never add hooks or always-on rules to bypass it.
- Do not import real project facts, local machine paths, credentials or conversation exports into public examples. Use self-contained synthetic fixtures.
- Preserve unrelated changes. Commit and push only when explicitly authorized; announce the exact command before either action.

## Client boundaries

Codex is the current implemented target. `.codex-plugin/plugin.json` is packaging configuration; its presence is not proof of installation success. Claude Code is a planned extension only: follow `.claude-plugin/README.md` before implementing it. Do not create executable Claude plugin configuration or claim verification merely to fill a directory.

## Changes and verification

- Update the owning skill and directly affected references. Add resources only for a concrete consumer.
- Run `python3 scripts/check_repository.py` for metadata, routes or packaging changes. Install its dependencies from `scripts/requirements.txt` when needed.
- Select behavior scenarios from `evals/<skill>/` for substantive instruction changes. Run in isolated workspaces; keep expected answers away from an independent evaluating reader.
- Reuse valid results for unchanged skill content. Report structural checks, behavior checks and client installation checks separately; mark checks not run explicitly.
- Keep support status in the root README accurate. Use release tags for published versions and release notes for meaningful behavior changes. Do not create a release merely for a documentation correction.
