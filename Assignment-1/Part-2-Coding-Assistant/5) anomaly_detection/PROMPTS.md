# Prompt Engineering Record — Anomaly Detection

## 1. Role, objective, and constraints
> Act as a senior data scientist and reproducible-ML engineer. Build server-telemetry anomaly detection with fixed seed 42 and labels used only for evaluation.
## 2. Data audit
> Report schema, missing values, duplicates, time ordering, ranges, anomaly prevalence, and anomaly archetypes before modeling.
## 3. Experiment design
> Compare robust z-score, Isolation Forest, Local Outlier Factor, and One-Class SVM. Report ROC-AUC, PR-AUC, precision, recall, F1, false-positive rate, alert rate, and threshold settings.
## 4. Implementation
> Use reproducible `--data` and `--output` scripts. Save model comparisons, confusion matrix, feature deviations, plots, predictions, and JSON results.
## 5. Adversarial metric audit
> Challenge class imbalance, false-alert cost, threshold sensitivity, contamination assumptions, drift, and whether ROC-AUC hides poor alert quality.
## 6. Interpretation
> Treat alerts as investigation signals, not proof of attacks or failures. Discuss analyst feedback, calibration, alert limits, drift, and response procedures.
## 7. Visualization audit
> Inspect model-comparison, confusion-matrix, and feature-deviation figures for readable and accurate anomaly labels.
## 8. Reproducibility and documentation
> Write README, report, notebook, setup, limitations, references, and AI disclosure from verified artifacts only.
## 9. Final consistency check
> Re-run commands, verify links and images, reconcile README values with CSV/JSON artifacts, and correct discrepancies.
