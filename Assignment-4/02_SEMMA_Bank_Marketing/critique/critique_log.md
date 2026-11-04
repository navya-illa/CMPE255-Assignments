# SEMMA critique and revision log

## Revision 1 — stage completeness

The initial draft used the name SEMMA but omitted the sampling rationale and treated exploration as a few plots. The revision documents the analytical population, stratified holdout, class balance, missing/unknown values, and candidate-variable inspection.

## Revision 2 — modeling validity

The initial draft encoded variables before splitting. The revision fits all imputation, scaling, and one-hot transformations within a pipeline, and compares models using the same stratified cross-validation protocol.

## Revision 3 — assessment quality

Accuracy was removed as the primary criterion because subscriptions are imbalanced. The revision reports ROC-AUC, PR-AUC, thresholded classification metrics, and campaign-capacity assumptions.

## Manual verification

- Run all cells from a fresh Colab runtime.
- Confirm the UCI/Kaggle source and dataset version in the notebook.
- Confirm no future-contact variable is used without a documented leakage discussion.
- Confirm the threshold is based only on training/validation decisions.
- Reconcile every metric in the report with notebook output.

## Revision 4 — leakage and reproducibility

**Critic finding:** The duration variable is measured during contact and can leak information into a pre-contact campaign model. The previous notebook also did not save an executable model artifact.

**Revision made:** duration is explicitly excluded and the decision is recorded in artifacts/leakage_decision.json. The selected pipeline, threshold, metrics, plots, and classification report are saved.

**Verification:** Clean execution completed with a selected gradient-boosting model and held-out evaluation metrics.

