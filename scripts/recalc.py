"""Recalculate all formulas in an Excel workbook via LibreOffice.

Usage:
    python scripts/recalc.py <input.xlsx>

Returns JSON to stdout:
    {"status": "ok"} or {"status": "errors_found", "error_summary": [...]}
"""

import argparse
import json
import sys


def recalculate(filepath: str) -> dict:
    """Recalculate all formulas in the workbook using LibreOffice.

    Args:
        filepath: Path to the .xlsx file.

    Returns:
        Dict with 'status' key ('ok' or 'errors_found') and optional 'error_summary'.
    """
    # TODO: Implement in Phase 2
    # 1. Launch LibreOffice in headless mode
    # 2. Open workbook, recalculate all cells
    # 3. Save and close
    # 4. Scan for formula errors (#REF!, #DIV/0!, etc.)
    # 5. Return JSON result
    pass


def main():
    parser = argparse.ArgumentParser(description="Recalculate Excel formulas via LibreOffice")
    parser.add_argument("filepath", help="Path to the .xlsx file")
    args = parser.parse_args()

    result = recalculate(args.filepath)
    if result:
        print(json.dumps(result, indent=2))
    else:
        print(json.dumps({"status": "not_implemented", "message": "Stub — implement in Phase 2"}))


if __name__ == "__main__":
    main()
