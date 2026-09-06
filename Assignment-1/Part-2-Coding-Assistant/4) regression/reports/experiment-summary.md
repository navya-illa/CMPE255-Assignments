# Regression Experiment Summary

## Objective

Predict synthetic NYC taxi trip duration and fare while comparing baseline, linear, and nonlinear regression methods and checking target leakage and residual behavior.

## Dataset and audit

The benchmark contains 10,000 synthetic trips, six numeric predictors, and two targets: duration and fare. The audit checks schema, missing values, duplicate rows, target ranges, and target exclusion from the feature matrix. The split uses a fixed random state of 42 with a 20% test set.

## Methods and verified results

The comparison includes a mean baseline, standardized Ridge regression, and random forest. RMSE is used for selection, while MAE and R² provide additional context.

| Model | Target | MAE | RMSE | R² |
|---|---|---:|---:|---:|
| Mean baseline | Duration | 69.1766 | 87.8493 | -0.0000 |
| Ridge | Duration | 61.7066 | 78.3068 | 0.2054 |
| Random forest | Duration | **21.7847** | **27.4499** | **0.9024** |
| Mean baseline | Fare | 1.8430 | 2.3169 | -0.0004 |
| Ridge | Fare | 1.7358 | 2.1814 | 0.1131 |
| Random forest | Fare | **1.1697** | **1.4824** | **0.5904** |

Random forest was selected for both targets. The authoritative values are in `artifacts/model-comparison.csv` and `artifacts/selected-models.csv`.

## Evidence artifacts

- `model-comparison.png` compares target distributions and RMSE across methods.
- `residual-diagnostics.png` checks residual patterns for the selected models.
- `results-summary.json` records the audit, split, model comparison, selected models, artifacts, and limitations.

## Interpretation and limitations

These results demonstrate a reproducible workflow, not real New York travel-time or fare accuracy. The data is synthetic and omits traffic, weather, geography, temporal effects, and operational changes. A real use case would require licensed trip data, temporal and geographic validation, residual review across subgroups, calibration, drift monitoring, and error-cost analysis.

## Reproducibility

Run `python src/run_experiment.py --data data/nyc_taxi.csv --output artifacts`. The notebook performs the data audit, executes the script, displays the comparison and residual figures, and checks the selected-model export against the JSON summary.

## AI assistance

The AI coding assistant supported experiment design, feature engineering, implementation, debugging, visualization, and documentation. The conclusions were checked against the executed CSV, PNG, and JSON artifacts.
