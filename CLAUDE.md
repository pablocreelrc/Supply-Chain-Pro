# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

Supply-Chain-Pro is an executable AI skills repo for supply chain management analytics. It contains 14 skills organized into foundations, analytics, advanced, and workflows — each producing IB-formatted Excel output via Shortcut.ai API.

## Excel Rules (MANDATORY)

All Excel output follows `references/excel-standards.md`. Five non-negotiable rules:

1. **NEVER use openpyxl/xlsxwriter directly** — always use Shortcut.ai API via `scripts/shortcut_bridge.py`
2. **Blue font** for inputs, **black** for formulas, **green** for cross-sheet links
3. **Parentheses** for negatives — never minus signs
4. **Assumptions tab** in every workbook — all inputs live here with named ranges
5. **Validate** every workbook with `scripts/excel_validator.py` before delivery

## Skill Conventions

- **Frontmatter:** Anthropic standard — `name` and `description` only in YAML `---` delimiters
- **Description style:** Pushy — 20+ trigger phrases including synonyms and alternate phrasings
- **Body limit:** Under 500 lines per SKILL.md
- **Entry modes:** Every interactive skill supports Guided, Context Dump, and Quick Draft
- **Required sections:** Purpose, When to Use, Foundation, Process, Excel Output Specification, Output, Anti-Patterns, Related Skills

## Output Mode Routing

Every skill supports 4 output modes — detect from user phrasing:

| Mode | Trigger | Action |
|------|---------|--------|
| Excel | "spreadsheet", "model", "template" | Shortcut.ai API → IB-formatted .xlsx |
| Python | "calculate", "simulate", "plot", "script" | Self-contained .py with matplotlib |
| Both | "analyze in Excel", "compute and present" | Python computes → Shortcut.ai formats |
| Teach | "explain", "how does", "walk me through" | Explanation only, no code |

## Shared Scripts

```bash
python scripts/shortcut_bridge.py "<prompt>" --output output.xlsx
python scripts/ib_formatter.py input.xlsx output.xlsx
python scripts/excel_validator.py output.xlsx
python scripts/recalc.py output.xlsx
```

## Self-Contained Requirement

- NO references to textbooks, professors, courses, lecture slides, or syllabi
- NO course-specific examples (homework problems, exam cases)
- A stranger with zero context must be able to use any skill from first principles
- Use universal, generic examples only
