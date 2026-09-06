# Regression Prompt Engineering Record

## 1. Role, objective, and constraints

> Act as a senior data scientist and reproducible-ML engineer. Build separate regression analyses for synthetic NYC taxi trip duration and fare. Use fixed seed 42, exclude both targets from the predictor matrix, prevent leakage, and do not present synthetic accuracy as real transportation performance.

**Technique:** role prompting, context grounding, and leakage constraints.

## 2. Data audit

> Inspect schema, missing values, duplicate rows, identifiers, target ranges, outliers, target distributions, and possible leakage before modeling. Report which columns are predictors and which are targets. Return executable checks for the expected schema.

**Technique:** staged decomposition and data-quality evidence.

## 3. Experiment design

> Compare a mean baseline, standardized Ridge regression, and random forest independently for duration and fare. Report MAE, RMSE, and R², select by RMSE, and explain why multiple metrics and residual diagnostics are needed.

**Technique:** controlled comparison and metric-definition constraints.

## 4. Implementation

> Implement one reproducible command-line script accepting `--data` and `--output`. Save model-comparison.csv, selected-models.csv, model-comparison.png, residual-diagnostics.png, results-summary.json, and all evidence required for the report. Keep selection logic separate from plotting logic.

**Technique:** explicit deliverables and reproducibility contract.

## 5. Adversarial metric audit

> Challenge outliers, skew, residual patterns, synthetic feature relationships, leakage, and whether R² reflects practical usefulness. Check that the selected model is the lowest-RMSE method for each target and reconcile every value with the exported files.

**Technique:** adversarial review and evidence reconciliation.

## 6. Interpretation

> Treat predictions as estimates, not guaranteed travel times or fares. Discuss temporal and geographic validation, traffic and weather variables, subgroup errors, drift, calibration, and the difference between statistical fit and operational usefulness.

**Technique:** bounded interpretation and responsible-AI constraint.

## 7. Visualization audit

> Generate and inspect target-distribution, model-comparison, and residual-diagnostic figures. Verify readable units, labels, legends, target names, and residual axes. Ensure residual plots are described as diagnostics rather than proof of production readiness.

**Technique:** visual output contract and semantic verification.

## 8. Reproducibility and documentation

> Write the README, notebook, report, requirements, limitations, references, dataset-attribution note, and AI-assistance disclosure from verified outputs. The notebook must show the audit, execution command, comparison table, figures, selected-model export, and JSON reconciliation.

**Technique:** provenance constraint and publication-ready formatting.

## 9. Final consistency check

> Re-run the documented command, confirm every artifact named in results-summary.json exists, verify notebook paths and README image links, reconcile target-level metrics across the CSV, JSON, report, and README, and correct discrepancies before completion.

**Technique:** iterative refinement and completion criteria.
