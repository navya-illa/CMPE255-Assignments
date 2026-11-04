# SAS/Enterprise Miner companion

1. Import `bank-full.csv` with semicolon delimiter.
2. Set `y` as the binary target and assign input/target roles.
3. Use a Sample node for train/validation/test partitions.
4. Use StatExplore or equivalent to inspect distributions and missing values.
5. Use Transform Variables or replacement nodes for numeric and categorical preparation.
6. Add Logistic Regression, Decision Tree, and Gradient Boosting nodes.
7. Compare models using ROC, lift, misclassification, and validation statistics.
8. Capture screenshots of the flow, data roles, model comparison, ROC/lift plots, and score output.

The Python notebook is the reproducible implementation; SAS screenshots should be added only after the student executes the flow personally.
