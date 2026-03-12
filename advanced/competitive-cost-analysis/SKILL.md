---
name: competitive-cost-analysis
description: "Use this skill when the user needs to benchmark operations against competitors, map value chains, or identify structural cost advantages. Triggers: competitive cost analysis, value chain mapping, cost benchmarking, cost driver analysis, unit economics comparison, cost advantage, cost leadership, structural advantage, competitive positioning, value chain analysis, porter value chain, inbound logistics cost, outbound logistics cost, operations benchmarking, cost per unit comparison, competitor cost structure, where do we have cost advantage, cost breakdown by activity, activity-based costing vs competitor, scale economies analysis, utilization advantage, technology cost driver, location cost driver, labor cost driver, cost position sustainability, relative cost position, cost parity, cost gap analysis, strategic cost management, competitive unit economics, margin benchmarking, cost waterfall, cost bridge analysis, operational efficiency comparison"
---

# Competitive Cost Analysis

## Purpose

Benchmark your operations against competitors by decomposing the value chain into discrete activities, quantifying cost drivers at each stage, comparing unit economics, and identifying structural advantages or vulnerabilities in your cost position.

## When to Use

- You need to understand WHY your costs are higher or lower than a competitor's
- You are evaluating whether a cost advantage is structural (durable) or temporary
- A strategic decision depends on knowing your relative cost position (make vs. buy, enter vs. exit)
- You want to identify which value chain activities offer the greatest improvement potential
- You are preparing a competitive positioning analysis for an investment memo or board presentation
- You need to quantify the impact of scale, utilization, technology, location, or labor on costs
- You are designing a cost leadership or cost parity strategy

## Foundation

### Value Chain Activities

The value chain decomposes operations into primary and support activities. Each activity consumes resources and creates (or destroys) value.

**Primary Activities:**

| Activity | Scope | Typical Cost Drivers |
|----------|-------|---------------------|
| Inbound Logistics | Receiving, warehousing, inventory management of inputs | Supplier proximity, inbound volume, modal mix |
| Operations | Transforming inputs into finished products | Scale, utilization, technology, process yield |
| Outbound Logistics | Storage, distribution, delivery to customer | Network density, drop size, route efficiency |
| Marketing & Sales | Demand generation, pricing, channel management | Brand strength, channel mix, customer acquisition cost |
| Service | Post-sale support, returns, warranties | Product quality, complexity, service model |

**Support Activities:** Procurement, Technology Development, Human Resource Management, Firm Infrastructure (overhead).

### Cost Driver Framework

Every cost difference between competitors can be traced to one or more structural or executional drivers:

| Driver Type | Driver | How It Affects Cost |
|-------------|--------|-------------------|
| Structural | Scale | Higher volume spreads fixed costs; purchasing leverage |
| Structural | Scope | Shared resources across products/segments reduce per-unit cost |
| Structural | Location | Labor rates, real estate, tax, proximity to inputs/customers |
| Structural | Vertical Integration | Eliminates margin stacking but adds complexity |
| Executional | Utilization | Higher asset utilization lowers per-unit depreciation and overhead |
| Executional | Technology | Automation, digitization reduce labor and error costs |
| Executional | Labor Productivity | Output per labor hour; training, retention, process design |
| Executional | Process Yield | Scrap, rework, and defect rates directly inflate unit cost |

### Unit Economics

```
Unit Cost = (Total Fixed Costs / Volume) + Variable Cost per Unit
Contribution Margin = Price - Variable Cost per Unit
Breakeven Volume = Total Fixed Costs / Contribution Margin
```

**Cost Waterfall:** Start from competitor's estimated unit cost, add/subtract each driver's differential to arrive at your unit cost. The waterfall makes it visual which drivers explain the gap.

### Sustainability Test

A cost advantage is sustainable when:
1. It is driven by structural factors (scale, location) rather than executional ones alone
2. Competitors face high switching costs or long lead times to replicate
3. The advantage compounds over time (learning curves, network effects)
4. It does not depend on a single input price that can change abruptly

## Process

### Entry Mode 1: Guided

Ask sequentially:

1. **Your company/product** -- what operation are you analyzing?
2. **Competitor(s)** -- who are you benchmarking against? (1-3 competitors ideal)
3. **Value chain scope** -- full chain or specific activities?
4. **Cost data** -- what cost figures do you have (yours and estimates for competitors)?
5. **Key cost drivers** -- which drivers do you suspect matter most?
6. **Output mode** -- Excel / Python / Both / Teach?

### Entry Mode 2: Context Dump

User provides a case, annual report data, or industry analysis. Extract company and competitor cost structures, volumes, and key operational metrics. Confirm interpretation, then produce output.

### Entry Mode 3: Quick Draft

User provides inline data like "Our COGS is $42/unit at 500K units, competitor is $38/unit at 800K units, both in Texas." Parse directly, fill reasonable defaults, and produce output.

### Adaptive Questioning

| Input | Required For | Default If Missing |
|-------|-------------|-------------------|
| Company cost data (total or per-unit) | All tabs | Ask -- no default |
| Competitor cost data (total or per-unit) | Unit Economics Comparison | Ask -- no default |
| Volume (units produced/sold) | Unit Economics, Cost Drivers | Ask -- no default |
| Value chain activity breakdown | Value Chain Map | Equal split across 5 primaries if unknown |
| Cost driver magnitudes | Cost Driver Analysis | Qualitative High/Med/Low if no numbers |
| Fixed vs. variable split | Unit Economics | Industry-typical 40/60 if unknown |

## Excel Output Specification

### Tab 1: Value Chain Map

| Column | Header | Format | Content |
|--------|--------|--------|---------|
| A | Activity | Text, left-aligned | Inbound, Operations, Outbound, Marketing, Service, Support |
| B | Your Cost ($) | #,##0 | Total cost per activity (blue font = input) |
| C | Your Cost (%) | 0.0% | =B_n/SUM(B) |
| D | Competitor Cost ($) | #,##0 | Estimated cost per activity (blue font = input) |
| E | Competitor Cost (%) | 0.0% | =D_n/SUM(D) |
| F | Difference ($) | #,##0;(#,##0) | =B_n-D_n |
| G | Advantage? | Text | =IF(F_n<0,"You","Competitor") |

Conditional formatting: green fill for activities where you have advantage, red where competitor does.

### Tab 2: Cost Driver Analysis

| Column | Header | Format | Content |
|--------|--------|--------|---------|
| A | Cost Driver | Text | Scale, Utilization, Technology, Location, Labor, Yield, Scope, Integration |
| B | Your Metric | General | Quantitative measure (blue font = input) |
| C | Competitor Metric | General | Quantitative measure (blue font = input) |
| D | Impact on Unit Cost ($) | #,##0.00;(#,##0.00) | Estimated per-unit cost impact of the gap |
| E | Driver Type | Text | Structural or Executional |
| F | Replicability | Text | Low / Medium / High |

Summary row: total unit cost gap explained by drivers.

### Tab 3: Unit Economics Comparison

| Column | Header | Format | Content |
|--------|--------|--------|---------|
| A | Metric | Text | Revenue/Unit, Variable Cost/Unit, Contribution Margin, Fixed Cost/Unit, Total Unit Cost, Unit Profit, Breakeven Volume |
| B | Your Company | #,##0.00 | Values (blue font for inputs, black for formulas) |
| C | Competitor 1 | #,##0.00 | Values |
| D | Competitor 2 | #,##0.00 | Values (if applicable) |
| E | Difference (You vs C1) | #,##0.00;(#,##0.00) | =B_n - C_n |

Include cost waterfall section below: starting from competitor unit cost, add/subtract each driver to bridge to your unit cost.

### Tab 4: Strategic Position

| Row | Content |
|-----|---------|
| Header | Assessment of cost position sustainability |
| Advantages | List of structural advantages with magnitude and durability rating |
| Vulnerabilities | List of cost disadvantages with risk rating |
| Recommendations | 3-5 actionable recommendations ranked by impact and feasibility |
| Scenario | What happens if competitor invests to close the gap? |

### Tab 5: Assumptions

| Cell | Label | Default Value | Format |
|------|-------|--------------|--------|
| B2 | Your Annual Volume | (user input) | #,##0 |
| B3 | Competitor Annual Volume | (user input) | #,##0 |
| B4 | Your Total Cost | (user input) | $#,##0 |
| B5 | Competitor Total Cost | (user input) | $#,##0 |
| B6 | Fixed/Variable Split (You) | 40% | 0.0% |
| B7 | Fixed/Variable Split (Comp) | 40% | 0.0% |
| B8 | Analysis Period | Annual | Text |

All cells blue font, yellow fill. Named ranges: `YourVolume` -> B2, `CompVolume` -> B3, etc.

### Formatting Summary

Per `references/excel-standards.md`:
- **Blue font (0,0,255):** All input cells and all values on the Assumptions tab
- **Black font (0,0,0):** All formula cells
- **Green font (0,128,0):** Formula cells that reference a different sheet
- **Negatives:** Parentheses format -- ($1,234), never minus signs
- **Headers:** Bold, white font on navy background, bottom border
- **Freeze panes:** Row 1 and Column A on each data tab
- **No merged cells** in data ranges

## Output

### Excel Mode
Deliver formatted .xlsx with all 5 tabs per spec above. Use Shortcut.ai API.

### Python Mode
Deliver a self-contained Python script with:
- `build_value_chain(activities_dict_you, activities_dict_comp)` returning comparison DataFrame
- `unit_economics(price, var_cost, fixed_cost, volume)` returning dict of metrics
- `cost_waterfall(your_cost, comp_cost, drivers_dict)` returning bridge DataFrame
- Console summary and matplotlib waterfall chart

### Both Mode
Deliver Excel file + Python script.

### Teach Mode
Step-by-step walkthrough:
1. Map the value chain and explain each activity's role
2. Identify cost drivers and explain structural vs. executional
3. Build unit economics for both firms with reasoning
4. Construct the cost waterfall bridge
5. Assess sustainability of the cost position
6. Recommend strategic actions

## Anti-Patterns

| # | Mistake | Why It Is Wrong | Correct Approach |
|---|---------|----------------|-----------------|
| 1 | Comparing total costs without normalizing for volume | A larger firm always has higher total costs; the comparison is meaningless without per-unit normalization | Always compute and compare unit costs at each firm's actual volume |
| 2 | Treating all cost differences as structural | Executional advantages (utilization, yield) can be replicated faster than structural ones (scale, location) | Classify each driver and assess replicability separately |
| 3 | Ignoring the fixed/variable split | Firms with different cost structures behave differently at different volumes; one may have lower cost at 500K units but higher at 1M | Model unit cost as a function of volume, not a single point |
| 4 | Using industry averages as competitor costs | Industry averages mask the variance; your actual competitor may be far above or below average | Use competitor-specific data from filings, teardowns, or expert estimates |
| 5 | Mapping only primary activities | Support activities (procurement, technology, HR, overhead) often account for 20-40% of total cost | Include all support activities in the value chain map |
| 6 | Assuming cost advantage equals competitive advantage | A cost leader may still lose if the product lacks differentiation or the market values features over price | Pair cost analysis with willingness-to-pay and differentiation assessment |
| 7 | Treating location advantage as permanent | Labor arbitrage erodes as wages rise; tax incentives expire; logistics costs change with fuel prices | Stress-test location-driven savings under adverse scenarios |
| 8 | Ignoring capacity utilization differences | Two identical plants have very different unit costs at 60% vs. 90% utilization; this is often the largest executional driver | Always collect and compare utilization rates |
| 9 | Double-counting cost drivers | Scale affects purchasing AND fixed cost spreading; attributing the full gap to both overstates the total | Use a waterfall that sums to the actual total gap -- no more, no less |
| 10 | Presenting the analysis without actionable recommendations | A cost map without "so what" is an academic exercise | End with ranked, specific actions: which driver to attack, expected savings, timeline |

## Related Skills

- **Supply Chain Contracting** (`foundations/supply-chain-contracting/`) -- Contract structures affect cost position through risk allocation and incentive alignment
- **Network Design** (`advanced/network-design/`) -- Facility location and network structure are primary drivers of logistics cost position
