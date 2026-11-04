# SEMMA: Bank Marketing

## Analytical goal

Predict whether a customer will subscribe to a term deposit and compare model performance with operational decision thresholds.

## Dataset

Bank Marketing dataset, available through Kaggle and the UCI Machine Learning Repository. The project records the Kaggle source and uses a Colab upload/download fallback.

## SEMMA stages

1. **Sample:** define the analytical population and create reproducible train/validation/test samples.
2. **Explore:** inspect distributions, class balance, missing/unknown values, associations, and candidate predictors.
3. **Modify:** encode categorical variables, transform numeric variables, address class imbalance, and document feature decisions.
4. **Model:** train baseline, logistic, random forest, and gradient-boosting models; compare models under consistent validation.
5. **Assess:** evaluate discrimination, threshold behavior, calibration, error costs, stability, and practical usefulness.

## SAS-oriented demonstration

The `sas/` directory contains a PROC-style mapping and a short guide showing how the same SEMMA flow can be reproduced in SAS Enterprise Miner or an available SAS trial. Python remains the reproducible execution path.

## Artifacts

- `notebook/SEMMA_Bank_Marketing.ipynb`
- `report/SEMMA_Bank_Marketing_Report.md`
- `critique/critique_log.md`
- `sas/SEMMA_SAS_Companion.md`
- `medium/medium_article_draft.md`
- `video/walkthrough_script.md`
