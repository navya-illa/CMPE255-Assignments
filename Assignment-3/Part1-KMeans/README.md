# Part 1: K-Means and its variations

[Open in Colab](https://colab.research.google.com/github/navya-illa/CMPE255-Assignments/blob/main/Assignment-3/Part1-KMeans/kmeans_variations.ipynb)

**Video walkthrough:** [Watch](ADD_LINK)

## What this notebook covers
1. Vanilla k-means and choosing k with the elbow method and silhouette score
2. Random vs k-means++ initialization over 30 seeds
3. MiniBatch k-means: speed vs quality on 200,000 points
4. Bisecting k-means
5. Gaussian Mixture Models (soft assignments, elliptical clusters)
6. Non-convex data (moons): k-means vs DBSCAN vs spectral clustering
7. Wine dataset: effect of feature scaling and a comparison table of methods

## Key results
- Silhouette picks k = 4 on the synthetic blobs, matching the true number of clusters.
- MiniBatch k-means was much faster than full k-means with slightly higher inertia.
- Wine clustering ARI improved from about 0.37 without scaling to about 0.90 with scaling.

## Files
- `kmeans_variations.ipynb`: the notebook with saved outputs
