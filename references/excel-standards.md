# Excel Output Standards — IB Formatting Reference

This document defines the formatting, formula, and validation standards for all Excel workbooks produced by CRM-Analytics-Pro skills. Every analytical skill references this file.

---

## 1. Color Coding Standards

### Industry-Standard Color Conventions

| Element | Font Color | RGB | When to Use |
|---------|-----------|-----|-------------|
| Hardcoded inputs | Blue | (0, 0, 255) | Numbers the user enters or changes for scenarios |
| Formulas and calculations | Black | (0, 0, 0) | ALL cells containing formulas |
| Cross-sheet links | Green | (0, 128, 0) | Formulas pulling data from other worksheets in the same workbook |
| External links | Red | (255, 0, 0) | Links to other files |
| Key assumptions | Yellow background | (255, 255, 0) | Cells needing attention or that should be updated per scenario |

### Application Rules

- Apply color coding to the **font**, not the cell background (except yellow for assumptions)
- When a cell contains a formula that references an input, the cell is **black** (it's a formula)
- Only the original input cell is **blue**
- Be consistent — every workbook follows these conventions without exception

---

## 2. Number Formatting Standards

| Data Type | Format | Example | Notes |
|-----------|--------|---------|-------|
| Currency | `$#,##0` or `$#,##0.00` | $1,234 or $1,234.56 | Always specify units in headers: "Revenue ($mm)" |
| Negative numbers | Parentheses | ($1,234) | NEVER use minus sign: -$1,234 |
| Percentages | `0.0%` or `0.00%` | 12.5% | One decimal default; two for precision-sensitive metrics |
| Zeros | Display as "-" | - | Use custom format: `$#,##0;($#,##0);"-"` |
| Years | Text string | 2024 | NOT formatted as number (would show 2,024) |
| Multiples | `0.0x` | 3.5x | For valuation multiples, LTV/CAC ratios |
| Counts (customers, orders) | `#,##0` | 1,234 | No currency symbol |
| Large numbers | Abbreviated with units | $1.2mm | State units in column header |

### Decimal Consistency

- Within any table section, all values of the same type must use the same number of decimal places
- Currency: 0 or 2 decimals (pick one per section)
- Percentages: 1 or 2 decimals (pick one per section)
- Do not mix formats within a column

---

## 3. Formula Construction Rules

### Assumptions Placement

- Place ALL assumptions (growth rates, margins, discount rates, response rates, etc.) in **dedicated assumption cells**
- Use **cell references** in formulas, never hardcoded values
- Good: `=B5*(1+$B$6)` where B6 contains the growth rate
- Bad: `=B5*1.05` with 5% hardcoded in the formula

### Formula Error Prevention

- Verify all cell references point to the correct cells
- Check for off-by-one errors in ranges (e.g., SUM range missing the last row)
- Ensure consistent formulas across all projection periods (drag-to-fill should work cleanly)
- Test with edge cases: zero values, negative numbers, empty cells
- No unintended circular references (only use iterative calculation when explicitly required, e.g., interest on average balance)

### Formula Best Practices

- Use named ranges for key assumptions when workbook has 3+ sheets
- Use `IFERROR()` only at presentation layer, never to mask calculation errors during development
- Prefer `INDEX(MATCH())` over `VLOOKUP()` for robustness
- Use absolute references (`$B$6`) for assumptions, relative references for row/column patterns
- Keep formulas readable — break complex calculations into intermediate rows rather than nesting 5+ functions

---

## 4. Workbook Structure Standards

### Sheet Organization

- **First sheet**: Summary / Dashboard (high-level results, key metrics)
- **Second sheet**: Assumptions & Inputs (all blue-font cells live here when possible)
- **Subsequent sheets**: Detailed analysis, one per major section
- **Last sheet** (optional): Raw Data

### Visual Standards

- Clear section headers in **bold**, larger font (12-14pt vs 10-11pt body)
- Bordered tables with header row highlighted (light gray or light blue background)
- Freeze panes on header rows and label columns
- No merged cells in data ranges (breaks formulas and sorting)
- Consistent column widths within each table

---

## 5. Documentation Requirements

### Hardcoded Value Sources

Every hardcoded input should have a source comment or adjacent cell note:

Format: `Source: [System/Document], [Date], [Specific Reference]`

Examples:
- `Source: PPG Chapter 9, Table 9.1`
- `Source: MKT 382 Session 8 Data, Prof. Du`
- `Source: Company 10-K, FY2024, Page 45`
- `Source: Industry benchmark, Bain & Co 2025`

### Sheet-Level Documentation

- Each sheet should have a brief description in row 1 or a text box explaining what the sheet calculates
- State the time period, currency, and any key assumptions at the top of each sheet

---

## 6. Validation Checklist (Double-Check Protocol)

Run this checklist after building any workbook:

1. **Formula audit**: Every calculated cell contains a formula (no hardcoded results)
2. **Reference check**: All formulas reference the correct cells (no off-by-one errors)
3. **Totals tie-out**: Row totals = sum of components; column totals match
4. **Dynamic cascade**: Change an input value → verify all dependent cells update correctly
5. **Zero errors**: No `#REF!`, `#DIV/0!`, `#VALUE!`, `#N/A`, `#NAME?` anywhere in the workbook
6. **Color compliance**: Inputs are blue, formulas are black, cross-sheet links are green
7. **Format consistency**: Decimal places consistent within each section
8. **Recalculate**: Run `python scripts/recalc.py <file.xlsx>` and verify clean JSON output

---

## 7. Shortcut.ai Integration

When building Excel files programmatically:

1. Use `scripts/shortcut_bridge.py` with API key from `.env`
2. The bridge handles IB formatting automatically when instructed
3. Always run `scripts/excel_validator.py` on the output to verify compliance
4. Always run `scripts/recalc.py` to recalculate formulas

---

## 8. Common CRM Analytics Formats

These format conventions are specific to CRM/database marketing workbooks:

| Metric | Format | Example |
|--------|--------|---------|
| Customer Lifetime Value (CLV) | `$#,##0.00` | $1,234.56 |
| Response Rate | `0.00%` | 3.25% |
| RFM Score | Text (3-digit) | "555" |
| Lift | `0.00x` | 2.35x |
| Cumulative Gains | `0.0%` | 45.2% |
| Number of Customers | `#,##0` | 12,345 |
| Revenue per Customer | `$#,##0.00` | $89.50 |
| Churn Rate | `0.0%` | 4.5% |
| Retention Rate | `0.0%` | 95.5% |
| Discount Rate | `0.0%` | 10.0% |
| Net Present Value | `$#,##0` | $5,678 |
| Logistic Regression Coefficients | `0.0000` | -0.0234 |
| Odds Ratio | `0.000` | 1.025 |
| p-value | `0.0000` | 0.0012 |
| Confidence / Support / Lift (Association Rules) | `0.000` | 0.325 |
