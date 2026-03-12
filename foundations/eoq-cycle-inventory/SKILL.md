---
name: eoq-cycle-inventory
description: "Use this skill when the user needs to determine optimal order quantities, reorder intervals, or cycle inventory levels for REPEATED purchasing decisions. Triggers: EOQ, economic order quantity, order quantity, how much to order, reorder interval, cycle inventory, holding cost, ordering cost, setup cost, lot sizing, batch size, inventory turns, days of inventory, quantity discount, volume discount, price break, multi-item ordering, joint replenishment, total landed cost, order frequency, inventory carrying cost, COGS to inventory ratio, working capital in inventory, square root formula"
---

# EOQ & Cycle Inventory

## Purpose

Determine the cost-minimizing order quantity and reorder frequency when demand is ongoing and known. Balances the tradeoff: ordering more frequently reduces inventory holding cost but increases ordering/setup cost. Extends to quantity discounts, multi-item coordination, and inventory performance metrics.

## When to Use

- Repeated purchasing or production of an item with steady demand
- You need to set lot sizes or batch quantities
- Evaluating quantity discount offers from suppliers
- Computing inventory turns or days-of-inventory benchmarks
- Coordinating orders across multiple items sharing a fixed order cost
- Justifying changes to order frequency or minimum order quantities

## Foundation

### Basic EOQ

| Symbol | Meaning |
|--------|---------|
| `D` | Annual demand (units/year) |
| `S` | Fixed cost per order ($/order) |
| `h` | Holding cost per unit per year ($/unit/year) |
| `C` | Unit purchase cost ($) |
| `r` | Annual carrying rate (% of unit cost) |

**Holding cost:** `h = C * r`. The rate `r` includes cost of capital, warehousing, insurance, obsolescence (typically 15-30%).

**Optimal order quantity:** `Q* = sqrt(2 * D * S / h)`

**Optimal order interval:** `T* = Q* / D` (in years; multiply by 365 or 52 for days/weeks)

**Optimal number of orders per year:** `N* = D / Q*`

**Total relevant cost at Q*:** `TLC* = sqrt(2 * D * S * h)`

**TLC for any Q:** `TLC(Q) = S * D / Q + h * Q / 2`

Note: TLC is flat near Q* -- deviating +/- 20% from Q* increases cost by only ~2%. This "robustness" is a key managerial insight.

### Multi-Item Joint Ordering

When multiple items share a common fixed ordering cost (same supplier, same truck):

**Optimal common cycle time:** `T* = sqrt(2 * S / SUM(h_i * D_i))`

**Item order quantities:** `Q_i = T* * D_i`

Where `S` = shared order cost, `h_i` = holding cost for item i, `D_i` = annual demand for item i.

### Quantity Discounts

**All-units discount:** Price per unit drops for ALL units when order >= breakpoint.

Process:
1. Compute EOQ at each price tier
2. If EOQ falls within its tier, it's feasible; compute TLC (including purchase cost)
3. For tiers where EOQ is below the breakpoint, evaluate TLC at the breakpoint quantity
4. Compare total annual cost = `C_j * D + S * D / Q + h_j * Q / 2` across all candidates
5. Lowest total cost wins

**Incremental discount:** Lower price applies only to units above the breakpoint. Compute marginal cost curve and optimize.

### Inventory Performance Metrics

| Metric | Formula |
|--------|---------|
| Average Cycle Inventory | `Q / 2` (in units) or `C * Q / 2` (in $) |
| Inventory Turns | `COGS / Average Inventory Value` |
| Days of Inventory (DOI) | `365 / Turns` |
| Inventory as % of Revenue | `Avg Inventory Value / Annual Revenue` |

## Process

### Entry Mode 1: Guided

Ask sequentially:

1. **Item(s)** -- single SKU or multiple items?
2. **Demand** -- annual demand in units (or derive from daily/weekly)?
3. **Costs** -- unit cost (C), order/setup cost (S), carrying rate (r) or holding cost (h)?
4. **Discounts** -- any quantity price breaks?
5. **Output mode** -- Excel / Python / Both / Teach?

### Entry Mode 2: Context Dump

User provides a case or problem. Extract D, S, C, h (or r), discount schedules. Confirm, then produce output.

### Entry Mode 3: Quick Draft

User says something like "EOQ, D=10000, S=150, C=25, r=20%." Parse and produce output directly.

## Excel Output Specification

### Tab 1: EOQ Calculator

| Section | Content |
|---------|---------|
| Inputs | D, S, C, r, h (blue font, yellow fill) |
| Results | Q*, T* (days/weeks/years), N* orders/year, TLC* |
| Cost Breakdown | Annual ordering cost, annual holding cost, annual purchase cost |
| Robustness | Table showing TLC at 0.5Q*, 0.8Q*, Q*, 1.2Q*, 1.5Q*, 2Q* with % increase vs optimal |

Formulas visible in a formula audit column or cell comments.

### Tab 2: Multi-Item Coordination

| Section | Content |
|---------|---------|
| Item Table | Item, D_i, C_i, h_i, Individual Q*_i, Individual TLC_i |
| Coordinated | Common T*, Q_i under coordination, Coordinated TLC |
| Comparison | Total cost individual vs coordinated, savings |

### Tab 3: Quantity Discounts

| Section | Content |
|---------|---------|
| Discount Schedule | Tier, Min Qty, Unit Price (input table, yellow fill) |
| Analysis | Tier, Feasible EOQ, Evaluation Qty, Annual Purchase, Annual Order, Annual Hold, Total Cost |
| Recommendation | Winning tier highlighted, annual savings vs base price |

### Tab 4: Assumptions

Key assumptions listed: constant demand rate, instantaneous replenishment, no stockouts allowed, single item (or independent items), fixed and known costs, no capacity constraints.

## Output

### Excel Mode
Deliver formatted .xlsx with all 4 tabs. Use Shortcut.ai API. IB formatting standards.

### Python Mode
Self-contained script with:
- `compute_eoq(D, S, C, r)` returning Q*, T*, N*, TLC*
- `quantity_discount(D, S, r, tiers)` returning optimal tier and quantity
- `multi_item_eoq(items, S)` returning coordinated T* and quantities
- Console summary + matplotlib cost curve (holding, ordering, total vs Q)

### Both Mode
Excel file + Python script.

### Teach Mode
Step-by-step walkthrough:
1. Frame the tradeoff (order cost vs holding cost)
2. Derive Q* intuitively (set marginal ordering cost = marginal holding cost)
3. Calculate with numbers
4. Show robustness (the flat cost curve near Q*)
5. Extend to discounts or multi-item if relevant
6. Interpret: what does this mean for purchasing operations?

## Anti-Patterns

1. **Forgetting to annualize.** D must be annual if h is annual. If demand is given weekly, multiply by 52. Period mismatch is the #1 calculation error.
2. **Using revenue instead of COGS for inventory turns.** Turns = COGS / Avg Inventory. Using revenue inflates turns and gives a false picture.
3. **Ignoring quantity discounts.** EOQ at base price may be dominated by a larger order at a discount. Always check discount breakpoints.
4. **Treating EOQ as exact.** The cost curve is flat near Q*. Round to practical units (pallets, truckloads). A 20% deviation costs only ~2% more.
5. **Double-counting holding cost.** If h already includes capital cost, don't add a separate financing charge. Define h = C * r clearly.
6. **Applying EOQ when demand is lumpy or seasonal.** EOQ assumes constant demand rate. For highly variable demand, use dynamic lot sizing (Wagner-Whitin) or MRP logic.
7. **Ignoring lead time in the EOQ context.** EOQ determines HOW MUCH to order. WHEN to order (reorder point) requires lead time and safety stock -- that's a separate calculation.
8. **Setting S = 0 to justify daily ordering.** Order cost includes receiving, inspection, PO processing, not just shipping. Underestimating S leads to excessive order frequency.
9. **Confusing cycle inventory with total inventory.** Cycle inventory = Q/2. Total inventory also includes safety stock, pipeline, and anticipation inventory.
10. **Not considering coordination across items.** Ordering each SKU independently when they share a supplier wastes the fixed cost. Use joint ordering when applicable.

## Related Skills

- `newsvendor-model` -- for single-period decisions under uncertainty
- `safety-stock-policy` -- for setting reorder points and safety buffers
