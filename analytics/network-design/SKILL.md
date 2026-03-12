---
name: network-design
description: "Design supply chain networks — facility location, gravity model, centralization analysis, distribution strategies. Use when someone says: facility location, gravity model, center of gravity, warehouse location, distribution network, centralization, decentralization, network design, plant location, DC location, distribution center, offshoring, nearshoring, reshoring, total landed cost, network optimization, hub and spoke, direct shipping, milk run, cross-dock, number of warehouses, location decision, fixed cost, transportation cost, service level tradeoff"
---

# Network Design

## Purpose

Make strategic facility location and distribution network decisions. Apply the gravity model for single-facility location, evaluate centralization vs decentralization tradeoffs, compare distribution network configurations, and analyze total cost of offshoring. These are long-horizon decisions (5-10 years) with high capital commitment.

## When to Use

- Deciding where to locate a new warehouse, plant, or distribution center
- Evaluating whether to consolidate multiple facilities into fewer locations
- Choosing a distribution network structure (direct ship, hub-and-spoke, cross-dock, etc.)
- Analyzing offshoring vs nearshoring vs domestic production
- Quantifying the tradeoff between transportation cost and facility cost
- Using decision trees to handle demand uncertainty in location decisions
- Determining the optimal number of warehouses in a network

## Foundation

### Gravity Model

Finds the location (X*, Y*) that minimizes weighted transportation cost:

**X* = SUM(d_i * x_i) / SUM(d_i)**
**Y* = SUM(d_i * y_i) / SUM(d_i)**

Where:
- (x_i, y_i) = coordinates of demand point i
- d_i = demand (or weight: demand * transport rate) at point i

Iterative refinement (Weiszfeld's algorithm) for distance-weighted version:
- w_i = d_i / dist(current_center, point_i)
- X* = SUM(w_i * x_i) / SUM(w_i), same for Y*
- Repeat until convergence

### Distribution Network Configurations (6 Types)

| # | Configuration | Description | Best When |
|---|--------------|-------------|-----------|
| 1 | **Direct shipping** | Manufacturer ships direct to customer | High-value, low-volume, custom products |
| 2 | **Direct with milk runs** | Truck visits multiple customers per trip | Multiple nearby customers, partial loads |
| 3 | **Distributor storage with delivery** | DC holds inventory, delivers to customer | Medium-value products, moderate demand |
| 4 | **Distributor storage with pickup** | DC holds inventory, customer picks up | Cost-sensitive customers willing to travel |
| 5 | **Manufacturer storage with direct ship** | Manufacturer holds all inventory, ships direct | High variety, low demand per SKU (long tail) |
| 6 | **Retail storage with pickup** | Local stores hold inventory | Immediate availability critical, high-demand items |

### Centralization vs Decentralization Tradeoffs

| Factor | Centralization Favors | Decentralization Favors |
|--------|----------------------|------------------------|
| Inventory cost | Lower (pooling effect: sigma * sqrt(n) vs sigma * n) | Higher |
| Transportation cost | Higher (longer distances to customers) | Lower |
| Facility cost | Lower (fewer facilities, economies of scale) | Higher |
| Response time | Slower | Faster |
| Service level | Lower for same inventory | Higher (closer to demand) |
| Product variety | Better for slow-movers | Better for fast-movers |

### Optimal Number of Warehouses

As number of warehouses (n) increases:
- **Facility costs**: Increase (roughly linearly)
- **Inbound transport**: Increase (more destinations for inbound)
- **Outbound transport**: Decrease (closer to customers)
- **Inventory costs**: Increase (sqrt(n) effect on safety stock)
- **Total cost**: U-shaped curve with minimum at n*

### Decision Trees for Location Under Uncertainty

Structure:
1. Decision node: Location options (A, B, C)
2. Chance nodes: Demand scenarios (High, Medium, Low) with probabilities
3. Terminal nodes: NPV or annual profit for each location-scenario pair
4. Decision rule: Choose location with highest Expected Monetary Value (EMV)

EMV = SUM(probability_i * payoff_i) for each scenario

### Total Cost of Offshoring

Beyond unit production cost, include:
- Transportation and logistics costs
- Inventory costs (longer pipelines = more inventory)
- Tariffs and duties
- Quality costs (defects, rework, returns)
- Management and travel overhead
- Currency risk and hedging costs
- Intellectual property risk
- Lead time variability and safety stock impact
- **Total landed cost = all of the above combined**

## Process

### Three Entry Modes

| Mode | User Provides | Skill Does |
|------|--------------|------------|
| **Guided** | "Where should we put our new warehouse?" | Asks for demand locations, volumes, cost data; runs gravity model and alternatives |
| **Context Dump** | Coordinates, demand volumes, facility costs, transport rates | Runs gravity model, builds cost comparison, recommends |
| **Quick Draft** | "Evaluate centralizing our 4 DCs into 2" | Template with consolidation analysis framework |

### Adaptive Questioning

| If User Provides... | Then Ask About... |
|---------------------|-------------------|
| Customer locations only | Demand volumes per location, transport cost per unit-mile |
| Candidate facility locations | Fixed costs per facility, capacity limits, labor costs |
| "Should we offshore?" | Current domestic costs, offshore unit cost, transport, lead time, tariffs |
| Demand uncertainty | Scenarios with probabilities for decision tree analysis |
| Number of warehouses question | Current network costs by category, service level requirements |

## Excel Output Specification

### Tab 1: Gravity Model
- **Row 3-15**: Input table -- Location name, X coordinate, Y coordinate, Demand volume, Transport rate (blue font, yellow fill)
- **Row 17-20**: Calculated weights (d_i * rate_i)
- **Row 22-24**: Center of gravity result: X*, Y*, with formula shown
- Scatter plot: demand points (sized by volume) with gravity center marked
- If iterative: show convergence table (iteration, X, Y, total weighted distance)

### Tab 2: Network Cost Comparison
- Columns: Network configuration options (e.g., 1 DC, 2 DCs, 3 DCs, or different locations)
- Rows: Cost categories -- facility fixed cost, inbound transport, outbound transport, inventory holding, labor
- Total cost per configuration
- Bar chart: stacked cost by category for each configuration
- Highlight minimum total cost option

### Tab 3: Decision Tree
- Scenario table: scenario name, probability, demand level
- Payoff matrix: rows = location options, columns = scenarios, cells = NPV or annual profit
- EMV calculation for each location
- Sensitivity: at what probability does the decision change?
- Tree diagram (text-based or structured table)

### Tab 4: Centralization Analysis
- Current (decentralized) costs: inventory by location, transport, facility
- Proposed (centralized) costs: pooled inventory, new transport, facility
- Safety stock comparison: sqrt(n) reduction calculation
- Net savings / (cost) with breakeven analysis
- Service level impact assessment (response time by customer zone)

### Tab 5: Assumptions
- Coordinate system and distance calculation method (Euclidean, Manhattan, road)
- Demand stationarity and forecast confidence
- Transport cost linearity
- Fixed vs variable cost split for facilities
- Planning horizon for NPV calculations
- Factors not modeled (zoning, labor availability, taxes, climate risk)

## Output

| Mode | Deliverable |
|------|------------|
| **Excel** | Formatted workbook with all 5 tabs, gravity model map, cost charts, decision tree |
| **Python** | Script with gravity model (scipy), cost optimization, scenario analysis |
| **Both** | Excel + Python with matching results and visualizations |
| **Teach** | Step-by-step: gravity model by hand, then cost comparison framework, then decision tree |

## Anti-Patterns

1. **Using gravity model without iterating** -- simple weighted average ignores distance; Weiszfeld iteration is more accurate
2. **Ignoring fixed costs in location decisions** -- a "central" location with expensive real estate may lose to a cheaper peripheral one
3. **Evaluating offshoring on unit cost alone** -- total landed cost includes transport, inventory, quality, lead time, risk
4. **Centralizing everything** -- fast-moving, bulky, low-value items should stay decentralized (transport dominates)
5. **Ignoring service level in consolidation** -- fewer DCs = longer delivery times; must quantify the customer impact
6. **Static analysis for a dynamic decision** -- demand patterns shift; build in flexibility or phase decisions
7. **Forgetting inventory cost scales with sqrt(n)** -- going from 4 to 1 warehouse cuts safety stock by 50%, not 75%
8. **Not discounting in multi-year decisions** -- facility decisions span 5-10 years; use NPV, not simple payback
9. **Treating all products the same** -- segment by volume, value, and variability; different products may need different networks

## Related Skills

- `safety-stock-policy` -- centralization reduces safety stock via pooling; this skill quantifies the inventory impact
- `linear-programming-optimization` -- large network design problems are solved as mixed-integer LPs
