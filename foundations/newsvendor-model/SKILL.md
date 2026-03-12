---
name: newsvendor-model
description: "Use this skill when the user needs to make a ONE-TIME inventory or capacity decision under demand uncertainty. Triggers: newsvendor, single-period, overage, underage, critical ratio, critical fractile, perishable inventory, seasonal ordering, one-shot order, how much to stock, how many to order, optimal order quantity under uncertainty, stocking decision, fashion buying, demand uncertainty, too much vs too little, salvage value, stockout cost, expected profit under uncertainty, EVPI, value of perfect information, news vendor, style goods ordering"
---

# Newsvendor Model

## Purpose

Determine the profit-maximizing order/capacity quantity when you have ONE chance to commit before uncertain demand is realized. Applies to any decide-then-observe situation: seasonal buys, perishable goods, event staffing, capacity reservations, promotional inventory.

## When to Use

- Single ordering opportunity before a selling season
- Perishable product with no replenishment window
- Capacity must be locked in before demand is known
- Leftover units have a salvage/markdown value below cost
- Unmet demand carries a penalty (lost margin, goodwill, contractual)
- You need to quantify the cost of demand uncertainty (EVPI)

## Foundation

### Cost Structure

| Symbol | Name | Formula |
|--------|------|---------|
| `c_u` | Underage cost (per unit short) | `p - v + g` |
| `c_o` | Overage cost (per unit excess) | `c + v_hold - s` |
| `CR` | Critical ratio | `c_u / (c_u + c_o)` |

Where: `p` = selling price, `c` = unit cost, `s` = salvage value, `g` = goodwill/penalty cost per unit short, `v` = variable cost per unit sold, `v_hold` = variable holding cost.

When `v` and `v_hold` are zero (common simplification): `c_u = p - c + g`, `c_o = c - s`.

### Optimal Quantity

**General (any distribution):** Find `K*` such that `P(D <= K*) = CR`.

**Normal demand shortcut:** `K* = mu + z * sigma` where `z = NORM.S.INV(CR)`.

**Discrete demand:** Walk the CDF table; `K*` is the smallest quantity where cumulative probability >= CR.

### Expected Performance at K*

| Metric | Formula |
|--------|---------|
| E[Sales] | `SUM[ min(d_i, K) * P(D = d_i) ]` for discrete; `K - sigma * L(z)` for normal |
| E[Leftover] | `K - E[Sales]` |
| E[Shortage] | `E[D] - E[Sales]` |
| E[Profit] | `p * E[Sales] + s * E[Leftover] - g * E[Shortage] - c * K` |
| Fill Rate (FR) | `E[Sales] / E[D]` |
| Service Level (SL) | `P(D <= K)` (probability of no stockout) |

**Normal loss function:** `L(z) = phi(z) - z * (1 - PHI(z))`, where `phi` = standard normal PDF, `PHI` = standard normal CDF.

### Value of Perfect Information

`EVPI = E[Profit_perfect] - E[Profit_K*]`

Where `E[Profit_perfect] = SUM[ (p - c) * d_i * P(D = d_i) ]` (you order exactly demand each time).

## Process

### Entry Mode 1: Guided

Ask sequentially:

1. **Product/context** -- what are you ordering?
2. **Demand distribution** -- discrete scenarios with probabilities, or normal(mu, sigma)?
3. **Economics** -- selling price (p), unit cost (c), salvage value (s), goodwill penalty (g)?
4. **Output mode** -- Excel / Python / Both / Teach?

### Entry Mode 2: Context Dump

User provides a case or problem description. Extract p, c, s, g, demand parameters. Confirm interpretation, then produce output.

### Entry Mode 3: Quick Draft

User says something like "newsvendor, p=50, c=30, s=10, g=0, demand Normal(1000,200)." Parse directly and produce output.

## Excel Output Specification

### Tab 1: Demand Distribution

| Row | Content |
|-----|---------|
| Header | Scenario, Demand, Probability, Cumulative Probability |
| Body | One row per scenario (or discretized normal buckets) |
| Format | IB standard: Calibri 10, headers bold white-on-navy, numbers right-aligned |

For normal distribution: discretize into ~20 buckets spanning mu +/- 3*sigma.

### Tab 2: Optimal Quantity Analysis

| Section | Content |
|---------|---------|
| Parameters | p, c, s, g, c_u, c_o, CR (blue font, yellow fill for inputs) |
| Optimal K* | Value, corresponding z-score if normal |
| Performance | E[Sales], E[Leftover], E[Shortage], E[Profit], SL, FR |
| EVPI | Perfect-info profit, K* profit, EVPI value |
| Profit by K | Table: K, E[Profit], E[Sales], SL, FR for range of K values |

### Tab 3: Sensitivity

| Analysis | Method |
|----------|--------|
| Vary selling price | K* and E[Profit] across p values |
| Vary cost | K* and E[Profit] across c values |
| Vary salvage | K* and E[Profit] across s values |
| Vary sigma | K* and E[Profit] across uncertainty levels |

Each sensitivity block: data table + conditional formatting to highlight optimal region.

### Tab 4: Assumptions

Bullet list of all assumptions: single period, known distribution, price-taker, no lead-time risk, risk-neutral decision-maker, etc.

## Output

### Excel Mode
Deliver formatted .xlsx with all 4 tabs per spec above. Use Shortcut.ai API.

### Python Mode
Deliver a self-contained Python script with:
- `compute_newsvendor(p, c, s, g, mu, sigma)` returning dict of all metrics
- Sensitivity sweep function
- Console output of key results
- matplotlib profit-vs-K chart

### Both Mode
Deliver Excel file + Python script.

### Teach Mode
Step-by-step walkthrough:
1. Explain why this is a newsvendor problem
2. Calculate c_u, c_o, CR with reasoning
3. Find K* with explanation of the CDF lookup
4. Compute expected profit line by line
5. Interpret: what does this K* mean operationally?
6. Show sensitivity to key drivers

## Anti-Patterns

1. **Using average demand as order quantity.** Average demand minimizes expected leftover, NOT maximizes profit. Use CR to find K*.
2. **Ignoring salvage value.** Salvage reduces overage cost, which raises CR and increases optimal K*. Always ask about markdown/liquidation value.
3. **Confusing Service Level with Fill Rate.** SL = P(no stockout) = P(D <= K). FR = E[units sold] / E[demand]. SL is always >= FR for the same K. They answer different questions.
4. **Hardcoding the critical ratio.** CR depends on economics. If any cost parameter changes, CR changes. Always link CR to its formula cells.
5. **Applying newsvendor to a multi-period problem.** If you can reorder, this is NOT a newsvendor. Use (Q,R) or (T,S) policies instead.
6. **Treating demand scenarios as equally likely by default.** Unless told otherwise, do NOT assume uniform probability. Always confirm the distribution.
7. **Forgetting goodwill cost.** Lost future business from stockouts is real. If g > 0, it increases c_u and raises K*. Ask about contractual penalties too.
8. **Using continuous formulas on discrete data (or vice versa).** For discrete demand, walk the CDF. For continuous, use z-table/NORM.S.INV. Don't mix.
9. **Ignoring EVPI.** EVPI tells you the max you'd pay for perfect demand info. If EVPI is small relative to profit, uncertainty isn't your main problem.
10. **Not annualizing or period-matching costs.** All costs must be per the same selling period. Don't mix annual holding costs with a one-week selling window.

## Related Skills

- `eoq-cycle-inventory` -- for repeated ordering with known demand
- `safety-stock-policy` -- for continuous/periodic review under uncertainty
- `flexibility-demand-pooling` -- for reducing newsvendor risk through substitution or postponement
