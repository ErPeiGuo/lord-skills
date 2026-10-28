"""Synthetic row-limit fixture; not a complete CSV export implementation."""

MAX_EXPORT_ROWS = 20000


def validate_rows(rows):
    if len(rows) > MAX_EXPORT_ROWS:
        raise ValueError("Export row limit exceeded")
