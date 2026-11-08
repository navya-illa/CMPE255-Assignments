# Verified Execution Results

All three source scripts were run from a clean Python environment after the leakage, threshold, output-artifact, and data-download fixes.

| Project | Verified result |
|---|---|
| CRISP-DM | Logistic regression selected; held-out ROC-AUC 0.8416; PR-AUC 0.6337; top-30% outreach recall 0.6765 |
| SEMMA | Histogram gradient boosting selected; held-out ROC-AUC 0.7927; PR-AUC 0.4512; 20% campaign-capacity recall 0.6087; duration excluded for leakage control |
| KDD | 4,338 customers; 17,138 valid multi-item invoices; best k=2; 282 frequent itemsets; 96 filtered rules |

Each project includes an artifacts/ directory containing real metrics, charts, tables, and serialized models where applicable. KDD outputs are also copied into knowledge_artifacts/.

