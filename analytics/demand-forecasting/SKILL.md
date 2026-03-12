---
name: demand-forecasting
description: "Build and evaluate demand forecasts — moving average, exponential smoothing, trend, seasonality. Use when someone says: forecast, demand forecast, moving average, exponential smoothing, Holt, Winters, seasonal forecast, trend analysis, MAD, MAPE, MSE, tracking signal, smoothing constant, alpha, beta, gamma, forecast error, bias, time series, prediction, forecast accuracy, demand planning, forecast method, weighted moving average, deseasonalize, seasonal index, forecast horizon, error metrics, best forecast method"
---

# Demand Forecasting

## Purpose

Apply time series forecasting methods to historical demand data, evaluate forecast accuracy using error metrics, detect bias, and select the best method. Covers moving averages, exponential smoothing (simple, Holt's trend-corrected, Winters' seasonal), and systematic method comparison.

## When to Use

- Generating demand forecasts for inventory, production, or capacity planning
- Choosing between forecasting methods for a specific demand pattern
- Evaluating forecast accuracy and detecting systematic bias
- Optimizing smoothing constants (alpha, beta, gamma)
- Decomposing demand into level, trend, and seasonal components
- Building a forecasting model for a new product or market
- Comparing qualitative judgment vs quantitative forecast

## Foundation

### Forecasting Methods

#### 1. Simple Moving Average (SMA)
- F_(t+1) = (1/N) * SUM(D_(t-N+1) to D_t)
- N = number of periods in the window
- Equal weight to all N observations; older data drops off

#### 2. Weighted Moving Average (WMA)
- F_(t+1) = SUM(w_i * D_(t-i+1)) where SUM(w_i) = 1
- More recent periods get higher weights

#### 3. Simple Exponential Smoothing (SES)
- F_(t+1) = alpha * D_t + (1 - alpha) * F_t
- Equivalent: F_(t+1) = F_t + alpha * (D_t - F_t)
- alpha in [0, 1]; higher alpha = more responsive, less smooth
- Best for: stationary demand (no trend, no seasonality)

#### 4. Holt's Method (Trend-Corrected)
- Level: L_t = alpha * D_t + (1 - alpha) * (L_(t-1) + T_(t-1))
- Trend: T_t = beta * (L_t - L_(t-1)) + (1 - beta) * T_(t-1)
- Forecast: F_(t+k) = L_t + k * T_t
- Best for: demand with trend but no seasonality

#### 5. Winters' Method (Trend + Seasonality)

**Multiplicative** (seasonal variation proportional to level):
- Level: L_t = alpha * (D_t / S_(t-m)) + (1 - alpha) * (L_(t-1) + T_(t-1))
- Trend: T_t = beta * (L_t - L_(t-1)) + (1 - beta) * T_(t-1)
- Seasonal: S_t = gamma * (D_t / L_t) + (1 - gamma) * S_(t-m)
- Forecast: F_(t+k) = (L_t + k * T_t) * S_(t+k-m)

**Additive** (seasonal variation constant):
- Level: L_t = alpha * (D_t - S_(t-m)) + (1 - alpha) * (L_(t-1) + T_(t-1))
- Trend: T_t = beta * (L_t - L_(t-1)) + (1 - beta) * T_(t-1)
- Seasonal: S_t = gamma * (D_t - L_t) + (1 - gamma) * S_(t-m)
- Forecast: F_(t+k) = L_t + k * T_t + S_(t+k-m)

Where m = seasonal period length (e.g., 12 for monthly, 4 for quarterly).

### Error Metrics

| Metric | Formula | Interpretation |
|--------|---------|----------------|
| Error | e_t = D_t - F_t | Positive = under-forecast |
| MAD | (1/n) * SUM(abs(e_t)) | Average absolute error; scale-dependent |
| MSE | (1/n) * SUM(e_t^2) | Penalizes large errors more heavily |
| MAPE | (1/n) * SUM(abs(e_t)/D_t) * 100% | Percentage error; scale-independent |
| Bias | (1/n) * SUM(e_t) | Systematic over/under forecasting |
| Tracking Signal | Running Sum of Errors / MAD | Should stay within +/- 4; out of bounds = bias |

### Optimal Smoothing Constants

- Minimize MSE (or MAD) over the historical fitting period
- Use Excel Solver or Python scipy.optimize.minimize
- Typical ranges: alpha 0.05-0.50, beta 0.01-0.20, gamma 0.05-0.50
- Overfit risk: validate on hold-out period, not just fitting period

### Seasonal Index Calculation

1. Compute centered moving average (CMA) of length m
2. Ratio: D_t / CMA_t for each period
3. Average ratios for each season across years
4. Normalize so indices sum to m (or average to 1.0)

## Process

### Three Entry Modes

| Mode | User Provides | Skill Does |
|------|--------------|------------|
| **Guided** | "Forecast next quarter's demand" | Asks for historical data, identifies pattern (trend/seasonality), recommends method |
| **Context Dump** | Historical demand data + desired methods | Applies all requested methods, computes errors, recommends best |
| **Quick Draft** | "Compare SES vs Holt's for my data" | Template with method formulas pre-built, ready for data |

### Adaptive Questioning

| If User Provides... | Then Ask About... |
|---------------------|-------------------|
| Raw demand data | How many periods ahead to forecast? Any known seasonality? |
| "Use exponential smoothing" | Simple, Holt's, or Winters'? Or compare all three? |
| Alpha value specified | Should we also optimize alpha to compare? |
| Monthly data, 2+ years | Is there seasonality? (check visually or statistically) |
| Forecast for new product | No history available -- consider analogous product data or qualitative methods |

## Excel Output Specification

### Tab 1: Historical Data
- **Column A**: Period label (Month/Quarter/Week)
- **Column B**: Actual demand (blue font, yellow fill)
- **Row below data**: Summary stats (mean, std dev, CV, min, max)
- Line chart of historical demand with trend line
- Visual inspection notes: trend present? seasonal pattern? outliers?

### Tab 2: Forecast Methods Comparison
- Each method in a column block:
  - SMA (3-period and 5-period)
  - SES (with alpha input cell)
  - Holt's (with alpha, beta input cells)
  - Winters' (with alpha, beta, gamma input cells) if seasonal data
- Actual vs Forecast for each method plotted together
- Smoothing constant inputs: blue font, yellow fill
- Formulas in black

### Tab 3: Error Analysis
- Error metrics table for each method:
  - MAD, MSE, RMSE, MAPE, Bias, Tracking Signal
- Tracking signal chart over time (with +/-4 control limits)
- Highlight: best method per metric in bold green
- Residual plots for top 2 methods

### Tab 4: Best Method Selection
- Ranking matrix: methods vs metrics with rank (1 = best)
- Overall recommendation with justification
- Optimal smoothing constants (from Solver or Python optimization)
- Forecast for next k periods using best method
- Confidence range: forecast +/- z * MAD (or using standard error)

### Tab 5: Assumptions
- Data frequency and completeness
- Stationarity assumption (or trend/seasonal decomposition)
- Forecast horizon and reliability degradation
- No structural breaks assumed (new products, COVID, etc.)
- Method limitations (SES can't handle trend; Holt's can't handle seasonality)

## Output

| Mode | Deliverable |
|------|------------|
| **Excel** | Formatted workbook with all 5 tabs, charts, Solver-ready optimization |
| **Python** | Script using statsmodels (ExponentialSmoothing) or manual implementation with optimization |
| **Both** | Excel workbook + Python script with cross-validation |
| **Teach** | Method-by-method walkthrough: compute by hand, then automate, then compare |

## Anti-Patterns

1. **Using SES when there's a clear trend** -- SES will systematically lag; use Holt's instead
2. **Using Holt's for seasonal data** -- trend correction alone won't capture seasonality; use Winters'
3. **Optimizing on all data with no hold-out** -- always split into training and validation sets
4. **High alpha without justification** -- alpha > 0.5 means you're basically using last period's demand
5. **Ignoring tracking signal** -- a forecast can have low MAD but high bias; tracking signal catches drift
6. **Averaging seasonal indices that don't sum to m** -- always normalize seasonal indices
7. **Forecasting too far ahead** -- accuracy degrades rapidly beyond 2-3 seasonal cycles
8. **Confusing MAD and standard deviation** -- for normal errors, sigma ≈ 1.25 * MAD
9. **Not plotting residuals** -- error metrics alone can miss patterns; always visualize residuals

## Related Skills

- `safety-stock-policy` -- forecast error (MAD/sigma) directly determines safety stock levels
- `aggregate-planning` -- demand forecast is the primary input to aggregate production planning
