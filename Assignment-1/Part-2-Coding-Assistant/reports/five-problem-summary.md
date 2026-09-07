# Five-Problem Experiment Summary

This report summarizes five separate data-mining problems solved with the support of an AI coding assistant. Each problem was implemented and evaluated independently. The metrics are not directly comparable because the problem types and evaluation measures differ.

## Results at a glance

| Problem | Selected method | Main result |
|---|---|---|
| Clustering | K-Means, k = 6 | Silhouette **0.4274**; coverage **100%** |
| Classification | Random forest | PR-AUC **0.9320**; ROC-AUC **0.9624**; F1 **0.8707** |
| Association mining | Apriori-style rule generation | **45** rules; top lift **0.9377** |
| Regression | Random forest | Duration RÂ² **0.9024**; fare RÂ² **0.5904** |
| Anomaly detection | Isolation Forest | PR-AUC **0.9908**; ROC-AUC **0.9995** |

## 1. Clustering

The Mall Customers experiment compared K-Means, Ward hierarchical clustering, and DBSCAN using age, annual income, and spending score. Six-cluster K-Means was selected because it provided full customer coverage and interpretable customer profiles.

- Selected method: K-Means with `k = 6`
- Silhouette score: `0.4274`
- Coverage: `100%`
- Detailed report: [`1) clustering/reports/experiment-summary.md`](../1%29%20clustering/reports/experiment-summary.md)
- Artifacts: [`1) clustering/artifacts/`](../1%29%20clustering/artifacts/)

## 2. Classification

The customer-churn experiment compared a majority-class baseline, logistic regression, and random forest. Random forest was selected using PR-AUC because the churn class is imbalanced.

- Selected method: Random forest
- PR-AUC: `0.9320`
- ROC-AUC: `0.9624`
- F1 score: `0.8707`
- Detailed report: [`2) classification/reports/experiment-summary.md`](../2%29%20classification/reports/experiment-summary.md)
- Artifacts: [`2) classification/artifacts/`](../2%29%20classification/artifacts/)

## 3. Association mining

The market-basket experiment generated synthetic grocery transactions and mined association rules. Rules describe item co-occurrence and should not be interpreted as proof of customer preference or causation.

- Selected method: Apriori-style rule generation
- Number of rules: `45`
- Highest lift: `0.9377`
- Detailed report: [`3) association_mining/reports/experiment-summary.md`](../3%29%20association_mining/reports/experiment-summary.md)
- Artifacts: [`3) association_mining/artifacts/`](../3%29%20association_mining/artifacts/)

## 4. Regression

The NYC taxi experiment predicted trip duration and fare using synthetic trip features. Random forest regression was used for both targets.

- Selected method: Random forest regression
- Duration R²: `0.9024`
- Fare R²: `0.5904`
- Detailed report: [`4) regression/reports/experiment-summary.md`](../4%29%20regression/reports/experiment-summary.md)
- Artifacts: [`4) regression/artifacts/`](../4%29%20regression/artifacts/)

## 5. Anomaly detection

The server-telemetry experiment evaluated Isolation Forest, Local Outlier Factor, and One-Class SVM on synthetic telemetry. The labels were used for evaluation and not for training the unsupervised detectors.

- Selected method: Isolation Forest
- PR-AUC: `0.9908`
- ROC-AUC: `0.9995`
- Detailed report: [`5) anomaly_detection/reports/experiment-summary.md`](../5%29%20anomaly_detection/reports/experiment-summary.md)
- Artifacts: [`5) anomaly_detection/artifacts/`](../5%29%20anomaly_detection/artifacts/)

## Responsible interpretation

These results demonstrate reproducible workflows rather than production-ready systems. The synthetic datasets cannot establish real-world performance. Internal metrics measure technical behavior, not business value, causation, or guaranteed future outcomes.

A real deployment would require external validation, appropriate licensing, data-quality monitoring, stability testing, fairness review where applicable, drift monitoring, controlled business evaluation, and periodic retraining.

## Reproducibility

Each numbered folder contains its own README, prompt record, requirements, data instructions, source code, notebook, report, and artifacts. The scripts use fixed random seeds and save their outputs under the corresponding `artifacts/` directory.

## AI-assistance disclosure

The AI coding assistant supported experiment design, code generation, debugging, visualization, validation, and documentation. The reported conclusions were checked against executed scripts and exported artifacts.
