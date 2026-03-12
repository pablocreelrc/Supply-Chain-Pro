---
name: supply-chain-contracting
description: "Design and evaluate supply chain contracts — revenue sharing, buyback, quantity flexibility, VMI. Use when someone says: double marginalization, revenue sharing, buyback contract, quantity flexibility, vendor managed inventory, VMI, channel coordination, wholesale price contract, decentralized supply chain, contract design, supply chain coordination, retailer profit, supplier profit, channel profit, coordinating contract, transfer price, consignment, markdown money, return policy, risk sharing, incentive alignment, profit split, stocking quantity"
---

# Supply Chain Contracting

## Purpose

Analyze and design contracts between supply chain partners (supplier and retailer) that align incentives and eliminate or reduce double marginalization. Compare wholesale price, revenue sharing, buyback, and quantity flexibility contracts on stocking decisions, profits, and total channel performance.

## When to Use

- A retailer stocks less than the supply-chain-optimal quantity under wholesale pricing
- Supplier wants to increase retailer's order quantity without cutting wholesale price to cost
- Designing a new supplier-retailer agreement with risk-sharing provisions
- Evaluating whether a buyback or revenue sharing contract improves total channel profit
- Comparing VMI to traditional ordering
- Quantifying the "coordination gap" (how much profit the channel leaves on the table)
- Negotiating contract terms that both parties prefer to the status quo

## Foundation

### The Double Marginalization Problem

**Setup**: Supplier (cost c) sells to Retailer (wholesale price w) who sells to end customer (retail price p). Demand is uncertain.

| Decision Maker | Stocking Decision | Problem |
|----------------|-------------------|---------|
| Integrated channel | Stocks Q* where F(Q*) = (p-c)/(p) | Maximizes total profit |
| Decentralized retailer | Stocks Q_d where F(Q_d) = (p-w)/(p) | Under-stocks because w > c |

**Gap**: Q_d < Q* because the retailer faces a higher effective cost (w > c), leading to lower service level, lost sales, and reduced total channel profit.

### Contract Types

#### 1. Wholesale Price (Benchmark)
- Supplier charges w per unit; retailer keeps all revenue
- Retailer's critical ratio: (p - w) / p
- Does NOT coordinate the channel (unless w = c)

#### 2. Revenue Sharing
- Supplier charges reduced wholesale price w
- Retailer keeps fraction alpha of revenue, gives (1-alpha) to supplier
- **Coordination condition: w = c * alpha** (so w < c is possible)
- Retailer's critical ratio becomes: (alpha*p - w) / (alpha*p) = (p - c) / p (matches integrated)
- Retailer profit: alpha * [expected revenue] - w*Q
- Supplier profit: (1-alpha) * [expected revenue] + (w - c)*Q

#### 3. Buyback Contract
- Supplier charges w per unit upfront
- Supplier buys back unsold units at price b per unit (b < w)
- **Coordination condition: b = w - w*(p-w)/p** or equivalently the critical ratio matches
- Retailer's effective salvage = b (instead of 0 or v), so retailer orders more
- Retailer's critical ratio: (p - w) / (p - b)
- Set b so that (p - w)/(p - b) = (p - c)/p

#### 4. Quantity Flexibility
- Retailer commits to buying Q but can adjust within a range [Q*(1-delta), Q*(1+delta)]
- Supplier bears risk of downside adjustment
- Delta parameter controls risk sharing

#### 5. VMI (Vendor Managed Inventory)
- Supplier decides stocking quantity at retailer's location
- Supplier has better visibility and incentive alignment
- Often combined with consignment (supplier owns inventory until sold)

### Profit Formulas (Newsvendor Setting)

Expected sales: S(Q) = mu - L(Q) where L(Q) = expected lost sales

| Party | Wholesale Price | Revenue Sharing |
|-------|----------------|-----------------|
| Retailer | (p-w)*S(Q) - w*(Q - S(Q)) | alpha*p*S(Q) - w*Q |
| Supplier | (w-c)*Q | (1-alpha)*p*S(Q) + (w-c)*Q |
| Channel | (p-c)*S(Q) - c*(Q - S(Q)) | Same as integrated |

### Key Relationships

- Revenue sharing with alpha and buyback with appropriate b can yield identical outcomes
- Any coordinating contract must make the retailer's marginal incentive match the channel's
- Contract acceptability: both parties must earn >= their decentralized profit (individual rationality)

## Process

### Three Entry Modes

| Mode | User Provides | Skill Does |
|------|--------------|------------|
| **Guided** | "My supplier charges $10 wholesale, I sell at $20, demand is uncertain" | Asks for cost, demand distribution; calculates all contract types |
| **Context Dump** | c, w, p, demand distribution, salvage value | Computes optimal Q under each contract, compares profits |
| **Quick Draft** | "Compare contracts for a seasonal product" | Builds template with example parameters |

### Adaptive Questioning

| If User Provides... | Then Ask About... |
|---------------------|-------------------|
| p and w only | Supplier's unit cost c, salvage value v, demand distribution |
| Demand distribution | Is it discrete (scenarios) or continuous (normal, uniform)? |
| Revenue sharing request | What alpha range is acceptable? Any minimum wholesale price? |
| Buyback request | Is there a maximum buyback price the supplier will accept? |
| Multiple products | Same contract for all, or product-specific terms? |

## Excel Output Specification

### Tab 1: Decentralized Benchmark
- **Row 3-8**: Input parameters (c, w, p, v, demand distribution params) -- blue font, yellow fill
- **Row 10-15**: Integrated channel optimum: Q*, expected profit, expected sales, expected overstock
- **Row 17-22**: Decentralized retailer: Q_d, retailer profit, supplier profit, channel profit
- **Row 24-28**: Coordination gap: lost channel profit, lost sales, efficiency ratio (decentralized/integrated)

### Tab 2: Revenue Sharing
- Alpha input (yellow cell) with recommended coordinating value shown
- Coordinating wholesale price: w = c * alpha
- Retailer's optimal Q under revenue sharing
- Profit split: retailer, supplier, total
- Sensitivity table: alpha from 0.1 to 0.9, showing Q, retailer profit, supplier profit
- Highlight the alpha range where both parties prefer this to decentralized

### Tab 3: Buyback Contract
- Buyback price b input (yellow cell) with coordinating value shown
- Retailer's optimal Q under buyback
- Profit split: retailer, supplier (net of buyback payments), total
- Sensitivity table: b from 0 to w, showing Q, profits
- Expected buyback quantity and cost to supplier

### Tab 4: Contract Comparison
- Summary table: all contract types side by side
- Columns: Contract Type, Wholesale Price, Other Terms, Q ordered, Retailer Profit, Supplier Profit, Channel Profit, Efficiency %
- Bar chart comparing channel profit across contracts
- Recommendation box: which contract is best and why

### Tab 5: Assumptions
- Demand distribution and parameters
- Single-period assumption (newsvendor setting)
- Risk neutrality of both parties
- No information asymmetry caveats
- Implementation costs not modeled (monitoring, returns processing)

## Output

| Mode | Deliverable |
|------|------------|
| **Excel** | Formatted workbook with all 5 tabs, sensitivity tables, comparison charts |
| **Python** | Script computing optimal Q and profits under each contract using scipy |
| **Both** | Excel + Python with cross-validation |
| **Teach** | Walkthrough of double marginalization, then contract-by-contract derivation |

## Anti-Patterns

1. **Ignoring double marginalization** -- assuming wholesale price contract is "good enough" without quantifying the gap
2. **Setting revenue share alpha without checking coordination condition** -- alpha must satisfy w = c*alpha to coordinate
3. **Buyback price above wholesale price** -- b must be < w; otherwise supplier loses money on every returned unit
4. **Forgetting individual rationality** -- a coordinating contract both parties reject is useless; each must earn >= status quo
5. **Assuming contracts are costless to implement** -- buyback requires returns logistics; revenue sharing requires sales monitoring
6. **Applying single-period contracts to multi-period settings without adjustment** -- reputation and repeated game effects matter
7. **Ignoring salvage value in buyback analysis** -- if unsold units have salvage value v > 0, buyback economics change
8. **Treating VMI as automatically coordinating** -- VMI changes who decides, but incentives still need alignment
9. **Not checking if demand distribution matters** -- some results are distribution-free, others depend heavily on tail shape

## Related Skills

- `newsvendor-model` -- contracting builds directly on the newsvendor stocking decision
- `competitive-cost-analysis` -- understanding cost structures informs contract negotiation leverage
