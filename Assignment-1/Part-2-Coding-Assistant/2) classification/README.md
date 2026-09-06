# Classification — Customer Churn

This experiment solves a customer-churn classification problem using a synthetic benchmark adapted from the AutoML example. It compares a baseline and supervised models using imbalance-aware metrics.

## Method

The workflow audits the data, uses a stratified split, compares a majority baseline, logistic regression, and random forest, and selects using PR-AUC. The generated benchmark is not real customer data.

## Reproduce

```bash
python src/run_experiment.py --data data/customer_churn.csv --output artifacts
```

The notebook, report, prompt record, requirements, and exported metrics are stored in this folder.

## References and disclosure

The reference example is [Data Science Examples](https://github.com/dlmastery/data_science_examples). scikit-learn documentation was used for model evaluation. The AI assistant supported design, implementation, debugging, and documentation; results were checked against executed artifacts.
