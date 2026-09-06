# Association-Mining Prompt Engineering Record

## 1. Role, objective, and constraints

> Act as a senior data scientist and reproducible data-mining engineer. Build an Instacart-style market-basket experiment using clearly labeled synthetic transactions. Use fixed seed 42, document the basket representation, and never interpret item co-occurrence as preference or causation.

**Technique:** role prompting, context grounding, and responsible-interpretation constraints.

## 2. Data audit

> Audit transaction count, unique items, item frequencies, basket sizes, empty baskets, duplicate items within baskets, missing values, and the representation used by the algorithms. Explain how synthetic data limits generalization.

**Technique:** staged decomposition and data-quality evidence.

## 3. Experiment design

> Compare an Apriori-style candidate-generation workflow with an ECLAT reference implementation using identical minimum-support and maximum-itemset-length thresholds. Report support, confidence, lift, rule count, and runtime. Make the comparison fair and state how rules are sorted.

**Technique:** controlled comparison and output contract.

## 4. Implementation

> Implement one reproducible command-line script accepting `--data` and `--output`. Save Apriori rules, ECLAT rules, algorithm-comparison.csv, top-rules.png, results-summary.json, and any audit outputs needed to verify the claims. Ensure the two implementations can be reconciled.

**Technique:** explicit deliverables and reproducibility contract.

## 5. Adversarial metric audit

> Challenge whether high lift is supported by enough transactions, whether popular items inflate confidence, whether rare rules are stable, and whether both algorithms use identical thresholds. Reconcile rule counts and top lift with the exported CSV and JSON files.

**Technique:** adversarial review and evidence reconciliation.

## 6. Interpretation

> Describe rules as observed co-occurrence only. Do not claim customer preference, causality, or guaranteed cross-selling success. Discuss seasonality, product availability, privacy, support stability, and the need for controlled testing.

**Technique:** bounded interpretation and responsible-AI constraint.

## 7. Visualization audit

> Generate and inspect basket-size, item-frequency, algorithm-comparison, and top-rule figures where supported by the implementation. Verify readable labels and make the non-causal meaning of the visual evidence clear.

**Technique:** visual output contract and semantic verification.

## 8. Reproducibility and documentation

> Write the README, notebook, report, requirements, limitations, references, dataset-attribution note, and AI-assistance disclosure from executed outputs. The notebook must show the audit, command execution, algorithm table, top rules, visual evidence, and JSON reconciliation.

**Technique:** provenance constraint and publication-ready formatting.

## 9. Final consistency check

> Re-run the command, confirm every artifact named in results-summary.json exists, verify notebook paths and README image links, reconcile rule counts and lift values with CSV/JSON outputs, and correct discrepancies before completion.

**Technique:** iterative refinement and completion criteria.
