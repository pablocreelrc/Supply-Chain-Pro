"""Shortcut.ai API wrapper for generating polished Excel workbooks.

Usage:
    python scripts/shortcut_bridge.py "<prompt>" [--output output.xlsx]

Reads the Shortcut.ai API key from .env file (SHORTCUT_API_KEY).
"""

import argparse
import os
import sys

try:
    from dotenv import load_dotenv
except ImportError:
    print("Warning: python-dotenv not installed. Set SHORTCUT_API_KEY env var manually.", file=sys.stderr)


def generate_excel(prompt: str, output_path: str = "output.xlsx") -> str:
    """Generate an Excel workbook via Shortcut.ai API.

    Args:
        prompt: Description of the Excel workbook to generate.
        output_path: Path to save the generated .xlsx file.

    Returns:
        Path to the generated file.
    """
    # TODO: Implement in Phase 2
    # 1. Load API key from .env
    # 2. Send prompt to Shortcut.ai API
    # 3. Receive and save Excel output
    # 4. Run ib_formatter.py on the output
    # 5. Run excel_validator.py to verify
    # 6. Return output path
    pass


def main():
    parser = argparse.ArgumentParser(description="Generate Excel via Shortcut.ai")
    parser.add_argument("prompt", help="Description of the workbook to generate")
    parser.add_argument("--output", "-o", default="output.xlsx", help="Output file path")
    args = parser.parse_args()

    # Load .env if available
    try:
        load_dotenv()
    except NameError:
        pass

    api_key = os.environ.get("SHORTCUT_API_KEY")
    if not api_key:
        print("Error: SHORTCUT_API_KEY not found in .env or environment", file=sys.stderr)
        sys.exit(1)

    result = generate_excel(args.prompt, args.output)
    if result:
        print(f"Generated: {result}")
    else:
        print("Stub — implement in Phase 2")


if __name__ == "__main__":
    main()
