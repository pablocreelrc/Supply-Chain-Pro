---
name: flexibility-demand-pooling
description: "Analyze dedicated vs flexible capacity and demand pooling benefits — chaining, correlation effects, safety stock reduction. Use when someone says: flexible capacity, dedicated capacity, demand pooling, risk pooling, chaining, partial flexibility, full flexibility, correlation, capacity investment, service level, plant flexibility, product flexibility, variance reduction, portfolio effect, diversification, square root law, pooled demand, flexible manufacturing, resource substitution, capacity strategy, hedge demand uncertainty"
---

# Flexibility & Demand Pooling

## Purpose

Quantify the value of flexible capacity over dedicated capacity. Analyze how pooling demand across products or regions reduces total variability, lowers required capacity, and improves service levels. Evaluate full flexibility, partial flexibility (chaining), and the role of demand correlation.

## When to Use

- Deciding whether to invest in flexible vs dedicated production lines
- Evaluating whether to consolidate warehouses or distribution centers
- Quantifying safety stock reduction from pooling demand across locations
- Assessing the impact of demand correlation on pooling benefits
- Designing chaining strategies (partial flexibility) that capture most pooling value
- Comparing capacity investment levels under different flexibility configurations
- Setting service level targets when flexibility is available

## Foundation

### Demand Pooling Formula

For two independent demands A and B:
- Pooled mean: mu_pooled = mu_A + mu_B
- Pooled std dev: sigma_pooled = sqrt(sigma_A^2 + sigma_B^2)

For correlated demands:
- **sigma(A+B) = sqrt(sigma_A^2 + sigma_B^2 + 2*rho*sigma_A*sigma_B)**

Where rho = correlation coefficient between A and B.

### Key Results

| Scenario | Pooled Std Dev | Variance Reduction |
|----------|---------------|-------------------|
| rho = -1 (perfect negative) | abs(sigma_A - sigma_B) | Maximum pooling benefit |
| rho = 0 (independent) | sqrt(sigma_A^2 + sigma_B^2) | Standard pooling benefit |
| rho = +1 (perfect positive) | sigma_A + sigma_B | Zero pooling benefit |

### N-Product Generalization

For N identical products each with mean mu and std dev sigma:
- Dedicated total safety stock: N * z * sigma
- Pooled safety stock: z * sigma * sqrt(N) (if independent)
- **Reduction factor: 1 - 1/sqrt(N)**
- With 4 products: 50% reduction; with 9 products: 67% reduction

### Capacity Investment Model

| Configuration | Required Capacity (per product) | Total Capacity |
|--------------|-------------------------------|----------------|
| Dedicated | mu_i + z * sigma_i | SUM(mu_i + z * sigma_i) |
| Fully Flexible | N/A | SUM(mu_i) + z * sigma_pooled |
| Savings | -- | z * [SUM(sigma_i) - sigma_pooled] |

### Chaining (Partial Flexibility)

- Full flexibility: every plant can make every product (expensive)
- Chaining: each plant can make 2 products, arranged in a chain/ring
- **Key insight**: A chain of N plants with 2-product flexibility captures ~95% of the benefit of full flexibility
- Chain structure: Plant 1 makes Products {1,2}, Plant 2 makes {2,3}, ..., Plant N makes {N,1}
- Avoid "short cycles" -- don't create disconnected sub-chains

### Value of Flexibility

Value of Flexibility = Profit(flexible) - Profit(dedicated)

Components:
- Reduced capacity investment (less total capacity needed)
- Higher expected sales (can shift production to where demand is)
- Lower lost sales / higher service level at same capacity
- Cost: flexible equipment premium, training, changeover costs

### When Flexibility Helps Most

- High service level targets (z >= 2)
- High demand uncertainty (high CV = sigma/mu)
- Low or negative demand correlation
- Expensive capacity (high cost per unit of capacity)
- Moderate number of products (diminishing returns beyond ~5-8)

## Process

### Three Entry Modes

| Mode | User Provides | Skill Does |
|------|--------------|------------|
| **Guided** | "Should we use flexible or dedicated lines?" | Asks for demand parameters, costs, service targets; builds full comparison |
| **Context Dump** | Demand means, std devs, correlations, capacity costs | Calculates pooling effect, builds comparison, recommends |
| **Quick Draft** | "Compare flexibility for 4-product plant" | Template with example data, ready to customize |

### Adaptive Questioning

| If User Provides... | Then Ask About... |
|---------------------|-------------------|
| Demand means only | Standard deviations, correlations, target service level |
| Two products | Are there more products to include? Capacity cost difference? |
| Full flexibility request | Have you considered chaining? What's the flexible equipment premium? |
| Correlation data | Is correlation stable or seasonal? |
| Service level target | Is this fill rate or cycle service level? |

## Excel Output Specification

### Tab 1: Dedicated vs Flexible Comparison
- **Row 3-10**: Product demand parameters (mu, sigma per product) -- blue font, yellow fill for inputs
- **Row 12-18**: Dedicated configuration -- capacity per product, total capacity, expected sales, expected lost sales
- **Row 20-26**: Flexible configuration -- pooled sigma calculation, total capacity needed, expected sales
- **Row 28-32**: Comparison summary -- capacity savings, service level improvement, value of flexibility
- Side-by-side bar chart: Dedicated vs Flexible capacity and profit

### Tab 2: Pooling Effect Calculator
- Correlation input matrix (rho values between all product pairs)
- Dedicated total sigma vs pooled sigma at each correlation level
- Sensitivity table: pooling benefit as rho varies from -1 to +1 (step 0.25)
- Line chart: sigma_pooled vs correlation
- Reduction percentage highlighted

### Tab 3: Chaining Analysis
- Plant-product assignment matrix (binary: which plant makes which product)
- Full flexibility assignment vs chain assignment vs dedicated
- Expected profit under each configuration
- Percentage of full-flexibility benefit captured by chain
- Visual diagram of chain structure (text-based)

### Tab 4: Assumptions
- Demand distribution assumptions (normal, stationary)
- Correlation estimation method
- Capacity cost assumptions (dedicated vs flexible premium)
- Changeover costs and times (if applicable)
- Limitations: assumes linear costs, no learning effects, single period

## Output

| Mode | Deliverable |
|------|------------|
| **Excel** | Formatted workbook with all 4 tabs, charts, sensitivity tables |
| **Python** | NumPy/SciPy script with pooling calculations, simulation of flexible vs dedicated |
| **Both** | Excel workbook + Python validation script |
| **Teach** | Step-by-step derivation of pooling formula, worked example, intuition building |

## Anti-Patterns

1. **Assuming independence when demands are correlated** -- positive correlation drastically reduces pooling benefit
2. **Ignoring the cost of flexibility** -- flexible equipment costs more; must net out the premium
3. **Full flexibility when chaining suffices** -- chaining with 2 products per plant captures ~95% of the benefit at far lower cost
4. **Creating short cycles in chains** -- a chain of 2 is just a pair; must connect all products in one ring
5. **Pooling with rho near +1** -- if demands move together, pooling provides almost no variance reduction
6. **Forgetting diminishing returns** -- going from 1 to 2 products per plant is huge; 5 to 6 is marginal
7. **Applying pooling to mean, not just variance** -- pooling does not change total expected demand, only its variability
8. **Ignoring changeover costs** -- flexibility is worthless if switching between products takes too long
9. **Using pooling formula for non-normal demands** -- the sqrt formula assumes normality; heavy-tailed demands need simulation

## Related Skills

- `newsvendor-model` -- flexible capacity decisions build on newsvendor stocking logic
- `aggregate-planning` -- flexibility enables better aggregate plans across products
