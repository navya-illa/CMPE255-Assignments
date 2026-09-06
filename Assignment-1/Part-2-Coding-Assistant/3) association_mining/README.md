# Association Mining — Market Basket Analysis

This experiment solves an association-mining problem using Instacart-style synthetic grocery transactions. It compares Apriori-style rule generation with documented support, confidence, and lift calculations.

## Method

The workflow audits transactions and basket sizes, generates frequent item pairs, ranks rules by lift, and exports rules and summary metrics. Association describes co-occurrence; it does not establish causation.

## Reproduce

```bash
python src/run_experiment.py --data data/transactions.json --output artifacts
```

The notebook, report, prompt record, requirements, and exported artifacts are stored in this folder.

## References and disclosure

The reference example is [Data Science Examples](https://github.com/dlmastery/data_science_examples). Agrawal and Srikant (1994) describe association-rule mining. The AI assistant supported design, implementation, debugging, and documentation; results were checked against executed artifacts.
