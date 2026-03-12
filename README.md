# Supply-Chain-Pro

The complete supply chain management analytics toolkit — newsvendor, EOQ, safety stock, LP optimization, flexibility, contracting, forecasting, and network design with IB-formatted Excel output.

## How to Use

Each skill is a standalone `SKILL.md`. Invoke via `/mba-supply-chain` or browse individual skills. Every skill supports three entry modes:

- **Guided** — step-by-step with questions
- **Context Dump** — paste your problem, get the answer
- **Quick Draft** — reusable template with placeholder inputs

## Skill Categories

| Category | Skills | Focus |
|----------|--------|-------|
| Foundations | 3 | Newsvendor, EOQ, Safety Stock |
| Analytics | 6 | LP Optimization, Flexibility, Contracting, Aggregate Planning, Forecasting, Network Design |
| Advanced | 2 | Competitive Cost Analysis, Sustainability |
| Workflows | 2 | End-to-End Capacity Planning, Inventory System Design |
| Infrastructure | 1 | Skill Authoring Workflow |

## Workflows

| Workflow | Skills Chained |
|----------|---------------|
| End-to-End Capacity Planning | demand-forecasting → newsvendor-model → flexibility-demand-pooling → aggregate-planning |
| Inventory System Design | eoq-cycle-inventory → safety-stock-policy → network-design |

## Excel Output Standards

All analytical skills produce IB-formatted Excel workbooks:
- Blue font for inputs, black for formulas, green for cross-sheet links
- Parentheses for negatives, consistent decimal places
- Assumptions tab with named ranges
- Generated via Shortcut.ai API (never openpyxl)

## Browse Full Catalog

See [CATALOG.md](CATALOG.md) for the complete inventory with tags and links.
