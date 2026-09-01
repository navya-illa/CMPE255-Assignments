# Experiment Summary

## Objective

Group mall customers into interpretable segments using age, annual income, and spending score while comparing partition-based, hierarchical, and density-based clustering.

## Verified findings

- The dataset contains 200 rows and five columns.
- No missing values, duplicate rows, or duplicate customer IDs were detected.
- K-Means with six clusters achieved a silhouette score of 0.4274 with 100% coverage.
- Ward hierarchical clustering with six clusters achieved 0.4201 with 100% coverage.
- The tuned DBSCAN candidate achieved 0.5158 on non-noise customers but covered only 69% of the dataset.
- K-Means was selected because it had the strongest full-coverage silhouette score and produced directly interpretable profiles.
- The two-component PCA view preserves 77.57% of standardized-feature variance and is used only for visualization.

## Interpretation

The final six groups separate affluent high spenders from affluent cautious shoppers, distinguish younger and mature mainstream groups, and identify budget-oriented high- and low-spending groups. These labels summarize observed cluster means. They do not establish customers' motivations or predict campaign response.

## Limitations

The dataset is small, cross-sectional, and lacks transaction history, recency, product preferences, geography, and outcomes. Internal cluster metrics do not demonstrate commercial value. Any marketing action based on these profiles should be evaluated through controlled experiments and fairness monitoring.

## Recommended extensions

- Test stability across seeds and bootstrap samples.
- Validate clusters on a second customer cohort.
- Add RFM transaction features when available.
- Measure downstream campaign lift rather than relying only on internal clustering metrics.
- Monitor cluster sizes and feature distributions for drift.

