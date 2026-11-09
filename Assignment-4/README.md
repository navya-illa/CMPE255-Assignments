# CMPE 255 Assignment 4  
# Principled Data Science with CRISP-DM, SEMMA, and KDD

This assignment demonstrates three complete, methodology-driven data-science projects. Each project uses a different dataset and follows the full workflow of one established data-mining methodology.

The goal is not only to train a model. Each project connects:

1. A clearly defined business or knowledge-discovery problem
2. Data collection and quality verification
3. Methodology-specific preparation and analysis
4. Reproducible modeling or data mining
5. Evaluation using appropriate metrics
6. Interpretation and limitations
7. Deployment or operational handoff
8. AI-assisted critique, revision, and manual verification

---

## Projects at a glance

| Project | Methodology | Dataset | Main objective | Primary output |
|---|---|---|---|---|
| 01 | CRISP-DM | IBM Telco Customer Churn | Identify customers at high risk of churn for retention outreach | Churn probability pipeline and outreach policy |
| 02 | SEMMA | UCI Bank Marketing | Rank customers by likelihood of subscribing to a term deposit | Campaign-response scoring pipeline |
| 03 | KDD | UCI Online Retail | Discover customer segments and product co-purchase patterns | RFM segments and association rules |

Each methodology is applied to a different dataset so that the project demonstrates how the workflow changes depending on the analytical goal.

---

## Repository structure

```text
Assignment-4/
├── README.md
├── VERIFICATION_RESULTS.md
├── requirements.txt
├── .gitignore
│
├── 01_CRISP_DM_Telco_Churn/
│   ├── notebook/
│   │   ├── CRISP_DM_Telco_Churn.ipynb
│   │   ├── CRISP_DM_Telco_Churn.py
│   │   └── README.md
│   ├── artifacts/
│   │   ├── data_quality.csv
│   │   ├── target_distribution.csv
│   │   ├── model_comparison.csv
│   │   ├── evaluation_metrics.json
│   │   ├── classification_report.csv
│   │   ├── telco_churn_pipeline.joblib
│   │   └── charts and plots
│   ├── report/
│   │   ├── CRISP_DM_Telco_Churn_Report.md
│   │   └── stage_checklist.md
│   ├── critique/
│   │   └── critique_log.md
│   ├── deployment/
│   │   └── score_customer.py
│   ├── medium/
│   │   └── medium_article_draft.md
│   └── video/
│       └── walkthrough_script.md
│
├── 02_SEMMA_Bank_Marketing/
│   ├── notebook/
│   │   ├── SEMMA_Bank_Marketing.ipynb
│   │   ├── SEMMA_Bank_Marketing.py
│   │   └── README.md
│   ├── artifacts/
│   │   ├── leakage_decision.json
│   │   ├── model_comparison.csv
│   │   ├── evaluation_metrics.json
│   │   ├── classification_report.csv
│   │   ├── bank_marketing_pipeline.joblib
│   │   └── charts and plots
│   ├── report/
│   ├── critique/
│   ├── sas/
│   ├── deployment/
│   ├── medium/
│   └── video/
│
├── 03_KDD_Online_Retail/
│   ├── notebook/
│   │   ├── KDD_Online_Retail.ipynb
│   │   ├── KDD_Online_Retail.py
│   │   └── README.md
│   ├── artifacts/
│   │   ├── preprocessing_summary.csv
│   │   ├── cluster_silhouette_scores.csv
│   │   ├── cluster_selection.png
│   │   ├── segment_profiles.csv
│   │   ├── association_rules.csv
│   │   └── knowledge_summary.json
│   ├── knowledge_artifacts/
│   │   ├── segment_profiles.csv
│   │   └── association_rules.csv
│   ├── report/
│   ├── critique/
│   ├── medium/
│   └── video/
│
└── shared/
    ├── critique_prompt_template.md
    └── data_sources.md
```

---

## Methodology coverage

### 1. CRISP-DM: Telco Customer Churn

The CRISP-DM project follows all six phases:

1. **Business Understanding**  
   Defines the telecom retention stakeholder, churn-risk objective, outreach budget, success criteria, risks, and business constraints.

2. **Data Understanding**  
   Loads the IBM Telco Customer Churn data, inspects data types, missing values, class balance, and important customer attributes.

3. **Data Preparation**  
   Converts `TotalCharges` to numeric, normalizes service labels, removes the customer identifier, and uses leakage-safe preprocessing inside a scikit-learn pipeline.

4. **Modeling**  
   Compares logistic regression and random forest models using stratified cross-validation.

5. **Evaluation**  
   Reports ROC-AUC, PR-AUC, precision, recall, classification results, ROC curves, precision-recall curves, and a confusion matrix. The outreach threshold is selected from out-of-fold training predictions rather than the final test set.

6. **Deployment**  
   Saves the selected model and provides a single-record scoring script. The deployment scorer reads the same threshold used in evaluation so the operational decision rule remains consistent.

### 2. SEMMA: Bank Marketing

The SEMMA project follows all five stages:

1. **Sample**  
   Defines the campaign population and creates reproducible stratified training and test partitions.

2. **Explore**  
   Examines the target distribution, missing or unknown values, data types, and candidate predictors.

3. **Modify**  
   Imputes missing values, encodes categorical features, scales numerical features, and prevents leakage by fitting transformations only inside the modeling pipeline.

4. **Model**  
   Compares logistic regression, random forest, and histogram gradient boosting.

5. **Assess**  
   Evaluates ROC-AUC, PR-AUC, classification metrics, precision-recall curves, and campaign-capacity thresholds.

The `duration` feature is intentionally excluded because it is recorded during a campaign contact and would not be available for a pre-contact targeting decision. This decision is documented in `artifacts/leakage_decision.json`.

The `sas/` folder contains a SAS Enterprise Miner mapping. SAS screenshots should be added only after running the flow personally in SAS.

### 3. KDD: Online Retail

The KDD project follows the complete knowledge-discovery process:

1. **Selection**  
   Defines the valid customer and transaction population and identifies two discovery questions: customer segmentation and product co-purchase discovery.

2. **Preprocessing**  
   Removes cancelled invoices, nonpositive quantities, nonpositive prices, missing customer identifiers, and missing product descriptions.

3. **Transformation**  
   Creates customer-level RFM features and invoice-product basket representations. Product descriptions are normalized to reduce duplicate text variants.

4. **Data Mining**  
   Uses K-means clustering with silhouette analysis and Apriori association-rule mining.

5. **Interpretation and Evaluation**  
   Profiles segments using RFM medians and filters rules using support, confidence, and lift. The results are treated as candidate business knowledge requiring stability and holdout validation.

---

## Dataset sources

| Dataset | Public source | Task |
|---|---|---|
| IBM Telco Customer Churn | IBM public GitHub mirror / Kaggle equivalent | Binary classification |
| Bank Marketing | UCI Machine Learning Repository | Binary classification |
| Online Retail | UCI Machine Learning Repository | Clustering and association mining |

The scripts use stable public download URLs so the projects can run in Colab without requiring a Kaggle API token. The exact source and download logic are documented in each script.

---

## Installation

From the `Assignment-4` directory:

```bash
python -m pip install -r requirements.txt
```

Recommended environment:

- Python 3.10 or newer
- pandas
- NumPy
- scikit-learn
- matplotlib
- seaborn
- joblib
- requests
- openpyxl
- mlxtend

---

## Running the projects

### CRISP-DM

```bash
cd 01_CRISP_DM_Telco_Churn
python notebook/CRISP_DM_Telco_Churn.py
```

Expected outputs:

- Model comparison table
- Data-quality report
- Class-balance chart
- ROC curve
- Precision-recall curve
- Confusion matrix
- Classification report
- Evaluation metrics JSON
- Serialized churn pipeline

### SEMMA

```bash
cd 02_SEMMA_Bank_Marketing
python notebook/SEMMA_Bank_Marketing.py
```

Expected outputs:

- Leakage decision record
- Missingness table
- Target distribution
- Model comparison table
- ROC curve
- Precision-recall curve
- Classification report
- Evaluation metrics JSON
- Serialized bank-marketing pipeline

### KDD

```bash
cd 03_KDD_Online_Retail
python notebook/KDD_Online_Retail.py
```

Expected outputs:

- Preprocessing summary
- Cluster silhouette scores
- Cluster-selection chart
- Segment profiles
- Association rules
- Knowledge summary JSON

The KDD script supports a local dataset path for faster testing:

```bash
KDD_DATA_PATH=/path/to/Online_Retail.xlsx python notebook/KDD_Online_Retail.py
```

---

## Medium articles

**Medium URL for CRISP-DM:** [Discovering Customers at Risk of Churning Using CRISP-DM](https://medium.com/@9navya9/discovering-customers-at-risk-of-churning-using-crisp-dm-4d5ff67924c9)

**Medium URL for SEMMA:** [Predicting Bank Marketing Responses Using the SEMMA Methodology](https://medium.com/@9navya9/predicting-bank-marketing-responses-using-the-semma-methodology-5dad2c2d1690)

**Medium URL for KDD:** [Discovering Customer Segments and Product Associations from Online Retail Data](https://medium.com/@9navya9/discovering-customer-segments-and-product-associations-from-online-retail-data-f73cb4072903)

## Video Walkthrough

**YouTube Link:** https://youtu.be/3iF4H96IU3g

## Verified results

The corrected scripts were executed from a clean Python environment.

| Project | Verified result |
|---|---|
| CRISP-DM | Logistic regression selected; held-out ROC-AUC 0.8416; PR-AUC 0.6337; top-30% outreach recall 0.6765 |
| SEMMA | Histogram gradient boosting selected; held-out ROC-AUC 0.7927; PR-AUC 0.4512; 20% campaign-capacity recall 0.6087 |
| KDD | 4,338 customers; 17,138 valid multi-item invoices; best k=2; 282 frequent itemsets; 96 filtered rules |

These values are stored in the project artifact files and should be reconciled with the report before submission.

---

## AI-assisted critique and revision process

Each project includes a critique log. The review prompt asks an AI assistant to act as a rigorous expert reviewer in the relevant methodology.

## Deployment and operational handoff

The classification projects include saved scikit-learn pipelines and scoring scripts.

The deployment scripts demonstrate:

- Loading the saved preprocessing and model pipeline
- Accepting a single customer record
- Returning a probability
- Applying the evaluation threshold
- Returning an operational priority label

A real production deployment would additionally require:

- API or batch-service packaging
- Input schema validation
- Authentication
- Monitoring
- Drift detection
- Calibration monitoring
- Retraining triggers
- Human review of high-impact decisions

The KDD project is an analytical knowledge-discovery workflow rather than a live prediction service. Its deployment handoff is the set of segment and association artifacts that can be reviewed by marketing or merchandising teams.

---

