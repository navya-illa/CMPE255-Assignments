# Prompt Engineering Record — Association Mining

## 1. Role, objective, and constraints
> Act as a senior data scientist and reproducible data-mining engineer. Build an Instacart-style market-basket analysis with fixed seed 42 and do not interpret co-occurrence as causation.
## 2. Data audit
> Report transaction count, unique items, basket sizes, item frequencies, duplicate items, empty baskets, missing values, and basket representation.
## 3. Experiment design
> Compare Apriori and ECLAT with documented support, confidence, lift, and maximum-itemset thresholds. Report itemsets, rules, support, confidence, lift, and runtime.
## 4. Implementation
> Use reproducible `--data` and `--output` scripts. Save itemsets, rules, algorithm comparisons, visualizations, and JSON results.
## 5. Adversarial metric audit
> Check whether lift has enough support, confidence is inflated by popular items, rare rules are stable, and both algorithms use identical thresholds.
## 6. Interpretation
> Treat rules as co-occurrence only. Do not claim preference, causation, or guaranteed cross-selling success; recommend controlled testing.
## 7. Visualization audit
> Inspect item-frequency, basket-size, algorithm-comparison, and top-rule figures for readable labels and non-causal interpretation.
## 8. Reproducibility and documentation
> Write README, report, notebook, setup, limitations, references, and AI disclosure from verified artifacts only.
## 9. Final consistency check
> Re-run commands, verify links and images, reconcile rule counts and lifts with CSV/JSON artifacts, and correct discrepancies.
