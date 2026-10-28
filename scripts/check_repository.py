"""Check repository structure only; never execute skills or behavioral fixtures."""

import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

import yaml


ROOT = Path(__file__).resolve().parents[1]


def check(root):
    errors = []
    skills = sorted((root / "skills").glob("*/SKILL.md"))
    if not skills:
        errors.append("No skills found")
    names = set()
    for entry in skills:
        text = entry.read_text(encoding="utf-8")
        try:
            match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", text, re.S)
            if not match:
                raise ValueError("Missing YAML frontmatter")
            meta = yaml.safe_load(match.group(1))
            if not isinstance(meta, dict):
                raise ValueError("Frontmatter must be a mapping")
            name = meta.get("name", "")
            if not isinstance(name, str) or not re.fullmatch(r"lord-[a-z0-9]+(?:-[a-z0-9]+)*", name):
                raise ValueError("Invalid lord skill name")
            if name != entry.parent.name or len(name) > 64 or name in names:
                raise ValueError("Skill name must be unique and match its folder, at most 64 characters")
            names.add(name)
            if not isinstance(meta.get("description"), str) or not meta["description"].strip():
                raise ValueError("Missing description")
            config_path = entry.parent / "agents/openai.yaml"
            if config_path.exists():
                config = yaml.safe_load(config_path.read_text(encoding="utf-8"))
                if not isinstance(config, dict):
                    raise ValueError("Codex metadata must be a mapping")
                policy = config.get("policy", {})
                if not isinstance(policy, dict):
                    raise ValueError("Codex policy must be a mapping")
                if "allow_implicit_invocation" in policy and type(policy["allow_implicit_invocation"]) is not bool:
                    raise ValueError("Invocation policy must be boolean")
                if name == "lord-doc-knowledge-governance" and policy.get("allow_implicit_invocation") is not False:
                    raise ValueError("Knowledge governance must remain explicit-only in Codex")
            elif name == "lord-doc-knowledge-governance":
                raise ValueError("Knowledge governance requires Codex invocation policy")
        except (ValueError, yaml.YAMLError) as exc:
            errors.append(f"{entry.relative_to(root)}: {exc}")

    for document in root.rglob("*.md"):
        if any(part in {".git", ".venv", "runs"} for part in document.relative_to(root).parts):
            continue
        # Check inline local path targets; external URLs and fragment contents are not fetched.
        for target in re.findall(r"\[[^\]\n]*\]\(([^\s)]+)\)", document.read_text(encoding="utf-8")):
            parsed = urlsplit(target.strip("<>"))
            if parsed.scheme or not parsed.path:
                continue
            destination = (document.parent / unquote(parsed.path)).resolve()
            if not destination.is_relative_to(root.resolve()) or not destination.exists():
                errors.append(f"{document.relative_to(root)}: invalid local target {target}")

    try:
        manifest = json.loads((root / ".codex-plugin/plugin.json").read_text(encoding="utf-8"))
        if manifest.get("name") != "lord-skills" or not re.fullmatch(r"\d+\.\d+\.\d+", manifest.get("version", "")):
            raise ValueError("Invalid plugin name/version")
        if manifest.get("skills") != "./skills/" or not (root / "skills").is_dir():
            raise ValueError("Plugin must route to the shared skills directory")
    except (OSError, ValueError, TypeError) as exc:
        errors.append(f"Codex packaging: {exc}")
    return errors, len(skills)


if __name__ == "__main__":
    failures, count = check(ROOT)
    for failure in failures:
        print(f"ERROR: {failure}", file=sys.stderr)
    if failures:
        sys.exit(1)
    print(f"Structure checks passed: {count} skill(s). Behavior and client installation were not executed.")
