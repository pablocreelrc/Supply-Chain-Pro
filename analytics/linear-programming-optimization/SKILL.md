---
name: linear-programming-optimization
description: "Build and solve LP models for supply chain resource allocation — production planning, transportation, distribution, blending. Use when someone says: optimize, linear program, LP, solver, minimize cost, maximize profit, resource allocation, production planning, transportation problem, assignment problem, constraint, decision variable, objective function, shadow price, sensitivity analysis, reduced cost, binding constraint, feasible region, simplex, optimal solution, capacity allocation, blending problem"
---

# Linear Programming Optimization

## Purpose

Formulate, solve, and interpret linear programming models for supply chain decisions. Covers model setup (decision variables, objective function, constraints), solving via Excel Solver or Python (PuLP/scipy), and extracting managerial insight from shadow prices and sensitivity analysis.

## When to Use

- Allocating limited resources (machines, labor, materials) across products or facilities
- Minimizing transportation or distribution costs across a network
- Production planning with capacity, demand, and inventory constraints
- Blending or mixing problems (ingredient optimization)
- Any decision requiring "best allocation" under linear constraints
- When you need shadow prices to value additional capacity
- Assignment of jobs to machines, workers to shifts, products to plants

## Foundation

### Model Structure

Every LP has three components:

1. **Decision Variables** (x_j): What you control (units to produce, ship, assign)
2. **Objective Function**: Minimize or maximize a linear expression
   - Min Z = c_1*x_1 + c_2*x_2 + ... + c_n*x_n
3. **Constraints**: Linear inequalities or equalities
   - a_11*x_1 + a_12*x_2 + ... <= b_1 (resource limits)
   - x_j >= 0 (non-negativity)

### Key Formulas

| Concept | Formula | Interpretation |
|---------|---------|----------------|
| Objective Function | Z = SUM(c_j * x_j) | Total cost or profit to optimize |
| Resource Constraint | SUM(a_ij * x_j) <= b_i | Cannot exceed available resource i |
| Demand Constraint | x_j >= d_j | Must meet minimum demand |
| Shadow Price | dZ*/db_i | Value of one more unit of resource i |
| Reduced Cost | c_j - z_j | How much coefficient must improve before variable enters basis |
| Allowable Increase/Decrease | Range on b_i or c_j | Range over which shadow price or basis remains valid |

### Transportation Problem

Special LP structure:
- Decision variables: x_ij = units shipped from source i to destination j
- Minimize: SUM(c_ij * x_ij) over all i,j
- Supply constraints: SUM_j(x_ij) <= S_i for each source
- Demand constraints: SUM_i(x_ij) >= D_j for each destination

### Sensitivity Analysis Interpretation

| Report Element | Question Answered |
|----------------|-------------------|
| Shadow Price > 0 | Binding constraint; would you pay for more? |
| Shadow Price = 0 | Non-binding; slack exists |
| Allowable Increase on RHS | How much more resource before shadow price changes |
| Reduced Cost | How much better must a variable's cost be to use it |
| Allowable range on coefficient | Stability of current optimal solution |

## Process

### Three Entry Modes

| Mode | User Provides | Skill Does |
|------|--------------|------------|
| **Guided** | Problem description in words | Asks clarifying questions, formulates model, solves, interprets |
| **Context Dump** | Parameters, costs, capacities, demands | Formulates and solves directly |
| **Quick Draft** | "Optimize production across 3 plants" | Builds template with placeholder data for user to populate |

### Adaptive Questioning

| If User Provides... | Then Ask About... |
|---------------------|-------------------|
| Products and resources | Unit resource consumption, resource availability |
| Cost data only | Demand requirements, capacity limits |
| Network (sources/destinations) | Supply at each source, demand at each destination, unit shipping costs |
| Objective (min cost) | Are there minimum production or service level constraints? |
| All parameters | Confirm: any integer requirements? (changes to ILP) |

### Solution Steps

1. Define decision variables with clear notation
2. Write objective function
3. List all constraints (resource, demand, non-negativity, logical)
4. Solve using Solver or PuLP
5. Report optimal values, total objective, binding constraints
6. Run sensitivity analysis and interpret shadow prices
7. Provide managerial recommendations

## Excel Output Specification

### Tab 1: Model Setup
- **A1**: "Linear Programming Model" (bold, navy header)
- **Section 1** (Row 3): Decision Variables table — variable name, description, lower bound, upper bound
- **Section 2** (Row 12+): Objective Function — coefficients per variable, formula for Z
- **Section 3** (Row 20+): Constraints table — constraint name, LHS formula, sign (<=, >=, =), RHS value, slack/surplus
- All input cells: blue font, yellow fill
- Formula cells: black font, no fill
- Solver target cell and changing cells clearly labeled

### Tab 2: Solver Results
- Optimal decision variable values (highlighted green if > 0)
- Optimal objective function value (double-border box)
- Constraint status table: constraint name, LHS value, RHS value, slack, binding (Yes/No)
- Summary box: "Total Cost = $X" or "Total Profit = $X"

### Tab 3: Sensitivity Analysis
- **Decision Variable Report**: variable, final value, reduced cost, objective coefficient, allowable increase, allowable decrease
- **Constraint Report**: constraint, final value, shadow price, RHS, allowable increase, allowable decrease
- Interpretation column in plain English for each shadow price
- Highlight: binding constraints in bold; shadow prices > 0 flagged

### Tab 4: Assumptions
- Linearity assumption and any real-world caveats
- Data sources for costs, capacities, demands
- What the model does NOT capture (integer requirements, nonlinear costs, uncertainty)
- Sensitivity ranges that are particularly tight (flag risks)

## Output

Based on the user's selected mode:

| Mode | Deliverable |
|------|------------|
| **Excel** | Formatted workbook with all 4 tabs, Solver configured and ready to run |
| **Python** | PuLP or scipy.optimize.linprog script with model, solution, and sensitivity output |
| **Both** | Excel workbook + Python script that replicates and validates |
| **Teach** | Step-by-step walkthrough of formulation, solving, and interpretation with the user's own data |

## Anti-Patterns

1. **Forgetting non-negativity constraints** -- decision variables must be >= 0 unless explicitly allowed negative
2. **Misreading shadow prices** -- shadow price is marginal value of relaxing a constraint by one unit, valid only within allowable range
3. **Ignoring sensitivity ranges** -- recommending "buy more capacity" without checking the allowable increase
4. **Using LP when integers are required** -- if variables must be whole units (trucks, workers), need ILP not LP
5. **Confusing <= and >= constraints** -- supply constraints limit what you CAN ship; demand constraints set what you MUST deliver
6. **Not checking feasibility** -- an infeasible model has contradictory constraints; always verify before interpreting
7. **Over-trusting the model** -- LP assumes certainty, linearity, divisibility; real problems may violate these
8. **Mixing up reduced cost and shadow price** -- reduced cost applies to variables; shadow price applies to constraints
9. **Not scaling units consistently** -- mixing thousands and units causes numerical issues in Solver

## Related Skills

- `aggregate-planning` -- LP is the core engine for optimal aggregate plans
- `network-design` -- facility location and distribution problems often solved via LP/ILP
