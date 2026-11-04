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
