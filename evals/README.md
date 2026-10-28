# Behavioral evaluation

Each skill owns its scenarios under `evals/<skill-name>/`. These are repeatable tasks and outcome criteria, not a universal workflow or a substitute for client installation checks.

Copy only the selected fixture into an isolated temporary directory. Give the executing AI the scenario prompt, skill and necessary input files. The evaluator retains the acceptance criteria; a fresh recovery reader receives neither expected answers nor earlier chat. Do not invoke an AI service or delegate work without the authorization required by the current task.

Record the skill revision or content identity, client, model, scenario, actual output and passed/failed/skipped outcome for a real run. Temporary transcripts and artifacts belong outside the repository or in ignored `runs/` folders. Never turn a scenario definition into a claimed test result.

Available: [Document knowledge governance](lord-doc-knowledge-governance/scenarios.md).
