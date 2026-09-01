# Prompt Engineering Record


## 1. Role, objective, and constraints

> Act as a senior data scientist and reproducible-ML engineer. Build a customer-segmentation experiment using `Mall_Customers.csv`. Follow a compact CRISP-DM workflow. Compare K-Means, Ward hierarchical clustering, and DBSCAN using age, annual income, and spending score. Do not use CustomerID as a feature. Do not use gender to construct clusters; retain it only for descriptive auditing. Use a fixed seed of 42, avoid data leakage, and save every reported metric and figure as an artifact. Do not invent results—derive every conclusion from executed code.

**Technique:** role prompting, context grounding, and constraint specification.

## 2. Data audit

> Inspect the dataset before modeling. Report its shape, schema, missing values, duplicate rows, duplicate customer IDs, categorical values, and numeric ranges. Identify identifier columns and explain which features should and should not influence clustering. Return a concise audit plus executable validation checks that fail clearly if the expected schema is absent.

**Technique:** staged decomposition and evidence requirements.

## 3. Experiment design

> Design a fair comparison among K-Means, Ward hierarchical clustering, and DBSCAN. Standardize the three selected numeric features. Evaluate K-Means and hierarchical clustering for k=2 through k=10. Tune DBSCAN over a reasonable eps/min_samples grid. Report silhouette, Davies–Bouldin, Calinski–Harabasz, number of clusters, and coverage. For DBSCAN, exclude noise only when mathematically required and always report the excluded proportion beside the metric.

**Technique:** output contract and metric-definition constraints.

## 4. Implementation

> Implement the experiment as one reproducible Python command-line script. Inputs must be supplied through `--data` and outputs through `--output`. Save model-comparison.csv, cluster-profiles.csv, customers-with-clusters.csv, results-summary.json, and publication-quality PNG figures. Use deterministic K-Means initialization and keep plotting separate from selection logic.

**Technique:** explicit deliverables and reproducibility contract.

## 5. Adversarial metric audit

> Critique the model-selection results as a skeptical reviewer. Check whether any method appears stronger only because its metric was calculated on a favorable subset. Specifically inspect DBSCAN noise coverage, sensitivity to cluster count, and whether the selected method assigns all customers. Reject any conclusion that compares non-equivalent metric populations without qualification.

**Technique:** adversarial self-critique and evidence reconciliation.

## 6. Interpretation

> Profile the selected clusters using customer counts and mean age, income, and spending score. Create concise descriptive persona names based only on those cluster averages. Do not claim personality, intent, causation, or future behavior. Explain one plausible business use for each segment while labeling it as a hypothesis requiring campaign validation.

**Technique:** bounded interpretation and responsible-AI constraint.

## 7. Visualization audit

> Generate and inspect: a data overview, elbow and silhouette comparison, Ward dendrogram, income-versus-spending cluster plot, PCA view, and normalized persona heatmap. Verify that titles, axes, legends, labels, and units are readable. Ensure PCA is described as a visualization rather than evidence that the original data is intrinsically two-dimensional.

**Technique:** visual output contract and semantic verification.

## 8. Reproducibility and documentation

> Write a GitHub README using only verified outputs. Include the dataset source, data audit, methods, model-selection tradeoff, final profiles, limitations, setup commands, repository structure, AI-assistance disclosure, and a placeholder for a YouTube walkthrough. Do not report a metric unless it exists in the generated CSV or JSON artifact.

**Technique:** provenance constraint and publication-ready formatting.

## 9. Final consistency check

> Perform a final repository audit. Re-run the experiment from the documented command, confirm that every README image and file link resolves, reconcile README numbers with results-summary.json and the CSV files, and list any remaining manual steps. Treat discrepancies as defects and correct them before declaring the project complete.

**Technique:** iterative refinement and completion criteria.

