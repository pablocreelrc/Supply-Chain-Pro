---
name: Skill Authoring Workflow
description: >
  Creates new SKILL.md files for Supply-Chain-Pro. Use this skill when you need to
  author a skill, write a skill, add a new skill, create a SKILL.md, build a skill file,
  draft a skill template, scaffold a skill, generate a skill document, design a skill spec,
  define a new analytical skill, set up a skill folder, bootstrap a skill, initialize a skill,
  skill format guide, skill conventions, skill quality checklist, skill standards,
  how to write a skill, skill authoring best practices, new skill setup, skill structure,
  skill frontmatter, skill body sections, skill anti-patterns template,
  add capability to the repo, extend the skill catalog, register a new skill
---

# Skill Authoring Workflow

## Purpose

Standardizes the creation of new SKILL.md files in CRM-Analytics-Pro so every skill follows the same conventions, triggers reliably, and produces consistent Excel output.

## When to Use

- You are adding a brand-new analytical or conceptual skill to this repo
- You need to remember the required SKILL.md sections and formatting rules
- You want the frontmatter template so the skill triggers correctly in Claude Code
- You are reviewing a draft SKILL.md against the quality checklist before merging
- You need to register a new skill in CATALOG.md and marketplace.json
- You want to understand why skills are structured the way they are in this repo

## Skill Template

Copy the template below when creating a new skill. Replace all `[bracketed]` placeholders. Delete any section comments (lines starting with `>>`) before finalizing.

````markdown
---
name: [Skill Name]
description: >
  [Pushy description. Start with what the skill does in one clause, then list 20+
  trigger phrases separated by commas. Include synonyms, alternate phrasings,
  common misspellings, and related jargon. The goal is to PREVENT undertriggering --
  if a user could reasonably mean this skill, a phrase here should match.]
---

# [Skill Name]

## Purpose

[One sentence. What does this skill teach and produce?]

## When to Use

- [Scenario 1 -- the most common reason a user invokes this skill]
- [Scenario 2]
- [Scenario 3]
- [Scenario 4]
- [Scenario 5]
- [Scenario 6 -- tie to a specific MKT 382 assignment or PPG chapter if applicable]
- [Scenario 7 -- optional, add more if genuinely distinct]

## Foundation

>> This is the "why" section. Teach the frameworks, formulas, and theory that
>> underpin the skill. Use tables, formulas in code blocks, and worked examples.
>> If this section would push the file over 500 lines, move the heavy theory into
>> a `references/` subfolder and summarize here with a link.

### [Framework or Concept 1]

[Explanation with formula blocks, tables, and worked examples.]

### [Framework or Concept 2]

[Explanation.]

## Process

### Entry Mode Selection

When the user invokes this skill, determine which mode fits:

**Guided Mode** -- The user wants to be walked through step by step.
1. [First question to ask]
2. [Second question]
3. [Continue until all inputs are gathered]

**Context Dump Mode** -- The user pastes a problem, dataset, or case excerpt.
1. Parse the inputs from what was provided.
2. State what you found and any assumptions.
3. Ask one clarifying question if a critical input is ambiguous, then build.

**Quick Draft Mode** -- The user says "just build it" or provides numbers inline.
Take what is given, fill reasonable defaults (state them clearly), produce output.

### Adaptive Questioning

>> List the inputs this skill needs, whether each is required, and what default
>> to use if missing. Present as a table.

| Input | Required For | Default If Missing |
|-------|-------------|-------------------|
| [Input 1] | [Which method/tab] | [Default or "Ask -- no default"] |
| [Input 2] | [Which method/tab] | [Default or "Ask -- no default"] |

### Build Steps

1. Create the Excel workbook with [N] tabs (see Excel Output Specification).
2. Enter all hardcoded inputs on the Assumptions tab in blue font.
3. Build all formulas referencing the Assumptions tab (cross-sheet links in green).
4. Apply IB formatting per `references/excel-standards.md`.
5. Run `python scripts/excel_validator.py` on the output.
6. Run `python scripts/recalc.py` on the output.
7. Present the result with a brief interpretation.

## Excel Output Specification

>> Every analytical skill MUST include this section. Reference `references/excel-standards.md`.
>> Specify each tab: name, layout (row-by-row), columns with headers, formats, and formulas.

### Tab 1: [Analysis Name]

| Column | Header | Format | Formula or Input |
|--------|--------|--------|-----------------|
| A | [Header] | [Excel format code] | [Formula text or "Input (blue)"] |
| B | [Header] | [Excel format code] | [Formula text] |

### Tab 2: [Second Analysis or Sensitivity Table]

[Same structure as Tab 1.]

### Tab N: Assumptions & Inputs

>> Always the last tab. All hardcoded values live here. Blue font, yellow background
>> on key assumptions. Define named ranges for anything referenced by other tabs.

| Cell | Label | Default Value | Format |
|------|-------|--------------|--------|
| B2 | [Assumption 1] | [value] | [format] |
| B3 | [Assumption 2] | [value] | [format] |

Named ranges: `[Name]` -> B2, `[Name]` -> B3.

### Formatting Summary

Per `references/excel-standards.md`:

- **Blue font (0,0,255):** All input cells and all values on the Assumptions tab
- **Black font (0,0,0):** All formula cells
- **Green font (0,128,0):** Formula cells that reference a different sheet
- **Negatives:** Parentheses format -- ($1,234), never minus signs
- **Headers:** Bold, light gray background, bordered
- **Freeze panes:** On header rows and label columns
- **No merged cells** in data ranges

## Output

This skill produces:

1. **A fully formulated Excel workbook** (`.xlsx`) with [N] tabs as specified above
2. **A written summary** interpreting the key results
3. **Validation confirmation** that the workbook passes `excel_validator.py` and `recalc.py`

## Anti-Patterns

>> List 8-10 specific, actionable mistakes. Not generic advice like "be careful."
>> Each row must name the mistake, explain why it is wrong, and give the fix.

| Mistake | Why It Is Wrong | Correct Approach |
|---------|----------------|-----------------|
| [Specific mistake 1] | [Concrete consequence] | [Exact fix] |
| [Specific mistake 2] | [Concrete consequence] | [Exact fix] |
| [Specific mistake 3] | [Concrete consequence] | [Exact fix] |
| [Specific mistake 4] | [Concrete consequence] | [Exact fix] |
| [Specific mistake 5] | [Concrete consequence] | [Exact fix] |
| [Specific mistake 6] | [Concrete consequence] | [Exact fix] |
| [Specific mistake 7] | [Concrete consequence] | [Exact fix] |
| [Specific mistake 8] | [Concrete consequence] | [Exact fix] |

## Related Skills

- **[Prerequisite Skill]** (`category/skill-name/`) -- [One-line relationship description]
- **[Follow-on Skill]** (`category/skill-name/`) -- [One-line relationship description]

## Sources

- **PPG Chapter [N]**: [Book title] -- [Topic covered]
- **MKT 382 Session [N]**: CRM & Database Marketing, Professor Rex Du, UT Austin McCombs -- [Topic]
````

## Quality Checklist

Run through every item before considering a SKILL.md ready to merge. A "No" on any item means the skill needs revision.

| # | Check | Pass? |
|---|-------|-------|
| 1 | **Frontmatter `description` is pushy** -- contains 20+ trigger phrases including synonyms, alternate phrasings, and related jargon | |
| 2 | **Under 500 lines** -- heavy theory moved to `references/` subfolder if needed | |
| 3 | **All three entry modes documented** -- Guided, Context Dump, and Quick Draft each have clear instructions | |
| 4 | **Excel Output Specification present** -- every analytical skill specifies tab names, column headers, Excel format codes, and formula text | |
| 5 | **Assumptions tab defined** -- last tab, blue font, yellow background on key cells, named ranges listed | |
| 6 | **Formatting summary references `references/excel-standards.md`** and restates the IB color rules (blue/black/green) | |
| 7 | **Anti-patterns are specific** -- 8-10 entries, each naming a concrete mistake with consequence and fix (not generic advice) | |
| 8 | **Related Skills use correct relative paths** -- format is `category/skill-name/` matching actual folder structure | |
| 9 | **Sources cite specific chapters and sessions** -- PPG chapter numbers and MKT 382 session numbers, not vague references | |
| 10 | **Adaptive questioning table present** -- lists every input, which method needs it, and the default if missing | |
| 11 | **Purpose is one sentence** -- not a paragraph, not a bullet list | |
| 12 | **When to Use has 5-7 bullets** -- each is a distinct scenario, not a restatement of the same idea | |

## Process for Adding a New Skill

### Step 1: Create the Folder and File

```
category/skill-name/SKILL.md
```

Where `category` is one of: `foundations`, `analytics`, `advanced`, `infrastructure`. Use lowercase kebab-case for the skill name.

If the skill requires heavy reference material (long derivations, large lookup tables, extended examples), create a `references/` subfolder inside the skill folder:

```
category/skill-name/
  SKILL.md
  references/
    theory-deep-dive.md
    example-dataset.csv
```

### Step 2: Write the SKILL.md

Copy the Skill Template above. Fill in every section. Delete the section comments (lines starting with `>>`). Run through the Quality Checklist.

### Step 3: Add to CATALOG.md

Open `CATALOG.md` at the repo root and add an entry in the appropriate category section:

```markdown
| [Skill Name] | `category/skill-name/` | [One-sentence description] |
```

### Step 4: Update marketplace.json

If the repo uses `marketplace.json` for programmatic skill discovery, add an entry:

```json
{
  "name": "skill-name",
  "category": "category",
  "path": "category/skill-name/SKILL.md",
  "description": "One-sentence description matching CATALOG.md"
}
```

### Step 5: Test the Skill

Invoke the skill with sample data to verify:

1. The description triggers correctly (try 3-4 different phrasings)
2. All three entry modes produce sensible behavior
3. The Excel output matches the specification (run `excel_validator.py`)
4. Changing an assumption on the Assumptions tab cascades through all dependent cells
5. Anti-patterns listed are genuinely things the skill avoids

## Sources

- **CLAUDE.md** (repo root): Skill conventions -- frontmatter format, description style, body limit, entry modes, required sections
- **references/excel-standards.md**: IB formatting rules applied to every analytical skill's Excel output
- **Existing skills**: `foundations/customer-lifetime-value/SKILL.md` and `analytics/rfm-analysis/SKILL.md` as canonical examples of the format
