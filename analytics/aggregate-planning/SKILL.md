---
name: aggregate-planning
description: "Build aggregate production plans — chase, level, mixed strategies with LP optimization. Use when someone says: aggregate planning, production planning, chase strategy, level strategy, mixed strategy, workforce planning, overtime, subcontracting, inventory planning, seasonal demand, S&OP, sales and operations planning, production smoothing, hiring and firing, backorder, stockout cost, production rate, capacity planning, workforce level, inventory holding cost, demand seasonality, production schedule, labor planning, master production schedule"
---

# Aggregate Planning

## Purpose

Develop medium-term (3-18 month) production plans that balance demand with capacity using workforce, inventory, overtime, and subcontracting levers. Compare chase, level, and mixed (LP-optimized) strategies to minimize total cost while meeting demand across all periods.

## When to Use

- Planning production for the next 6-18 months with seasonal or variable demand
- Deciding between hiring/firing workers vs building inventory vs using overtime
- Evaluating subcontracting as a capacity supplement
- Building an S&OP (Sales & Operations Planning) plan
- Comparing production strategies (chase vs level vs hybrid) on total cost
- Setting workforce levels, overtime budgets, and inventory targets by period
- Translating a demand forecast into an actionable production schedule

## Foundation

### Three Core Strategies

| Strategy | How It Works | Pros | Cons |
|----------|-------------|------|------|
| **Chase** | Adjust production each period to match demand exactly | Zero inventory cost | High hiring/firing costs, workforce instability |
| **Level** | Constant production rate; inventory absorbs fluctuations | Stable workforce, smooth operations | High inventory costs, risk of stockouts |
| **Mixed** | Optimize combination of workforce changes, inventory, OT, subcontracting | Lowest total cost | More complex to plan and execute |

### Cost Components

| Cost Element | Symbol | Typical Unit |
|-------------|--------|-------------|
| Regular production | c_r | $/unit |
| Overtime production | c_ot | $/unit (usually 1.5x regular) |
| Subcontracting | c_sub | $/unit |
| Inventory holding | c_h | $/unit/period |
| Backorder / stockout | c_b | $/unit/period |
| Hiring | c_hire | $/worker |
| Firing / layoff | c_fire | $/worker |

### LP Formulation (Mixed Strategy)

**Decision Variables** (for each period t = 1, ..., T):
- P_t = units produced (regular time)
- O_t = units produced (overtime)
- S_t = units subcontracted
- I_t = ending inventory
- B_t = backorders
- W_t = workforce level
- H_t = workers hired
- F_t = workers fired

**Objective Function**:
Min Z = SUM over t of [c_r*P_t + c_ot*O_t + c_sub*S_t + c_h*I_t + c_b*B_t + c_hire*H_t + c_fire*F_t]

**Constraints**:
1. **Demand balance**: I_(t-1) + P_t + O_t + S_t - I_t + B_t - B_(t-1) = D_t
2. **Production capacity**: P_t <= k * W_t (k = units per worker per period)
3. **Overtime limit**: O_t <= OT_max * W_t
4. **Subcontracting limit**: S_t <= Sub_max
5. **Workforce balance**: W_t = W_(t-1) + H_t - F_t
6. **Non-negativity**: All variables >= 0

### Key Relationships

- Units per worker per period: k = (working days) * (units per worker per day)
- Workers needed (chase): W_t = ceiling(D_t / k)
- Level production rate: P = SUM(D_t) / T (total demand / periods)
- Cumulative production must >= cumulative demand (if no backorders allowed)

## Process

### Three Entry Modes

| Mode | User Provides | Skill Does |
|------|--------------|------------|
| **Guided** | "Plan production for seasonal demand over 6 months" | Asks for demand, costs, initial conditions; builds all strategies |
| **Context Dump** | Demand by period, all cost parameters, initial workforce/inventory | Computes chase, level, and LP-optimal plans directly |
| **Quick Draft** | "Compare chase vs level for a toy manufacturer" | Template with seasonal demand profile and typical costs |

### Adaptive Questioning

| If User Provides... | Then Ask About... |
|---------------------|-------------------|
| Demand forecast only | Cost parameters (hiring, firing, holding, OT premium), initial workforce |
| Costs but no demand | Demand by period, planning horizon length |
| Workforce data | Productivity rate (units per worker per period), OT limits |
| "No backorders allowed" | Is subcontracting available? What's the OT cap? |
| All parameters | Confirm initial inventory, any minimum ending inventory target |

## Excel Output Specification

### Tab 1: Demand Forecast
- **Row 3**: Period labels (Month 1 through T)
- **Row 4**: Demand by period (blue font, yellow fill)
- **Row 5**: Working days per period (input)
- **Row 7-10**: Summary stats: total demand, average demand, peak demand, trough demand
- Line chart of demand over planning horizon
- Cumulative demand line for graphical planning

### Tab 2: Chase Strategy
- Period-by-period table:
  - Demand, Production (= Demand), Workers needed, Workers hired, Workers fired, Inventory (= 0)
- Cost rows: regular production cost, hiring cost, firing cost, period total
- **Bottom row**: Grand total cost (double border)
- All formulas in black; demand inputs reference Tab 1

### Tab 3: Level Strategy
- Constant production rate calculated and shown
- Period-by-period table:
  - Demand, Production (constant), Ending Inventory, Backorders (if allowed)
- Cost rows: regular production cost, holding cost, backorder cost, period total
- **Bottom row**: Grand total cost (double border)
- Flag any period where cumulative production < cumulative demand

### Tab 4: Optimal Plan (LP)
- Full decision variable table by period:
  - P_t, O_t, S_t, I_t, B_t, W_t, H_t, F_t
- Cost breakdown by category and period
- **Bottom row**: Grand total cost (double border, highlighted as lowest)
- Solver setup instructions or note that Python LP was used
- Binding constraints flagged

### Tab 5: Cost Comparison
- Summary table: Strategy | Total Regular | Total OT | Total Sub | Total Inventory | Total Backorder | Total Hiring | Total Firing | **Grand Total**
- Bar chart comparing total cost across strategies
- Percentage savings of optimal vs chase and vs level
- Recommendation with rationale

### Tab 6: Assumptions
- Planning horizon and period length
- Demand source and confidence level
- Cost assumptions and sources
- Constraints (OT limits, subcontracting availability, no-backorder policy)
- Initial conditions (starting workforce, starting inventory)

## Output

| Mode | Deliverable |
|------|------------|
| **Excel** | Formatted workbook with all 6 tabs, Solver-ready LP tab, comparison charts |
| **Python** | PuLP script formulating and solving the LP, outputting optimal plan and costs |
| **Both** | Excel workbook + Python script with matching results |
| **Teach** | Walkthrough: chase calculation, level calculation, then LP formulation step-by-step |

## Anti-Patterns

1. **Ignoring cumulative demand check** -- level strategy may cause stockouts if cumulative production falls below cumulative demand
2. **Forgetting initial conditions** -- starting inventory and workforce levels affect period 1 costs significantly
3. **Treating overtime as unlimited** -- overtime is typically capped at 20-50% of regular capacity
4. **Ignoring workforce indivisibility** -- you can't hire 0.3 workers; may need integer variables
5. **Double-counting costs** -- regular production cost per unit already includes base labor; don't add it again
6. **Not including backorder cost when backorders are allowed** -- if B_t can be > 0, there must be a penalty
7. **Using chase strategy without considering morale** -- high turnover has hidden costs (training, quality, culture)
8. **Optimizing one period at a time** -- aggregate planning is inherently multi-period; myopic decisions are suboptimal
9. **Forgetting ending conditions** -- should ending inventory be zero? Should workforce return to starting level?

## Related Skills

- `demand-forecasting` -- forecast feeds directly into aggregate planning as the demand input
- `linear-programming-optimization` -- the LP engine underlying the optimal mixed strategy
