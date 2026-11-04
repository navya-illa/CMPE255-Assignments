# CRISP-DM Report: Telco Customer Churn

## Executive summary

This project follows all six CRISP-DM phases to develop a churn-risk scoring workflow. The objective is not merely to maximize a metric; it is to identify a manageable group of customers for retention outreach while making the cost, uncertainty, and limitations explicit.

## 1. Business understanding

The stakeholder is a telecom retention team. The data-science question is: **which active customers are most likely to churn soon?** The target is the observed `Churn` field. A practical success criterion is strong recall among the highest-risk 30% of customers, while tracking precision, PR-AUC, calibration, and outreach capacity.

Risks include treating correlation as causation, targeting customers unfairly, using post-churn information, and optimizing for a metric that does not reflect retention value.

## 2. Data understanding

The dataset contains demographic, service, contract, billing, and tenure attributes. The notebook profiles data types, missing values, class balance, categorical distributions, and churn rates across contract and service groups.

## 3. Data preparation

`TotalCharges` is converted from text to numeric. The customer identifier is removed. Numeric variables are median-imputed and standardized; categorical variables are mode-imputed and one-hot encoded. The split is stratified and preprocessing is fitted inside a scikit-learn pipeline to avoid leakage.

## 4. Modeling

Logistic regression provides an interpretable baseline. A random forest provides a nonlinear comparison. Cross-validation is used on the training set; the test set is held out until final evaluation.

## 5. Evaluation

The notebook reports ROC-AUC, PR-AUC, classification metrics at a documented outreach threshold, ROC and precision-recall curves, and the confusion matrix. The final business decision should use expected retention value and contact cost, not a generic 0.5 threshold.

## 6. Deployment

The selected pipeline is serialized with joblib. `score_customer.py` demonstrates single-record scoring. A production implementation should monitor drift, missingness, calibration, recall at the outreach budget, and downstream retention outcomes. Retraining should be triggered by a sustained performance or data-quality decline.

## Limitations

This is observational data, so the model identifies risk rather than proving that an intervention will prevent churn. The dataset may not represent current telecom customers, and threshold decisions require real cost and benefit estimates.

## Reproducible execution results

The corrected script was executed from a clean Python environment. The selected model was logistic regression based on the highest mean five-fold training cross-validation ROC-AUC (0.8458). On the held-out test set, ROC-AUC was 0.8416 and PR-AUC was 0.6337. At an outreach budget of the top 30% of customers, the out-of-fold-derived threshold was 0.6427, precision was 0.5647, and recall was 0.6765.

The threshold is selected from out-of-fold training predictions rather than the test set. The test set is used only once for final reporting. The saved pipeline and threshold metadata are in artifacts/.

## Reproducibility and artifacts

Run python notebook/CRISP_DM_Telco_Churn.py. It downloads the public dataset, creates charts and CSV metrics under artifacts/, and writes artifacts/telco_churn_pipeline.joblib. The scoring example in deployment/score_customer.py loads the same saved pipeline and threshold, preventing a deployment-time threshold mismatch.

Artifacts include data-quality checks, class-balance chart, model comparison, ROC and precision-recall curves, confusion matrix, classification report, evaluation metrics, and the serialized model.

