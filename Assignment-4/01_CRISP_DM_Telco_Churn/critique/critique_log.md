# CRISP-DM critique and revision log

## Revision 1 — methodology coverage

**Reviewer prompt:** Use the shared expert critique prompt with the CRISP-DM persona.

**Issues found:** The first draft treated modeling as the entire project, did not define a business success metric, and lacked deployment monitoring.

**Revision made:** Added stakeholder goals, outreach-budget evaluation, probability calibration discussion, model artifact export, scoring code, and a monitoring/retraining plan.

## Revision 2 — technical validity

**Issues found:** Preprocessing could leak test-set information; `TotalCharges` required numeric coercion; accuracy alone would be misleading for churn.

**Revision made:** Fit preprocessing only inside a pipeline on training data, document coercion and missingness, and report ROC-AUC, PR-AUC, recall, and thresholded decisions.

## Manual verification checklist

- Run the notebook from a clean Colab runtime.
- Confirm the dataset shape and target distribution.
- Confirm no identifier is used as a predictor.
- Confirm preprocessing is fitted only through the training pipeline.
- Confirm deployment scoring accepts a single customer record.
- Record actual metrics after execution rather than inventing them.

## Revision 3 — threshold and deployment consistency

**Critic finding:** The initial threshold was calculated from test predictions and the deployment scorer used an unrelated fixed 0.70 cutoff.

**Revision made:** The threshold is now derived from out-of-fold training probabilities at the stated outreach budget. The saved evaluation metadata is loaded by the deployment scorer, and final test metrics are reported only after threshold selection.

**Verification:** Clean execution produced evaluation_metrics.json, model_comparison.csv, plots, a serialized pipeline, and a working single-record scoring path.

