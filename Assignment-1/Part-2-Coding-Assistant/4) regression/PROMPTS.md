# Prompt Engineering Record — Regression

## 1. Role, objective, and constraints
> Act as a senior data scientist and reproducible-ML engineer. Build NYC taxi duration and fare regression experiments with fixed seed 42 and no target leakage.
## 2. Data audit
> Report schema, missing values, duplicates, ranges, timestamps, outliers, target distributions, identifiers, and possible leakage.
## 3. Experiment design
> Compare a mean baseline, Ridge regression, and random forest for duration and fare. Report MAE, RMSE, R², and RMSLE and select by RMSE.
## 4. Implementation
> Use reproducible `--data` and `--output` scripts. Save comparisons, selected models, residual diagnostics, target distributions, and JSON results.
## 5. Adversarial metric audit
> Challenge outliers, skew, residual patterns, leakage, synthetic relationships, and whether R² reflects practical usefulness.
## 6. Interpretation
> Treat predictions as estimates, not guaranteed travel times or fares. Discuss real data, temporal validation, traffic, weather, drift, and geographic variation.
## 7. Visualization audit
> Inspect target-distribution and residual plots for readable units, labels, and accurate interpretation.
## 8. Reproducibility and documentation
> Write README, report, notebook, setup, limitations, references, and AI disclosure only from verified outputs.
## 9. Final consistency check
> Re-run commands, verify links and images, reconcile all values with artifacts, and correct discrepancies.
