# Anomaly-Detection Prompt Engineering Record

## 1. Role, objective, and constraints

> Act as a senior data scientist and reproducible-ML engineer. Build a server-telemetry anomaly-detection experiment using synthetic signals. Use fixed seed 42, keep labels strictly for evaluation, and explain that alerts are investigation signals rather than proof of incidents.

**Technique:** role prompting, context grounding, and label-use constraints.

## 2. Data audit

> Audit schema, missing values, duplicate rows, signal count, signal ranges, anomaly prevalence, time ordering if available, and anomaly archetypes before fitting detectors. Report explicitly that labels are not used during training.

**Technique:** staged decomposition and data-quality evidence.

## 3. Experiment design

> Compare Isolation Forest, Local Outlier Factor, and One-Class SVM using the same evaluation population and documented contamination assumptions. Report ROC-AUC, PR-AUC, precision, recall, F1, false-positive rate, alert rate, and threshold behavior. Emphasize PR-AUC because anomalies are rare.

**Technique:** fair comparison and metric-definition constraints.

## 4. Implementation

> Implement one reproducible command-line script accepting `--data` and `--output`. Save model-comparison.csv, model-comparison.png, selected-confusion-matrix.png, anomaly-feature-deviations.csv, results-summary.json, and all evidence needed for the report. Keep labels out of model fitting.

**Technique:** explicit deliverables and reproducibility contract.

## 5. Adversarial metric audit

> Challenge class imbalance, contamination sensitivity, threshold choice, false-alert cost, drift, and whether ROC-AUC hides poor alert quality. Reconcile the selected method, all metrics, label-use statement, and artifact list with the exported CSV and JSON files.

**Technique:** adversarial review and evidence reconciliation.

## 6. Interpretation

> Treat an alert as a signal for investigation, not proof of an attack or system failure. Discuss analyst feedback, alert-volume limits, threshold review, drift monitoring, changing operating conditions, and documented response procedures.

**Technique:** bounded interpretation and responsible-AI constraint.

## 7. Visualization audit

> Generate and inspect detector-comparison, confusion-matrix, and feature-deviation evidence. Verify readable method names, metric labels, anomaly terminology, and threshold explanations. Avoid visual claims that exceed the synthetic evaluation.

**Technique:** visual output contract and semantic verification.

## 8. Reproducibility and documentation

> Write the README, notebook, report, requirements, limitations, references, dataset-attribution note, and AI-assistance disclosure from verified outputs. The notebook must show the audit, execution command, comparison table, visual evidence, label-use check, and JSON reconciliation.

**Technique:** provenance constraint and publication-ready formatting.

## 9. Final consistency check

> Re-run the documented command, confirm every artifact named in results-summary.json exists, verify notebook paths and README image links, reconcile detector metrics across CSV, JSON, report, and README, and correct discrepancies before completion.

**Technique:** iterative refinement and completion criteria.
