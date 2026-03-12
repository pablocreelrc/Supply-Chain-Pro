---
name: safety-stock-policy
description: "Use this skill when the user needs to set safety stock levels, reorder points, or inventory review policies under demand and/or lead time uncertainty. Triggers: safety stock, reorder point, ROP, service level target, fill rate target, continuous review, periodic review, Q R policy, T S policy, order-up-to, base stock, lead time demand variability, demand variability, sigma lead time, risk pooling, inventory centralization, pooling effect, square root rule, coefficient of variation, CV, cycle service level, in-stock probability, how much safety stock, buffer inventory, when to reorder, stockout risk, ABC classification safety stock"
---

# Safety Stock & Reorder Policy

## Purpose

Determine how much buffer inventory to hold and when/how to trigger replenishment orders so that stockout probability stays within a target service level. Covers continuous review (Q,R), periodic review (T,S), and risk pooling across locations.

## When to Use

- Setting or revising safety stock levels for SKUs
- Choosing between continuous and periodic review systems
- Defining reorder points for an inventory management system
- Evaluating the benefit of centralizing inventory (risk pooling)
- Translating a service level target into concrete inventory parameters
- Analyzing the impact of lead time variability on stock requirements

## Foundation

### Demand Variability Over Lead Time

The core challenge: you must cover demand during the lead time (or review period + lead time). Variability compounds over this exposure period.

| Scenario | Formula for sigma_L |
|----------|-------------------|
| Variable demand, fixed lead time | `sigma_L = sigma_D * sqrt(L)` |
| Fixed demand, variable lead time | `sigma_L = D_bar * sigma_LT` |
| Both variable (independent) | `sigma_L = sqrt(L * sigma_D^2 + D_bar^2 * sigma_LT^2)` |

Where: `sigma_D` = std dev of demand per period, `L` = lead time in periods, `D_bar` = mean demand per period, `sigma_LT` = std dev of lead time in periods.

### Safety Stock

`SS = z * sigma_L`

Where `z` = safety factor from target service level:
- `z = NORM.S.INV(CSL)` for cycle service level (probability of no stockout per cycle)

Common z-values: 90% -> 1.28, 95% -> 1.65, 97.5% -> 1.96, 99% -> 2.33, 99.5% -> 2.58.

### Continuous Review (Q, R) Policy

**How it works:** Monitor inventory continuously. When inventory position hits R, order quantity Q.

| Parameter | Formula |
|-----------|---------|
| Reorder point R | `D_bar * L + SS` |
| Order quantity Q | Typically EOQ: `sqrt(2 * D * S / h)` |
| Safety stock SS | `z * sigma_L` |
| Average inventory | `Q/2 + SS` |
| Average orders/year | `D / Q` |

**Fill Rate (Type 2 service):** `FR = 1 - sigma_L * L(z) / Q`

Where `L(z) = phi(z) - z * (1 - PHI(z))` is the standard normal loss function.

### Periodic Review (T, S) Policy

**How it works:** Every T periods, order up to level S. Order quantity varies each cycle.

| Parameter | Formula |
|-----------|---------|
| Review period T | Set by business constraints or optimized |
| Protection period | `T + L` |
| sigma for protection period | `sigma_D * sqrt(T + L)` (if demand variable, LT fixed) |
| Order-up-to level S | `D_bar * (T + L) + z * sigma_D * sqrt(T + L)` |
| Safety stock SS | `z * sigma_D * sqrt(T + L)` |
| Average inventory | `D_bar * T / 2 + SS` |
| Order quantity (average) | `D_bar * T` |

**Key difference from (Q,R):** Must protect over T+L, not just L. This means more safety stock for the same service level.

### Risk Pooling (Centralization)

When demand across `n` locations is independent with identical distributions:

| Metric | Decentralized (n locations) | Centralized (1 location) |
|--------|---------------------------|-------------------------|
| Total SS | `n * z * sigma_L` | `z * sigma_L * sqrt(n)` |
| SS reduction | -- | `1 - 1/sqrt(n)` fraction saved |

**General (non-identical, correlated):**
`sigma_pooled = sqrt(SUM_i(sigma_i^2) + 2 * SUM_{i<j}(rho_ij * sigma_i * sigma_j))`

If demands are positively correlated, pooling benefit shrinks. If uncorrelated (rho=0), the sqrt(n) rule applies.

### Coefficient of Variation

`CV = sigma_D / D_bar`

Higher CV items benefit most from risk pooling and need proportionally more safety stock. CV is useful for ABC/XYZ classification.

## Process

### Entry Mode 1: Guided

Ask sequentially:

1. **Item(s)** -- single SKU or portfolio?
2. **Demand stats** -- mean and std dev of demand per period, what period (daily/weekly)?
3. **Lead time** -- mean lead time, variability? Fixed or stochastic?
4. **Service target** -- cycle service level (%) or fill rate (%)?
5. **Review system** -- continuous or periodic? If periodic, review interval T?
6. **Risk pooling** -- multiple locations to compare centralized vs decentralized?
7. **Output mode** -- Excel / Python / Both / Teach?

### Entry Mode 2: Context Dump

User provides a case with demand data, lead times, service targets. Extract parameters, confirm interpretation, produce output.

### Entry Mode 3: Quick Draft

User says something like "safety stock, D=100/week, sigma=30/week, L=2 weeks, CSL=95%." Parse and produce output.

## Excel Output Specification

### Tab 1: Safety Stock Calculator

| Section | Content |
|---------|---------|
| Inputs | D_bar, sigma_D, period, L, sigma_LT, target CSL (blue font, yellow fill) |
| Calculations | sigma_L (formula shown), z, SS |
| Results | SS in units, SS in dollars (= SS * unit cost), SS in days of supply |
| Scenario table | SS at 90%, 95%, 97.5%, 99%, 99.5% service levels |

### Tab 2: Reorder Policy (Q, R)

| Section | Content |
|---------|---------|
| Inputs | All from Tab 1 + S (order cost), h (holding cost), unit cost |
| EOQ | Q* calculation |
| Reorder Point | R = D_bar * L + SS |
| Performance | Avg inventory (units, $), annual holding cost, annual order cost, fill rate |
| Summary | "Order Q* units when inventory position reaches R" |

### Tab 3: Periodic Review (T, S)

| Section | Content |
|---------|---------|
| Inputs | All from Tab 1 + T (review interval) |
| Protection period | T + L |
| Order-up-to S | D_bar * (T+L) + z * sigma_D * sqrt(T+L) |
| Performance | Avg inventory, avg order quantity, annual cost |
| Comparison | Side-by-side vs (Q,R) on total cost and avg inventory |

### Tab 4: Risk Pooling Analysis

| Section | Content |
|---------|---------|
| Location table | Location, D_i, sigma_i, SS_i (input rows, yellow fill) |
| Decentralized | Total SS, total avg inventory, total cost |
| Centralized | Pooled sigma, pooled SS, pooled avg inventory, pooled cost |
| Savings | SS reduction (units, $, %), inventory reduction |
| Correlation sensitivity | Savings at rho = 0, 0.25, 0.5, 0.75, 1.0 |

### Tab 5: Assumptions

Key assumptions: demand is normally distributed, lead time is constant (or normally distributed), no demand-lead time correlation, no capacity constraints, no order crossover, single-echelon.

## Output

### Excel Mode
Deliver formatted .xlsx with all 5 tabs. Use Shortcut.ai API. IB formatting standards.

### Python Mode
Self-contained script with:
- `compute_safety_stock(d_bar, sigma_d, L, sigma_lt, csl)` returning SS, ROP, sigma_L
- `qr_policy(d_bar, sigma_d, L, sigma_lt, csl, S_cost, h)` returning Q, R, avg inventory, costs
- `ts_policy(d_bar, sigma_d, L, T, csl)` returning S, avg inventory
- `risk_pooling(locations, csl)` returning centralized vs decentralized comparison
- Console summary + matplotlib charts (SS vs service level curve, pooling savings by n)

### Both Mode
Excel file + Python script.

### Teach Mode
Step-by-step walkthrough:
1. Explain why safety stock exists (buffer against variability during lead time)
2. Calculate sigma_L -- emphasize which variability formula applies
3. Look up z from service level, compute SS
4. Build the reorder point or order-up-to level
5. Show cost of higher service (SS grows exponentially near 100%)
6. Demonstrate risk pooling savings if multi-location

## Anti-Patterns

1. **Using sigma_D directly as sigma_L.** You must scale demand variability over the lead time. sigma_L = sigma_D * sqrt(L), not sigma_D. This is the most common error.
2. **Ignoring lead time variability.** If lead times vary, the D_bar^2 * sigma_LT^2 term can dominate. Ignoring it causes chronic stockouts.
3. **Targeting 100% service level.** SS approaches infinity as CSL -> 100%. Going from 99% to 99.5% roughly doubles safety stock. Always frame the cost-service tradeoff.
4. **Applying sqrt(n) pooling to correlated demands.** The sqrt(n) reduction assumes independence. Stores in the same region often have correlated demand; pooling benefit is smaller.
5. **Over-aggregating dissimilar items.** Pooling a fast-mover (low CV) with a slow-mover (high CV) can increase total inventory if the slow-mover dominates variability.
6. **Confusing cycle service level with fill rate.** CSL = P(no stockout per replenishment cycle). Fill rate = fraction of demand met from stock. A 95% CSL often corresponds to 98-99% fill rate. Know which one your business targets.
7. **Forgetting the review period in periodic review.** (T,S) must protect over T+L, not just L. Omitting T from the protection period drastically understocks.
8. **Using days-of-supply as the only metric.** "30 days of safety stock" ignores variability. A high-CV item needs more days than a low-CV item for the same service level. Always base SS on sigma_L and z.
9. **Setting SS once and never updating.** Demand patterns, lead times, and costs change. Safety stock parameters should be reviewed at least quarterly.
10. **Ignoring pipeline inventory.** Inventory in transit counts toward inventory position in (Q,R). If your system doesn't track in-transit, you'll over-order.

## Related Skills

- `eoq-cycle-inventory` -- for determining order quantity Q in (Q,R) policy
- `network-design` -- for broader network decisions where risk pooling is one factor
