# KDD: Online Retail Knowledge Discovery

## Knowledge-discovery goal

Transform transactional retail data into validated knowledge about customer groups and item co-purchases.

## Dataset

Online Retail dataset, available through Kaggle and the UCI Machine Learning Repository.

## KDD stages

1. **Selection:** define the population, time period, transactions, and discovery questions.
2. **Preprocessing:** remove cancellations and invalid records, handle missing customer IDs, and validate transaction integrity.
3. **Transformation:** create RFM features, customer-level matrices, and basket representations.
4. **Data mining:** perform clustering and association-rule mining with justified parameters.
5. **Interpretation/evaluation:** validate stability, inspect rule support/confidence/lift, profile segments, and translate patterns into actions.

## Artifacts

- `notebook/KDD_Online_Retail.ipynb`
- `report/KDD_Online_Retail_Report.md`
- `critique/critique_log.md`
- `knowledge_artifacts/segment_profiles.csv`
- `knowledge_artifacts/association_rules.csv`
- `medium/medium_article_draft.md`
- `video/walkthrough_script.md`
