# Prompt Engineering Record — Classification

## 1. Role, objective, and constraints
> Act as a senior data scientist and reproducible-ML engineer. Build a customer-churn classification experiment with fixed seed 42, no identifier features, no leakage, and conclusions grounded in executed artifacts.
## 2. Data audit
> Report shape, schema, missing values, duplicates, target balance, ranges, identifiers, and possible leakage before modeling.
## 3. Experiment design
> Compare a majority baseline, logistic regression, and random forest using stratified evaluation. Report accuracy, precision, recall, F1, ROC-AUC, and PR-AUC, emphasizing PR-AUC for imbalance.
## 4. Implementation
> Use reproducible `--data` and `--output` scripts. Save comparisons, confusion matrices, class distribution, permutation importance, predictions, and JSON results.
## 5. Adversarial metric audit
> Challenge class imbalance, thresholds, recall, calibration, leakage, and whether accuracy alone supports model selection.
## 6. Interpretation
> Treat churn as predicted risk, not intent or causation. Discuss fairness, calibration, intervention cost, and human oversight.
## 7. Visualization audit
> Inspect class-distribution, confusion-matrix, and feature-importance figures for readable and accurate labels.
## 8. Reproducibility and documentation
> Write README, report, notebook, setup, limitations, references, and AI disclosure only from verified outputs.
## 9. Final consistency check
> Re-run commands, verify links and images, reconcile README values with artifacts, and correct discrepancies.
