# Anomaly Detection Experiment Summary

## Objective

Detect unusual server-telemetry observations while comparing unsupervised detectors and making the operational cost of false alerts visible.

## Dataset and audit

The benchmark contains 10,000 synthetic telemetry records, six signals, and an anomaly rate of 3.43%. The audit checks schema, missing values, duplicate rows, signal count, and anomaly prevalence. Labels are retained for evaluation only and are not used to fit the detectors.

## Methods and verified results

The experiment compares Isolation Forest, Local Outlier Factor, and One-Class SVM. PR-AUC is emphasized because anomalies are rare; false-positive rate, precision, recall, and F1 are also reported.

| Method | PR-AUC | ROC-AUC | Precision | Recall | F1 | False-positive rate |
|---|---:|---:|---:|---:|---:|---:|
| Isolation Forest | **0.9908** | **0.9995** | **0.9534** | **0.9534** | **0.9534** | **0.0017** |
| One-Class SVM | 0.4744 | 0.9353 | 0.4577 | 0.4577 | 0.4577 | 0.0193 |
| Local Outlier Factor | 0.0510 | 0.5286 | 0.0816 | 0.0816 | 0.0816 | 0.0326 |

Isolation Forest was selected using PR-AUC. The complete comparison is in `artifacts/model-comparison.csv`, and the selected metrics are recorded in `artifacts/results-summary.json`.

## Evidence artifacts

- `model-comparison.png` compares detector PR-AUC values.
- `selected-confusion-matrix.png` shows thresholded errors for the selected detector.
- `anomaly-feature-deviations.csv` summarizes feature-level deviations.
- `results-summary.json` records label usage, the audit, methods, metrics, artifact names, and limitations.

## Interpretation and limitations

An alert is a signal for investigation, not proof of an attack or system failure. Performance depends on contamination assumptions, thresholding, data drift, and changing operating conditions. The synthetic benchmark may make separation easier than production telemetry. Deployment would require analyst feedback, alert-volume limits, threshold review, drift monitoring, and documented response procedures.

## Reproducibility

Run `python src/run_experiment.py --data data/server_telemetry.csv --output artifacts`. The notebook performs the audit, executes the script, displays detector evidence, and verifies that labels remain evaluation-only.

## AI assistance

The AI coding assistant supported experiment design, implementation, debugging, evaluation, visualization, and documentation. The conclusions were checked against the executed CSV, PNG, and JSON artifacts.
