---
name: sustainability-operations
description: "Use this skill when the user needs to analyze environmental, social, or governance dimensions of supply chain decisions. Triggers: sustainability operations, triple bottom line, ESG supply chain, tragedy of the commons, closed-loop supply chain, reverse logistics, remanufacturing, take-back program, carbon pricing, carbon footprint, externalities, lifecycle assessment, LCA, circular economy, sustainable supply chain, green supply chain, carbon tax impact, scope 1 2 3 emissions, environmental cost accounting, cradle to cradle, cradle to grave, product stewardship, extended producer responsibility, EPR, waste reduction operations, circular supply chain, remanufacturing cost-benefit, carbon offset analysis, net zero supply chain, decarbonization roadmap, sustainable procurement, ESG metrics operations, environmental impact assessment, closed loop cost benefit, reverse logistics network, carbon calculator supply chain"
---

# Sustainability & Operations

## Purpose

Evaluate the environmental, social, and economic dimensions of supply chain decisions using triple bottom line analysis, closed-loop supply chain design, carbon footprint calculation, and lifecycle assessment to make operations both profitable and sustainable.

## When to Use

- You need to quantify the carbon footprint of a supply chain or product
- You are evaluating whether to implement a closed-loop (take-back/remanufacturing) program
- A decision requires balancing profitability against environmental or social externalities
- You need to calculate the financial impact of carbon pricing or a carbon tax on operations
- You are designing reverse logistics for product recovery, recycling, or remanufacturing
- You want ESG metrics to guide supply chain network or sourcing decisions
- You are assessing whether a "green" initiative actually pays for itself or requires subsidy

## Foundation

### Triple Bottom Line (TBL)

Decisions are evaluated on three dimensions simultaneously:

| Dimension | Measures | Supply Chain Impact |
|-----------|----------|-------------------|
| Economic (Profit) | Revenue, cost, margin, ROI | Traditional supply chain optimization |
| Environmental (Planet) | Emissions, waste, resource use, energy | Transportation mode, packaging, facility energy, product design |
| Social (People) | Labor conditions, community impact, safety | Supplier labor practices, local employment, health/safety |

A sustainable decision performs acceptably on ALL three -- not just one at the expense of others.

### Tragedy of the Commons

When shared resources (atmosphere, water, roads) have no price, individual firms over-exploit them because the cost is externalized to society. Supply chain examples:

- **Carbon emissions:** Each firm minimizes transport cost (chooses trucking) without paying for CO2 damage
- **Water use:** Factories draw from shared aquifers without reflecting scarcity cost
- **Congestion:** Just-in-time deliveries increase truck traffic, imposing costs on all road users

**Solutions:** Carbon pricing (tax or cap-and-trade), regulation, industry standards, voluntary commitments backed by transparency.

### Closed-Loop Supply Chains

A closed-loop supply chain (CLSC) integrates forward and reverse flows:

```
Raw Materials -> Manufacturing -> Distribution -> Customer
       ^                                            |
       |         Reverse Logistics                  v
       +--- Remanufacture/Recycle <--- Collection/Return
```

**Key Economics:**

| Parameter | Definition |
|-----------|-----------|
| Recovery Rate (r) | Fraction of sold units returned for processing |
| Remanufacturing Cost (c_r) | Cost to restore a returned unit to sellable condition |
| New Manufacturing Cost (c_n) | Cost to produce from virgin materials |
| Collection Cost (c_coll) | Cost to collect and transport returns |
| Salvage Value (s) | Value recovered from recycling if not remanufacturable |
| Cannibalization Rate | Fraction of remanufactured sales that displace new-product sales |

**Closed-loop is profitable when:**
```
r * (c_n - c_r - c_coll) > Fixed cost of reverse logistics infrastructure
```

Accounting for cannibalization:
```
Net Benefit = r * [(c_n - c_r - c_coll) - Cannibalization Rate * Margin_new] - Fixed Costs_reverse
```

### Carbon Footprint Calculation

Emissions are categorized by scope:

| Scope | Source | Examples |
|-------|--------|---------|
| Scope 1 | Direct emissions from owned/controlled sources | Company fleet, manufacturing furnaces |
| Scope 2 | Indirect from purchased energy | Electricity for warehouses, heating |
| Scope 3 | All other indirect (upstream and downstream) | Supplier manufacturing, customer use, end-of-life |

**Transport emissions formula:**
```
CO2 (kg) = Distance (km) * Weight (tonnes) * Emission Factor (kg CO2/tonne-km)
```

**Emission factors by mode (approximate):**

| Mode | kg CO2 / tonne-km |
|------|-------------------|
| Air freight | 0.500 - 0.600 |
| Road (truck) | 0.060 - 0.100 |
| Rail | 0.015 - 0.025 |
| Ocean | 0.008 - 0.015 |

### Lifecycle Assessment (LCA)

Evaluates environmental impact from cradle to grave (or cradle to cradle):

1. **Raw material extraction** -- mining, agriculture, forestry
2. **Manufacturing** -- energy, water, chemicals, waste
3. **Distribution** -- transport emissions, packaging waste
4. **Use phase** -- energy consumption, maintenance
5. **End of life** -- landfill, incineration, recycling, remanufacturing

Each phase is scored on: carbon emissions, water use, energy consumption, waste generation, toxicity.

## Process

### Entry Mode 1: Guided

Ask sequentially:

1. **What decision?** -- New product design, network change, supplier selection, take-back program, carbon reduction target?
2. **Scope** -- Which sustainability dimensions matter (carbon only, full TBL, ESG scorecard)?
3. **Data available** -- Emission factors, costs, volumes, distances, energy consumption?
4. **Baseline** -- Current state to compare against?
5. **Constraints** -- Regulatory requirements, corporate commitments, budget limits?
6. **Output mode** -- Excel / Python / Both / Teach?

### Entry Mode 2: Context Dump

User provides a case, sustainability report, or operational data. Extract emission sources, volumes, costs, and targets. Confirm interpretation, then produce output.

### Entry Mode 3: Quick Draft

User provides inline data like "We ship 10K tonnes/year by truck 500km, considering rail. Carbon tax is $50/tonne CO2." Parse directly and produce output.

### Adaptive Questioning

| Input | Required For | Default If Missing |
|-------|-------------|-------------------|
| Product/operation description | All tabs | Ask -- no default |
| Annual volume (units or tonnes) | All tabs | Ask -- no default |
| Transport distances and modes | Carbon Footprint | Ask -- no default |
| Energy consumption (kWh) | Carbon Footprint | Estimate from industry benchmarks |
| New manufacturing cost (c_n) | Closed-Loop tab | Ask -- no default |
| Remanufacturing cost (c_r) | Closed-Loop tab | Typically 40-60% of c_n |
| Recovery rate | Closed-Loop tab | 20% as conservative default |
| Carbon price ($/tonne CO2) | Carbon Footprint | $50/tonne (social cost of carbon) |
| Collection/reverse logistics cost | Closed-Loop tab | Estimate from distance and volume |

## Excel Output Specification

### Tab 1: Sustainability Scorecard

| Column | Header | Format | Content |
|--------|--------|--------|---------|
| A | Dimension | Text | Economic, Environmental, Social (with sub-metrics) |
| B | Metric | Text | Specific KPI name |
| C | Current State | #,##0.00 | Baseline value (blue font = input) |
| D | Proposed State | #,##0.00 | After-change value (formula or input) |
| E | Change | 0.0% | =(D_n-C_n)/C_n |
| F | Target | #,##0.00 | Corporate/regulatory target (blue font) |
| G | On Track? | Text | =IF(D_n meets F_n direction, "Yes", "Gap") |

Sections separated by bold sub-headers for Economic, Environmental, Social. Conditional formatting: green for on-track, red for gap.

### Tab 2: Closed-Loop Cost-Benefit

| Column | Header | Format | Content |
|--------|--------|--------|---------|
| A | Parameter | Text | Row labels |
| B | Value | #,##0.00 | Input or formula |
| C | Unit | Text | $/unit, %, units, $ |

Rows: Units Sold, Recovery Rate, Units Recovered, New Mfg Cost, Remfg Cost, Collection Cost, Savings per Remanufactured Unit, Gross Savings, Cannibalization Loss, Reverse Logistics Fixed Cost, Net Annual Benefit, Payback Period, NPV (5-year).

Sensitivity section below: Net Benefit vs. Recovery Rate (10% to 60%) and vs. Remanufacturing Cost.

### Tab 3: Carbon Footprint Calculator

| Column | Header | Format | Content |
|--------|--------|--------|---------|
| A | Emission Source | Text | Transport, Manufacturing, Warehousing, etc. |
| B | Scope | Text | 1, 2, or 3 |
| C | Activity Data | #,##0 | Distance*weight, kWh, fuel liters (blue font) |
| D | Emission Factor | 0.000 | kg CO2 per unit of activity (blue font) |
| E | Annual CO2 (tonnes) | #,##0.0 | =C_n*D_n/1000 |
| F | Carbon Cost ($) | #,##0 | =E_n * CarbonPrice (green font, refs Assumptions) |
| G | % of Total | 0.0% | =E_n/SUM(E) |

Summary section: Total Scope 1, Total Scope 2, Total Scope 3, Grand Total, Total Carbon Cost. Pie chart data for emissions by source.

### Tab 4: Assumptions

| Cell | Label | Default Value | Format |
|------|-------|--------------|--------|
| B2 | Carbon Price ($/tonne CO2) | 50 | $#,##0 |
| B3 | Discount Rate (for NPV) | 10% | 0.0% |
| B4 | Analysis Horizon (years) | 5 | #,##0 |
| B5 | Recovery Rate | 20% | 0.0% |
| B6 | Cannibalization Rate | 10% | 0.0% |
| B7 | Truck Emission Factor (kg CO2/t-km) | 0.080 | 0.000 |
| B8 | Rail Emission Factor (kg CO2/t-km) | 0.020 | 0.000 |
| B9 | Ocean Emission Factor (kg CO2/t-km) | 0.010 | 0.000 |
| B10 | Grid Emission Factor (kg CO2/kWh) | 0.400 | 0.000 |

All cells blue font, yellow fill. Named ranges: `CarbonPrice` -> B2, `DiscountRate` -> B3, etc.

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
Deliver formatted .xlsx with all 4 tabs per spec above. Use Shortcut.ai API.

### Python Mode
Deliver a self-contained Python script with:
- `carbon_footprint(sources_list)` returning emissions by scope and total cost
- `closed_loop_npv(c_n, c_r, c_coll, recovery_rate, volume, fixed_cost, discount_rate, years)` returning NPV and payback
- `sustainability_scorecard(metrics_dict)` returning formatted summary
- Console output and matplotlib charts (emissions pie, NPV sensitivity)

### Both Mode
Deliver Excel file + Python script.

### Teach Mode
Step-by-step walkthrough:
1. Explain the triple bottom line and why all three dimensions matter
2. Identify the tragedy-of-the-commons dynamics in the specific situation
3. Calculate carbon footprint source by source with unit conversions
4. Build the closed-loop cost-benefit analysis with reasoning
5. Assess the financial impact of carbon pricing
6. Synthesize into a sustainability scorecard with recommendations

## Anti-Patterns

| # | Mistake | Why It Is Wrong | Correct Approach |
|---|---------|----------------|-----------------|
| 1 | Ignoring Scope 3 emissions | Scope 3 often represents 70-90% of total supply chain carbon footprint; Scope 1+2 alone massively understates impact | Always estimate Scope 3, even approximately, using industry emission factors |
| 2 | Assuming remanufacturing is always profitable | Remanufacturing requires collection infrastructure, quality inspection, and may cannibalize new-product sales | Model the full cost structure including collection, cannibalization, and fixed costs before concluding profitability |
| 3 | Treating carbon price as zero when there is no current regulation | Absent a tax, the externality still exists and future regulation is increasingly likely; ignoring it misprices decisions | Use shadow carbon pricing ($40-80/tonne) to stress-test decisions against likely future costs |
| 4 | Comparing green vs. traditional options on cost alone | A green option may cost more but reduce regulatory risk, improve brand value, or qualify for subsidies | Use triple bottom line: quantify economic, environmental, AND social impacts side by side |
| 5 | Using global average emission factors for specific operations | Emission factors vary dramatically by region (grid mix), vehicle type, and fuel; a US truck is not an Indian truck | Use region-specific and mode-specific emission factors; document sources |
| 6 | Ignoring the reverse logistics network cost | Collection, sorting, and transportation of returns require real infrastructure and operating cost | Model reverse logistics as a separate cost line, not just "returns happen" |
| 7 | Double-counting emission reductions | Switching from truck to rail reduces transport emissions but may increase warehousing emissions if delivery frequency drops | Track total system emissions, not just the changed activity |
| 8 | Treating sustainability as a one-time project | Emission factors change, regulations evolve, carbon prices rise; a snapshot analysis becomes stale | Build the model for periodic refresh; link to live data where possible |
| 9 | Assuming 100% recovery rate for closed-loop analysis | Even the best take-back programs rarely exceed 40-60% recovery; assuming 100% grossly overstates benefits | Use conservative recovery rates (15-30%) as base case and sensitivity-test upward |
| 10 | Presenting environmental metrics without financial translation | Decision-makers need dollar impact; "500 tonnes CO2 reduced" is abstract without "saving $25K in carbon costs" | Always convert environmental metrics to financial equivalents using carbon price or regulatory cost |

## Related Skills

- **Competitive Cost Analysis** (`advanced/competitive-cost-analysis/`) -- Sustainability costs are part of the total cost position; green operations can be a cost advantage or disadvantage
- **Network Design** (`advanced/network-design/`) -- Facility location and transport mode decisions are the primary levers for supply chain carbon footprint
