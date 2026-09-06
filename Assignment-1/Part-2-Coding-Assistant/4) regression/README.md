# Regression — NYC Taxi Duration and Fare

This experiment solves regression problems for synthetic NYC taxi trip duration and fare. It compares a baseline and tree-based regression model using separate targets.

## Method

The workflow audits the data, prevents target leakage, evaluates duration and fare separately, and reports RMSE and R². The synthetic benchmark is not real taxi data.

## Reproduce

```bash
python src/run_experiment.py --data data/nyc_taxi.csv --output artifacts
```

The notebook, report, prompt record, requirements, and exported artifacts are stored in this folder.

## References and disclosure

The reference example is [Data Science Examples](https://github.com/dlmastery/data_science_examples). scikit-learn documentation was used for regression metrics. The AI assistant supported design, implementation, debugging, and documentation; results were checked against executed artifacts.
