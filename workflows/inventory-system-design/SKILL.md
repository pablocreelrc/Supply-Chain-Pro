---
name: inventory-system-design
description: "Use this skill when the user needs to design a complete inventory management system from order sizing through network configuration. Triggers: inventory system design, inventory management workflow, EOQ to network design, complete inventory analysis, inventory policy design, end to end inventory, inventory optimization workflow, how to set up inventory system, order quantity and safety stock and network, integrated inventory model, inventory strategy, inventory pipeline, multi-echelon inventory, centralized vs decentralized inventory, inventory pooling network, design my inventory system, set inventory parameters, reorder point and order quantity, inventory total cost optimization, warehouse inventory policy, distribution center inventory, SKU-level inventory policy, inventory consolidation analysis, inventory centralization, square root law inventory, risk pooling inventory, chain eoq safety stock network, inventory planning process, optimal inventory configuration, stocking policy design, full inventory model"
---

# Inventory System Design

## Purpose

Chain three analytical steps -- EOQ/cycle inventory optimization, safety stock and reorder point setting, and network design with inventory pooling -- into an integrated workflow that produces a complete, cost-minimized inventory system configuration.

## When to Use

- You need to set both order quantities AND safety stock levels for a product or portfolio
- You are evaluating centralized vs. decentralized inventory network configurations
- A network redesign requires understanding total inventory cost (cycle + safety + transport)
- You want to quantify the inventory pooling benefit of consolidating warehouses
- You need to present a complete inventory policy recommendation (Q, R, SS, network)
- You are designing inventory parameters for a new product or distribution channel
- You want to understand how order frequency, service level, and network structure interact

## Foundation

### Workflow Architecture

This skill chains three foundational analyses. Each step's output informs the next:

```
Step 1: EOQ & CYCLE INVENTORY
  Input: Annual demand, ordering cost, holding cost
  Output: Optimal order quantity Q*, cycle inventory, order frequency
         |
         v
Step 2: SAFETY STOCK & REORDER POINT
  Input: Demand variability, lead time, service level target
  Output: Safety stock SS, reorder point R, total inventory investment
         |
         v
Step 3: NETWORK DESIGN
  Input: Q* and SS from above, number/location of facilities
  Output: Centralized vs. decentralized comparison, optimal configuration
```

### Step 1: EOQ & Cycle Inventory

**Economic Order Quantity:**
```
Q* = sqrt(2 * D * S / H)
```

Where: `D` = annual demand (units), `S` = fixed cost per order ($), `H` = annual holding cost per unit ($ or = h * C where h = holding rate, C = unit cost).

**Cycle inventory** = Q*/2 (average on-hand from cycle stock).

**Key derived metrics:**

| Metric | Formula |
|--------|---------|
| Orders per year | D / Q* |
| Time between orders | Q* / D (in years) |
| Annual ordering cost | (D / Q*) * S |
| Annual holding cost | (Q* / 2) * H |
| Total cycle cost | Ordering + Holding (these are equal at Q*) |

**EOQ is robust:** A 20% error in Q changes total cost by only ~2%. This means rough estimates of S and H are usually good enough.

### Step 2: Safety Stock & Reorder Point

**Safety stock for continuous review (Q,R) system:**
```
SS = z * sigma_DL
sigma_DL = sigma_D * sqrt(L)     (if demand varies, lead time constant)
sigma_DL = D_avg * sigma_L       (if lead time varies, demand constant)
sigma_DL = sqrt(L * sigma_D^2 + D_avg^2 * sigma_L^2)   (both vary)
```

Where: `z` = safety factor from target service level (e.g., z=1.65 for 95% CSL), `sigma_D` = std dev of demand per period, `L` = lead time in periods, `sigma_L` = std dev of lead time.

**Reorder point:**
```
R = D_avg * L + SS
```

**Periodic review (T,S) system:**
```
SS = z * sigma_D * sqrt(T + L)
Order-up-to level S = D_avg * (T + L) + SS
```

Where `T` = review interval.

**Service level definitions:**

| Metric | Definition | z for 95% |
|--------|-----------|-----------|
| Cycle Service Level (CSL) | P(no stockout per cycle) | 1.645 |
| Fill Rate (FR) | Fraction of demand filled from stock | Requires ESC calculation |

### Step 3: Network Design & Inventory Pooling

**Square Root Law for safety stock pooling:**
```
SS_centralized = SS_per_location * sqrt(n)     (vs. n * SS_per_location for n locations)
SS_savings = SS_per_location * (n - sqrt(n))
```

This assumes: identical locations, independent demand, same service level target.

**Centralized vs. Decentralized Trade-off:**

| Factor | Centralized (fewer locations) | Decentralized (more locations) |
|--------|------------------------------|-------------------------------|
| Safety stock | Lower (pooling effect) | Higher (no pooling) |
| Cycle stock | Same total (EOQ unchanged) | Same total |
| Inbound transport | Lower (fewer destinations) | Higher |
| Outbound transport | Higher (farther from customers) | Lower (closer to customers) |
| Lead time to customer | Longer | Shorter |
| Facility costs | Lower (fewer facilities) | Higher |
| Service responsiveness | Slower | Faster |

**Total cost comparison:**
```
Total Cost = Inventory Holding + Ordering + Inbound Transport + Outbound Transport + Facility Fixed Costs
```

The optimal network minimizes total cost subject to service level constraints.

## Process

### Entry Mode 1: Guided

Ask sequentially:

1. **Product(s)** -- single SKU or portfolio? Annual demand per SKU?
2. **Cost parameters** -- unit cost, ordering/setup cost, holding rate?
3. **Demand variability** -- standard deviation of demand per period? Period length?
4. **Lead time** -- average and variability?
5. **Service level target** -- CSL or fill rate? What percentage?
6. **Network** -- how many current locations? Considering consolidation or expansion?
7. **Transport costs** -- inbound and outbound per unit or per shipment?
8. **Output mode** -- Excel / Python / Both / Teach?

### Entry Mode 2: Context Dump

User provides a case with demand data, cost structure, and network description. Extract all parameters, map to the three steps, confirm interpretation, then produce output.

### Entry Mode 3: Quick Draft

User provides inline data like "Demand 10K/year, sigma 500/month, cost $50/unit, order cost $200, holding 25%, lead time 2 weeks, 95% CSL, currently 4 warehouses." Parse and produce output.

### Adaptive Questioning

| Input | Required For | Default If Missing |
|-------|-------------|-------------------|
| Annual demand (D) | All tabs | Ask -- no default |
| Unit cost (C) | EOQ, Safety Stock | Ask -- no default |
| Ordering/setup cost (S) | EOQ | Ask -- no default |
| Holding cost rate (h) | EOQ, Safety Stock, Network | 25% of unit cost per year |
| Demand std dev (sigma_D) | Safety Stock, Network | Ask -- no default |
| Demand period (for sigma_D) | Safety Stock | Monthly |
| Lead time (L) | Safety Stock | Ask -- no default |
| Lead time variability (sigma_L) | Safety Stock | 0 (constant lead time) |
| Service level target | Safety Stock | 95% CSL |
| Number of current locations | Network | 1 (skip network comparison) |
| Outbound transport cost/unit | Network | Ask if doing network comparison |
| Facility fixed cost | Network | Ask if doing network comparison |

## Excel Output Specification

### Tab 1: EOQ Analysis

| Column | Header | Format | Content |
|--------|--------|--------|---------|
| A | Parameter | Text | Row labels |
| B | Value | Various | Input or formula |
| C | Unit | Text | Units, $, orders/yr, days |

Rows: Annual Demand (D), Unit Cost (C), Ordering Cost (S), Holding Rate (h), Holding Cost (H = h*C), EOQ (Q*), Cycle Inventory (Q*/2), Orders per Year, Days Between Orders, Annual Ordering Cost, Annual Holding Cost, Total Cycle Cost.

Sensitivity section below: Total Cost vs. Q (plot data for Q from 0.5*Q* to 2*Q* in 10 increments). Show that cost curve is flat near Q*.

### Tab 2: Safety Stock & ROP

| Column | Header | Format | Content |
|--------|--------|--------|---------|
| A | Parameter | Text | Row labels |
| B | Value | Various | Input or formula |
| C | Unit | Text | Units, days, $ |

Section 1 -- Inputs: sigma_D, demand period, lead time (L), sigma_L, target CSL.

Section 2 -- Calculations: sigma_DL, z-score, Safety Stock (SS), Reorder Point (R), Average Inventory (Q*/2 + SS), Average Inventory Value.

Section 3 -- Service Level Sensitivity:

| Column | Header | Format | Content |
|--------|--------|--------|---------|
| A | CSL Target | 0.0% | 80% to 99.9% |
| B | z-score | 0.00 | =NORM.S.INV(CSL) |
| C | Safety Stock | #,##0 | =z * sigma_DL |
| D | SS Investment ($) | $#,##0 | =C_n * Unit Cost (green font) |
| E | Total Inventory ($) | $#,##0 | =(Q*/2 + C_n) * Unit Cost |

### Tab 3: Network Options

| Column | Header | Format | Content |
|--------|--------|--------|---------|
| A | Metric | Text | Row labels |
| B | 1 Location | $#,##0 | Centralized scenario |
| C | 2 Locations | $#,##0 | Formulas using sqrt law |
| D | 4 Locations | $#,##0 | Formulas |
| E | Current (n) | $#,##0 | User's current state |

Rows: Safety Stock (units), Safety Stock ($), Cycle Stock ($), Total Inventory ($), Inbound Transport, Outbound Transport, Facility Fixed Costs, TOTAL ANNUAL COST.

Highlight minimum-cost column with conditional formatting.

### Tab 4: Total Cost Comparison

| Column | Header | Format | Content |
|--------|--------|--------|---------|
| A | Cost Component | Text | Ordering, Holding (Cycle), Holding (Safety), Inbound Transport, Outbound Transport, Facility, TOTAL |
| B | Current System ($) | $#,##0 | Baseline total costs |
| C | Optimized System ($) | $#,##0 | With Q*, SS*, best network |
| D | Savings ($) | $#,##0;($#,##0) | =B_n - C_n |
| E | Savings (%) | 0.0% | =D_n / B_n |

Grand total row with double border. Savings summary below.

### Tab 5: Executive Summary

| Row | Content |
|-----|---------|
| Order Policy | "Order Q* = X units when inventory hits R = Y units" |
| Safety Stock | SS = Z units providing W% cycle service level |
| Network Recommendation | Optimal number of locations with rationale |
| Total Annual Cost | Current vs. optimized, with dollar and percentage savings |
| Key Trade-offs | What you gain and give up with the recommendation |
| Implementation Notes | Transition considerations, phasing |

### Tab 6: Assumptions

| Cell | Label | Default Value | Format |
|------|-------|--------------|--------|
| B2 | Annual Demand (units) | (user input) | #,##0 |
| B3 | Unit Cost ($) | (user input) | $#,##0.00 |
| B4 | Ordering Cost ($) | (user input) | $#,##0 |
| B5 | Holding Rate (%) | 25% | 0.0% |
| B6 | Demand Std Dev (per period) | (user input) | #,##0 |
| B7 | Demand Period | Monthly | Text |
| B8 | Lead Time (periods) | (user input) | 0.0 |
| B9 | Lead Time Std Dev | 0 | 0.0 |
| B10 | Target CSL | 95% | 0.0% |
| B11 | Number of Current Locations | (user input) | #,##0 |
| B12 | Outbound Transport ($/unit) | (user input) | $#,##0.00 |
| B13 | Facility Fixed Cost ($/yr) | (user input) | $#,##0 |

All cells blue font, yellow fill. Named ranges: `AnnualDemand` -> B2, `UnitCost` -> B3, etc.

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
- `compute_eoq(D, S, H)` returning Q*, cycle inventory, costs
- `compute_safety_stock(sigma_D, L, sigma_L, csl)` returning SS, ROP, z
- `network_comparison(D, sigma_D, L, csl, H, n_locations, transport_costs, facility_costs)` returning cost by configuration
- `design_inventory_system(params_dict)` chaining all three steps
- Console summary and matplotlib charts (EOQ cost curve, SS vs. CSL, network cost comparison)

### Both Mode
Deliver Excel file + Python script.

### Teach Mode
Step-by-step walkthrough:
1. Derive EOQ from the total cost equation; explain why ordering and holding costs balance
2. Calculate Q* and show the cost curve is flat near optimum (robustness)
3. Compute demand-during-lead-time variability; explain the sqrt(L) factor
4. Set safety stock and reorder point; interpret what R means operationally
5. Apply the square root law to compare centralized vs. decentralized networks
6. Build total cost comparison across all cost components
7. Synthesize into a policy recommendation: "Order Q when you hit R, using N warehouses"

## Anti-Patterns

| # | Mistake | Why It Is Wrong | Correct Approach |
|---|---------|----------------|-----------------|
| 1 | Setting safety stock without specifying the service level target | Safety stock is meaningless without knowing what probability of stockout it provides; different stakeholders assume different targets | Always tie SS to an explicit CSL or fill rate target; document it |
| 2 | Using EOQ without checking the holding cost rate | H = h * C; if you use h = 25% but unit cost is $500, H = $125/unit/year which may be unrealistic | Validate that H reflects actual capital cost, storage, obsolescence, insurance, and shrinkage |
| 3 | Applying the square root law when demands are correlated | The sqrt(n) pooling formula assumes independent demand across locations; correlated demand reduces the benefit | Estimate demand correlation; use sigma_pooled = sqrt(sum(sigma_i^2) + 2*sum(rho_ij*sigma_i*sigma_j)) |
| 4 | Ignoring outbound transport cost when centralizing | Fewer warehouses means each shipment travels farther to the customer; transport cost may exceed inventory savings | Always model outbound transport as a function of number of locations and average distance |
| 5 | Mixing demand period and lead time units | If sigma_D is per month but lead time is in weeks, sigma_DL will be wrong by a large factor | Convert everything to the same time unit before calculating sigma_DL |
| 6 | Optimizing Q and SS independently of network design | Q* and SS depend on demand volume per location, which changes when you add or remove warehouses | Run the full pipeline: set network first (or test options), then compute Q* and SS per location |
| 7 | Using a single service level for all SKUs | A 99% CSL on a $2 widget costs far less than 99% on a $5,000 component; one-size-fits-all is wasteful | Segment SKUs (ABC analysis) and set differentiated service levels |
| 8 | Ignoring lead time variability | If lead time varies, sigma_DL includes a D_avg * sigma_L term that can dominate; ignoring it understates required safety stock | Always ask about lead time variability; even 1-2 days of sigma_L matters for fast-moving items |
| 9 | Treating EOQ as a hard constraint | EOQ is optimal for the cost model, but practical constraints (truck capacity, minimum order, shelf life) may override it | Adjust Q* to the nearest practical quantity (full truckload, case pack) and verify cost impact is small |
| 10 | Presenting inventory costs without total system cost | Showing only holding cost reduction from centralization ignores the transport, facility, and service impacts | Always present the full cost stack: ordering + holding (cycle + safety) + transport + facility |

## Related Skills

- **EOQ & Cycle Inventory** (`foundations/eoq-cycle-inventory/`) -- Step 1 of this workflow; optimal order quantity under known demand
- **Safety Stock Policy** (`foundations/safety-stock-policy/`) -- Step 2; setting safety stock and reorder points under demand/lead time uncertainty
- **Network Design** (`advanced/network-design/`) -- Step 3; facility location and inventory pooling across the distribution network
