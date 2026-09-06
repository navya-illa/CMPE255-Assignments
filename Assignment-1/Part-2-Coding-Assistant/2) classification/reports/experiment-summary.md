# Classification Experiment Summary

## Objective

Predict customer churn risk and compare a simple baseline, an interpretable linear model, and a nonlinear tree-based model. The experiment emphasizes metrics appropriate for an imbalanced target.

## Dataset and audit

The benchmark contains 10,000 synthetic customer records, ten numeric predictors, and a churn rate of 14.67%. The audit found no missing values or duplicate rows. The churn label is excluded from the feature matrix, and the data is split with stratification using a fixed random state of 42.

## Methods and verified results

The experiment compares a majority-class baseline, logistic regression, and random forest. PR-AUC is the primary selection metric because the positive class is uncommon.

| Model | PR-AUC | ROC-AUC | Precision | Recall | F1 |
|---|---:|---:|---:|---:|---:|
| Majority baseline | 0.1465 | 0.5000 | 0.0000 | 0.0000 | 0.0000 |
| Logistic regression | 0.6985 | 0.8615 | 0.8045 | 0.4915 | 0.6102 |
| Random forest | **0.9320** | **0.9624** | **0.9828** | **0.7816** | **0.8707** |

Random forest was selected. The authoritative comparison is `artifacts/model-comparison.csv`, and the selected-model metrics are recorded in `artifacts/results-summary.json`.

## Evidence artifacts

- `model-comparison.png` shows class balance and PR-AUC across models.
- `selected-confusion-matrix.png` shows thresholded test-set errors.
- `permutation-importance.csv` and `permutation-importance.png` summarize feature sensitivity.
- `results-summary.json` records the audit, split, selection rule, metrics, artifact names, and limitations.

## Interpretation and limitations

The model estimates statistical risk, not customer intent or causal churn drivers. The benchmark is synthetic, and the reported threshold-dependent precision and recall should not be treated as deployment performance. A real use case would require licensed data, calibration, fairness review, cost-sensitive threshold selection, intervention testing, drift monitoring, and human oversight.

## Reproducibility

Run `python src/run_experiment.py --data data/customer_churn.csv --output artifacts`. The notebook provides the audit, execution command, comparison table, visual evidence, and JSON reconciliation. The generated artifacts, rather than unexecuted narrative claims, are the source of the reported results.

## AI assistance

The AI coding assistant supported experiment design, implementation, debugging, visualization, and documentation. The conclusions were checked against the executed script and exported CSV, PNG, and JSON artifacts.
