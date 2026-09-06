# Association Mining Experiment Summary

## Objective

Discover item relationships in synthetic grocery baskets and compare two transparent pair-rule implementations under the same support threshold.

## Dataset and audit

The benchmark contains 10,000 synthetic transactions generated with seed 42. The audit checks transaction count, unique items, average basket size, empty baskets, duplicate items, and basket representation. The data is not a redistribution of the original Instacart dataset.

## Methods and verified results

Apriori-style candidate enumeration is compared with an ECLAT reference implementation. Both use minimum support `0.035` and maximum itemset length two.

| Algorithm | Rules | Highest lift |
|---|---:|---:|
| Apriori-style | **45** | **0.9377** |
| ECLAT reference | **45** | **0.9377** |

The Apriori-style workflow was retained as the documented selected workflow because its candidate-generation steps are straightforward to inspect. The exact algorithm comparison is in `artifacts/algorithm-comparison.csv`.

## Evidence artifacts

- `apriori-rules.csv` contains support, confidence, and lift for the Apriori-style output.
- `eclat-rules.csv` provides the reference output for reconciliation.
- `algorithm-comparison.csv` compares rule counts, highest lift, and runtime.
- `top-rules.png` visualizes the highest-lift rules.
- `results-summary.json` records thresholds, audit values, metrics, artifacts, and limitations.

## Interpretation and limitations

Rules describe observed co-occurrence, not preference, causation, or guaranteed cross-selling response. Synthetic transactions may not represent real shopping behavior. High-lift rules should be checked for support, stability, seasonality, product availability, privacy implications, and business value before any controlled recommendation test.

## Reproducibility

Run `python src/run_experiment.py --data data/transactions.json --output artifacts`. The notebook audits baskets, runs the command, displays the rule comparison and figure, and reconciles the rule count with the JSON summary.

## AI assistance

The AI coding assistant supported experiment design, implementation, debugging, visualization, and documentation. The conclusions were checked against the executed CSV, PNG, and JSON artifacts.
