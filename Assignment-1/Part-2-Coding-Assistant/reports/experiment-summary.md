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



