# Classification Prompt Engineering Record

## 1. Role, objective, and constraints

> Act as a senior data scientist and reproducible-ML engineer. Build a customer-churn classification experiment from the synthetic AutoML-style benchmark. Use fixed seed 42, exclude the churn target and any identifiers from the feature matrix, prevent leakage, and derive every conclusion from executed artifacts. Treat the output as a data-mining experiment, not a production claim.

**Technique:** role prompting, context grounding, and constraint specification.

## 2. Data audit

> Inspect the data before modeling. Report shape, schema, missing values, duplicate rows, class balance, feature ranges, identifier columns, and possible target leakage. Return executable validation checks and fail clearly if the expected churn schema is absent.

**Technique:** staged decomposition and evidence requirements.

## 3. Experiment design

> Compare a majority-class baseline, logistic regression, and random forest using a stratified train/test split. Report PR-AUC, ROC-AUC, precision, recall, F1, and threshold behavior. Use PR-AUC as the primary selection metric because churn is imbalanced, and explain why accuracy alone is insufficient.

**Technique:** output contract and metric-selection constraints.

## 4. Implementation

> Implement one reproducible command-line script accepting `--data` and `--output`. Save model-comparison.csv, results-summary.json, a model-comparison figure, a selected-model confusion matrix, permutation-importance CSV/PNG files, and any other evidence required to support the README and report. Use deterministic model settings.

**Technique:** explicit deliverables and reproducibility contract.

## 5. Adversarial metric audit

> Challenge whether class imbalance, threshold choice, calibration, leakage, or a majority baseline changes the conclusion. Reconcile the selected model and every reported metric with the exported comparison CSV and JSON. Do not describe feature importance as causal evidence.

**Technique:** adversarial review and evidence reconciliation.

## 6. Interpretation

> Explain the selected model as a statistical risk signal, not customer intent. Discuss false positives, false negatives, intervention cost, fairness review, calibration, drift, and human oversight. Keep the interpretation bounded by the synthetic benchmark.

**Technique:** responsible interpretation and bounded claims.

## 7. Visualization audit

> Generate and inspect class-balance, model-comparison, confusion-matrix, and permutation-importance figures. Verify readable titles, axes, labels, units, and model names. Ensure every figure corresponds to the executed outputs.

**Technique:** visual output contract and semantic verification.

## 8. Reproducibility and documentation

> Write the README, notebook, report, requirements, limitations, references, dataset-attribution note, and AI-assistance disclosure from verified outputs. The notebook must show the audit, execution command, comparison table, visual evidence, and JSON reconciliation.

**Technique:** provenance constraint and publication-ready formatting.

## 9. Final consistency check

> Re-run the documented command, confirm that every artifact named in results-summary.json exists, verify notebook paths and README image links, reconcile the report table with CSV/JSON values, and correct any discrepancy before declaring the experiment complete.

**Technique:** iterative refinement and completion criteria.
