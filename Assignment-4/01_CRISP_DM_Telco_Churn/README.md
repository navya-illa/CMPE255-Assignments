# CRISP-DM: Telco Customer Churn

## Business goal

Identify customers at high risk of churn and provide retention-oriented insights that a telecom business could act on.

## Dataset

IBM Telco Customer Churn, commonly distributed through Kaggle. The notebook includes a reproducible download option and a manual upload fallback for Colab.

## CRISP-DM stages

1. **Business understanding:** define churn, stakeholders, costs, success criteria, and project risks.
2. **Data understanding:** collect data, describe variables, inspect quality, and explore churn patterns.
3. **Data preparation:** clean `TotalCharges`, encode categorical variables, handle missingness, split data, and prevent leakage.
4. **Modeling:** establish a baseline, train logistic regression and tree-based models, tune only on training data, and calibrate probabilities.
5. **Evaluation:** assess ROC-AUC, PR-AUC, recall at an outreach budget, calibration, subgroup behavior, and business impact.
6. **Deployment:** export the selected model, preprocessing pipeline, scoring script, API example, monitoring plan, and retraining triggers.

## Artifacts

- `notebook/CRISP_DM_Telco_Churn.ipynb`
- `report/CRISP_DM_Telco_Churn_Report.md`
- `critique/critique_log.md`
- `deployment/score_customer.py`
- `medium/medium_article_draft.md`
- `video/walkthrough_script.md`
