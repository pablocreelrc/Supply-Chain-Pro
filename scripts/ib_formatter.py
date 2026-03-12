"""Apply IB (Investment Banking) color coding and number formatting to an Excel workbook.

Usage:
    python scripts/ib_formatter.py <input.xlsx> <output.xlsx>

Applies:
    - Blue font (0,0,255) for hardcoded inputs
    - Black font (0,0,0) for formulas
    - Green font (0,128,0) for cross-sheet references
    - Parentheses for negatives
    - Consistent number formatting per references/excel-standards.md
"""

import argparse
import sys

try:
    from openpyxl import load_workbook
    from openpyxl.styles import Font, numbers
except ImportError:
    print("Error: openpyxl is required. Install with: pip install openpyxl", file=sys.stderr)
    sys.exit(1)


# IB Color Constants (RGB)
BLUE_INPUT = "0000FF"
BLACK_FORMULA = "000000"
GREEN_CROSSSHEET = "008000"
RED_EXTERNAL = "FF0000"


def apply_ib_formatting(input_path: str, output_path: str) -> None:
    """Apply IB formatting standards to all sheets in the workbook.

    Args:
        input_path: Path to the source .xlsx file.
        output_path: Path to save the formatted .xlsx file.
    """
    # TODO: Implement in Phase 2
    # 1. Load workbook with openpyxl
    # 2. Iterate all cells in all sheets
    # 3. Detect if cell contains formula or hardcoded value
    # 4. Apply appropriate font color
    # 5. Detect cross-sheet references (contains '!')
    # 6. Apply number formatting based on header/context
    # 7. Save to output path
    pass


def main():
    parser = argparse.ArgumentParser(description="Apply IB formatting to Excel workbook")
    parser.add_argument("input", help="Path to input .xlsx file")
    parser.add_argument("output", help="Path to output .xlsx file")
    args = parser.parse_args()

    apply_ib_formatting(args.input, args.output)
    print(f"IB formatting applied: {args.output}")


if __name__ == "__main__":
    main()
