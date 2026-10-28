# Export implementation evidence

[Source](../../src/export.py) sets `MAX_EXPORT_ROWS = 20000` and rejects requests above that limit. This is a source observation, not a runtime export or memory test. Large-export runtime behavior has not been verified.

The [contract](export.md) owns the approved target.
