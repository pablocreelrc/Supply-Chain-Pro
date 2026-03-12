---
name: end-to-end-capacity-planning
description: "Use this skill when the user needs a complete capacity planning workflow from demand forecast through aggregate production plan. Triggers: end to end capacity planning, capacity planning workflow, demand to production plan, full capacity analysis, forecast to aggregate plan, integrated capacity planning, how much capacity do I need, capacity sizing, demand forecast to production schedule, capacity requirements planning, match supply to demand, production capacity analysis, workforce and capacity plan, long-range capacity planning, capacity expansion decision, dedicated vs flexible capacity, demand pooling and capacity, seasonal capacity planning, peak capacity sizing, capacity under uncertainty, aggregate planning from forecast, chain demand forecasting newsvendor flexibility aggregate, capacity pipeline, capacity master plan, strategic capacity decision, how to plan production capacity, capacity investment analysis, multi-step capacity model, capacity planning process, capacity workflow"
---

# End-to-End Capacity Planning

## Purpose

Chain four analytical steps -- demand forecasting, newsvendor capacity sizing, flexibility/demand pooling evaluation, and aggregate planning -- into a single integrated workflow that takes historical demand data and produces an actionable production plan.

## When to Use

- You need to go from raw demand history to a finished production/staffing plan
- Seasonal or uncertain demand makes capacity sizing non-trivial
- You are evaluating whether to invest in dedicated or flexible capacity
- A capacity expansion or contraction decision requires quantified demand analysis
- You want a single integrated model rather than running four separate analyses
- You need to present a capacity plan to executives with supporting demand analysis
- You are planning for a new product launch with uncertain demand forecasts

## Foundation

### Workflow Architecture

This skill chains four foundational analyses in sequence. Each step's output feeds the next:

```
Step 1: DEMAND FORECASTING
  Input: Historical data, causal factors
  Output: Point forecast + uncertainty range
         |
         v
Step 2: NEWSVENDOR CAPACITY SIZING
  Input: Forecast distribution, cost of over/under capacity
  Output: Optimal capacity level for peak/uncertain periods
         |
         v
Step 3: FLEXIBILITY & DEMAND POOLING
  Input: Capacity level, multiple demand streams
  Output: Dedicated vs. flexible capacity recommendation
         |
         v
Step 4: AGGREGATE PLANNING
  Input: Monthly demand forecast, capacity constraints, costs
  Output: Production plan (units, workforce, inventory by period)
```

### Step 1: Demand Forecasting

**Methods by data availability:**

| Data Available | Method | Formula |
|---------------|--------|---------|
| 3+ years of history with trend/seasonality | Decomposition | Demand = Trend * Seasonal Index * Cyclical * Irregular |
| History with known causal drivers | Regression | D = b0 + b1*X1 + b2*X2 + ... + error |
| Short history or new product | Moving average / Exponential smoothing | F_t+1 = alpha * A_t + (1-alpha) * F_t |
| No history | Analogous product, expert judgment, market sizing | Top-down or bottom-up estimation |

**Forecast error:** `sigma_forecast = RMSE = sqrt(SUM(A_t - F_t)^2 / n)`

This sigma feeds directly into Step 2.

### Step 2: Newsvendor Capacity Sizing

For periods with a single commitment decision under uncertainty:

```
c_u = Margin lost per unit of insufficient capacity
c_o = Cost per unit of excess capacity
CR = c_u / (c_u + c_o)
K* = mu + NORM.S.INV(CR) * sigma
```

Apply when: capacity must be locked before demand is known (equipment purchases, lease commitments, seasonal hiring).

### Step 3: Flexibility & Demand Pooling

**Key insight:** Flexible capacity serving multiple demand streams requires less total capacity than dedicated capacity for each stream.

```
Dedicated total capacity = SUM(K*_i) for each stream i
Pooled capacity needed = K*_pooled (using pooled mu and pooled sigma)
Pooled sigma = sqrt(SUM(sigma_i^2) + 2*SUM(rho_ij * sigma_i * sigma_j))
Capacity savings = Dedicated - Pooled
```

When correlation (rho) < 1, pooling always saves capacity. Greater savings when:
- More streams are pooled
- Streams have lower correlation
- Streams have higher coefficient of variation

**Flexibility premium:** Flexible capacity costs more per unit. Worth it when:
```
Capacity Savings * c_dedicated > (Pooled Capacity) * (c_flexible - c_dedicated)
```

### Step 4: Aggregate Planning

Match production to demand over a planning horizon (typically 6-18 months):

**Decision variables per period t:** Production quantity, workforce level, inventory, overtime hours, subcontracting.

**Cost components:**

| Cost | Typical Range | Formula |
|------|--------------|---------|
| Regular labor | Base | Workers * Hours * Wage |
| Overtime | 1.5x wage | OT_hours * 1.5 * Wage |
| Hiring | $1K-5K/worker | New_hires * Hiring_cost |
| Firing/layoff | $2K-10K/worker | Layoffs * Firing_cost |
| Holding inventory | 20-30% of value/yr | End_inventory * Holding_cost/period |
| Stockout/backorder | Lost margin or penalty | Backorders * Backorder_cost |
| Subcontracting | Premium over internal | Subcontract_units * Sub_cost |

**Classic strategies:**
- **Chase:** Adjust workforce each period to match demand exactly (high hire/fire cost, low inventory)
- **Level:** Constant workforce, absorb fluctuations with inventory (low hire/fire, high holding cost)
- **Hybrid:** Blend of chase and level with overtime and subcontracting buffers

## Process

### Entry Mode 1: Guided

Ask sequentially:

1. **Historical demand data** -- how many periods? Monthly/weekly? Any known seasonality?
2. **Forecast horizon** -- how far out to plan?
3. **Capacity economics** -- cost of over-capacity vs. under-capacity? Cost per unit of capacity?
4. **Multiple demand streams?** -- if yes, how many and what is their correlation?
5. **Flexible vs. dedicated capacity costs** -- cost differential?
6. **Aggregate planning costs** -- labor rate, OT rate, hiring/firing cost, holding cost, subcontracting cost?
7. **Constraints** -- max overtime, max subcontracting, min workforce, max inventory?
8. **Output mode** -- Excel / Python / Both / Teach?

### Entry Mode 2: Context Dump

User provides a case with demand history, cost structure, and capacity constraints. Extract all parameters, map to the four steps, confirm interpretation, then produce output.

### Entry Mode 3: Quick Draft

User provides summary data inline. Parse, fill reasonable defaults for missing parameters, state all assumptions, and produce integrated output.

### Adaptive Questioning

| Input | Required For | Default If Missing |
|-------|-------------|-------------------|
| Historical demand (12+ periods ideal) | Demand Forecast | Ask -- no default |
| Forecast horizon (periods) | All tabs | 12 months |
| c_u (underage cost) | Capacity Sizing | Lost margin = Price - Cost |
| c_o (overage cost) | Capacity Sizing | Cost of idle capacity per unit |
| Number of demand streams | Flexibility Analysis | 1 (skip pooling) |
| Correlation between streams | Flexibility Analysis | 0.3 (moderate) if multiple streams |
| Flexible capacity cost premium | Flexibility Analysis | 20% above dedicated |
| Regular wage ($/hr) | Aggregate Plan | $25/hr |
| Overtime multiplier | Aggregate Plan | 1.5x |
| Hiring cost ($/worker) | Aggregate Plan | $3,000 |
| Firing cost ($/worker) | Aggregate Plan | $5,000 |
| Holding cost ($/unit/period) | Aggregate Plan | Ask -- no default |
| Hours per unit | Aggregate Plan | Ask -- no default |

## Excel Output Specification

### Tab 1: Demand Forecast

| Column | Header | Format | Content |
|--------|--------|--------|---------|
| A | Period | Text | Month/Week label |
| B | Actual Demand | #,##0 | Historical data (blue font = input) |
| C | Trend Component | #,##0 | Regression or moving average trend |
| D | Seasonal Index | 0.00 | Multiplicative seasonal factor |
| E | Forecast | #,##0 | =C_n * D_n (or additive equivalent) |
| F | Forecast Error | #,##0 | =B_n - E_n (where actuals exist) |
| G | Lower Bound (95%) | #,##0 | =E_n - 1.96 * RMSE |
| H | Upper Bound (95%) | #,##0 | =E_n + 1.96 * RMSE |

Summary section: RMSE, MAE, MAPE, forecast sigma.

### Tab 2: Capacity Sizing

| Section | Content |
|---------|---------|
| Parameters | c_u, c_o, CR (formulas in black, inputs in blue) |
| Optimal K* | Capacity level, z-score, service level |
| Peak Period Analysis | K* for highest-demand period |
| Expected Performance | E[Utilization], E[Idle Capacity], E[Shortage] |
| Sensitivity | K* and expected cost across CR values (0.3 to 0.9) |

### Tab 3: Flexibility Analysis

| Column | Header | Format | Content |
|--------|--------|--------|---------|
| A | Demand Stream | Text | Stream name/ID |
| B | Mean Demand | #,##0 | mu_i (blue font) |
| C | Std Dev | #,##0 | sigma_i (blue font) |
| D | Dedicated K* | #,##0 | =B_n + NORM.S.INV(CR) * C_n |
| E | Pooled Contribution | #,##0 | Allocated share of pooled K* |
| F | Capacity Saved | #,##0 | =D_n - E_n |

Summary: Total Dedicated, Total Pooled, Savings, Flexibility Cost Premium, Net Benefit of Pooling.

### Tab 4: Aggregate Plan

| Column | Header | Format | Content |
|--------|--------|--------|---------|
| A | Period | Text | Month label |
| B | Demand Forecast | #,##0 | =link to Demand Forecast tab (green font) |
| C | Production | #,##0 | Planned output |
| D | Workers | #,##0 | Workforce level |
| E | Hired | #,##0 | =MAX(D_n - D_(n-1), 0) |
| F | Fired | #,##0 | =MAX(D_(n-1) - D_n, 0) |
| G | Regular Hours | #,##0 | =D_n * HoursPerDay * WorkDays |
| H | Overtime Hours | #,##0 | Additional hours needed |
| I | Subcontracted | #,##0 | Units outsourced |
| J | Ending Inventory | #,##0 | =J_(n-1) + C_n - B_n |
| K | Period Cost ($) | #,##0 | Sum of all cost components |

Strategies compared: Chase row totals vs. Level row totals vs. Hybrid row totals. Highlight lowest-cost strategy.

### Tab 5: Executive Summary

| Row | Content |
|-----|---------|
| Demand Summary | Forecast range, growth trend, seasonality strength |
| Capacity Recommendation | Optimal capacity level with confidence interval |
| Flexibility Decision | Dedicated vs. flexible with financial justification |
| Production Plan | Recommended aggregate strategy with total cost |
| Key Risks | Top 3 risks and mitigation actions |

### Tab 6: Assumptions

| Cell | Label | Default Value | Format |
|------|-------|--------------|--------|
| B2 | Forecast Method | Decomposition | Text |
| B3 | Confidence Level | 95% | 0.0% |
| B4 | Underage Cost (c_u) | (user input) | $#,##0 |
| B5 | Overage Cost (c_o) | (user input) | $#,##0 |
| B6 | Number of Demand Streams | 1 | #,##0 |
| B7 | Correlation Between Streams | 0.3 | 0.00 |
| B8 | Flexible Capacity Premium | 20% | 0.0% |
| B9 | Regular Wage ($/hr) | 25 | $#,##0 |
| B10 | OT Multiplier | 1.5 | 0.0x |
| B11 | Hiring Cost ($/worker) | 3,000 | $#,##0 |
| B12 | Firing Cost ($/worker) | 5,000 | $#,##0 |
| B13 | Holding Cost ($/unit/period) | (user input) | $#,##0.00 |
| B14 | Hours per Unit | (user input) | 0.00 |

All cells blue font, yellow fill. Named ranges for all parameters.

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
Deliver formatted .xlsx with all 6 tabs per spec above. Use Shortcut.ai API.

### Python Mode
Deliver a self-contained Python script with:
- `forecast_demand(history, horizon, method)` returning forecast with confidence bands
- `newsvendor_capacity(mu, sigma, c_u, c_o)` returning K* and performance metrics
- `pooling_analysis(streams_list, correlation_matrix, cr)` returning dedicated vs. pooled capacity
- `aggregate_plan(forecast, costs, constraints, strategy)` returning period-by-period plan
- `run_pipeline(history, params)` chaining all four steps
- Console summary and matplotlib charts (forecast plot, capacity sensitivity, aggregate plan timeline)

### Both Mode
Deliver Excel file + Python script.

### Teach Mode
Step-by-step walkthrough:
1. Decompose historical demand into trend and seasonality; generate forecast
2. Calculate forecast error and uncertainty range
3. Frame the capacity decision as a newsvendor problem; compute CR and K*
4. Evaluate dedicated vs. flexible capacity with pooling math
5. Build chase, level, and hybrid aggregate plans; compare total costs
6. Synthesize into an executive recommendation

## Anti-Patterns

| # | Mistake | Why It Is Wrong | Correct Approach |
|---|---------|----------------|-----------------|
| 1 | Using point forecast without uncertainty range for capacity sizing | Capacity sized to mean demand has a 50% chance of shortage; the whole point of Steps 2-3 is to account for uncertainty | Always carry forecast sigma through to capacity sizing; use newsvendor CR |
| 2 | Sizing capacity for average demand instead of peak periods | Peak demand drives capacity requirements; average demand drives utilization | Size to peak (adjusted by CR), then evaluate utilization across all periods |
| 3 | Ignoring correlation between demand streams in pooling analysis | Assuming independence (rho=0) overstates pooling benefits; assuming perfect correlation (rho=1) understates them | Estimate actual correlation from historical data; sensitivity-test across rho values |
| 4 | Applying newsvendor to every period in the aggregate plan | Newsvendor is for one-shot decisions; aggregate planning allows inventory carry-over between periods | Use newsvendor for total capacity sizing, then aggregate planning for period allocation |
| 5 | Comparing chase vs. level strategies on production cost alone | Hiring/firing costs, overtime premiums, and inventory holding costs dominate the comparison; ignoring them inverts the ranking | Include ALL cost components: regular labor, OT, hiring, firing, holding, stockout, subcontracting |
| 6 | Treating the four steps as independent analyses | Each step's output constrains the next; a forecast error change cascades through capacity, pooling, and planning | Run the full pipeline; when assumptions change, rerun from the affected step forward |
| 7 | Using annual averages for seasonal capacity planning | Seasonality is the reason you need capacity planning; averaging it away defeats the purpose | Preserve monthly/weekly granularity through all four steps |
| 8 | Ignoring the cost of flexible capacity when recommending pooling | Flexible equipment and cross-trained workers cost more per unit; pooling only wins if savings exceed the premium | Always compute net benefit = capacity savings * dedicated cost - pooled capacity * cost premium |
| 9 | Setting capacity equal to K* without considering aggregate plan feasibility | K* may not be achievable given workforce constraints, lead times, or facility limits | Validate K* against aggregate planning constraints before finalizing |
| 10 | Presenting four separate analyses without an executive summary | Decision-makers need the integrated recommendation, not four disconnected tables | Always include an Executive Summary tab that synthesizes the workflow into 3-5 key findings |

## Related Skills

- **Demand Forecasting** (`foundations/demand-forecasting/`) -- Step 1 of this workflow; provides forecast methods and error calculation
- **Newsvendor Model** (`foundations/newsvendor-model/`) -- Step 2; single-period capacity/inventory sizing under uncertainty
- **Flexibility & Demand Pooling** (`foundations/flexibility-demand-pooling/`) -- Step 3; dedicated vs. flexible capacity evaluation
- **Aggregate Planning** (`foundations/aggregate-planning/`) -- Step 4; period-by-period production and workforce planning
