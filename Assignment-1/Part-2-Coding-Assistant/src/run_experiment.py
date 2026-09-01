"""Reproducible clustering experiment for the Mall Customers dataset."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering, DBSCAN, KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import (
    calinski_harabasz_score,
    davies_bouldin_score,
    silhouette_score,
)
from sklearn.preprocessing import StandardScaler

SEED = 42
FEATURES = ["Age", "Annual Income (k$)", "Spending Score (1-100)"]


def evaluate(X: np.ndarray, labels: np.ndarray) -> dict[str, float | int]:
    """Return internal clustering metrics, excluding DBSCAN noise points."""
    mask = labels != -1
    X_eval, labels_eval = X[mask], labels[mask]
    n_clusters = len(set(labels_eval))
    if n_clusters < 2 or len(X_eval) <= n_clusters:
        return {
            "n_clusters": n_clusters,
            "coverage": float(mask.mean()),
            "silhouette": np.nan,
            "davies_bouldin": np.nan,
            "calinski_harabasz": np.nan,
        }
    return {
        "n_clusters": n_clusters,
        "coverage": float(mask.mean()),
        "silhouette": float(silhouette_score(X_eval, labels_eval)),
        "davies_bouldin": float(davies_bouldin_score(X_eval, labels_eval)),
        "calinski_harabasz": float(calinski_harabasz_score(X_eval, labels_eval)),
    }


def persona_name(row: pd.Series) -> str:
    """Convert cluster means into concise, descriptive—not causal—labels."""
    age_value = row["Age"]
    income_value = row["Annual Income (k$)"]
    spending_value = row["Spending Score (1-100)"]
    age = "Young" if age_value < 35 else "Mature" if age_value >= 45 else "Midlife"
    income = "affluent" if income_value >= 70 else "budget" if income_value <= 40 else "mid-income"
    behavior = "enthusiasts" if spending_value >= 60 else "cautious" if spending_value <= 35 else "mainstream"
    return f"{age} {income} {behavior}"


def main(data_path: Path, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    sns.set_theme(style="whitegrid", context="talk")

    df = pd.read_csv(data_path)
    expected = {"CustomerID", "Gender", *FEATURES}
    missing_columns = expected.difference(df.columns)
    if missing_columns:
        raise ValueError(f"Missing required columns: {sorted(missing_columns)}")
    if df.empty:
        raise ValueError("Dataset is empty")

    audit = {
        "rows": int(len(df)),
        "columns": int(df.shape[1]),
        "missing_values": int(df.isna().sum().sum()),
        "duplicate_rows": int(df.duplicated().sum()),
        "duplicate_customer_ids": int(df["CustomerID"].duplicated().sum()),
    }

    X_raw = df[FEATURES].copy()
    scaler = StandardScaler()
    X = scaler.fit_transform(X_raw)

    # Evaluate K-Means and Ward hierarchical clustering for k=2,...,10.
    rows: list[dict[str, float | int | str]] = []
    inertia_rows = []
    for k in range(2, 11):
        kmeans = KMeans(n_clusters=k, random_state=SEED, n_init=20)
        k_labels = kmeans.fit_predict(X)
        rows.append({"model": "K-Means", "parameter": f"k={k}", **evaluate(X, k_labels)})
        inertia_rows.append({"k": k, "inertia": float(kmeans.inertia_)})

        ward = AgglomerativeClustering(n_clusters=k, linkage="ward")
        h_labels = ward.fit_predict(X)
        rows.append({"model": "Hierarchical (Ward)", "parameter": f"k={k}", **evaluate(X, h_labels)})

    # DBSCAN uses a coverage-aware selection criterion so high-noise solutions
    # cannot win purely by discarding difficult customers.
    dbscan_candidates = []
    for eps in np.arange(0.30, 1.31, 0.05):
        for min_samples in (3, 4, 5, 6, 8, 10):
            labels = DBSCAN(eps=float(eps), min_samples=min_samples).fit_predict(X)
            metrics = evaluate(X, labels)
            if 2 <= metrics["n_clusters"] <= 10 and not np.isnan(metrics["silhouette"]):
                coverage_adjusted = float(metrics["silhouette"] * metrics["coverage"])
                dbscan_candidates.append(
                    {
                        "model": "DBSCAN",
                        "parameter": f"eps={eps:.2f}, min_samples={min_samples}",
                        **metrics,
                        "coverage_adjusted_silhouette": coverage_adjusted,
                        "labels": labels,
                    }
                )
    best_dbscan = max(dbscan_candidates, key=lambda row: row["coverage_adjusted_silhouette"])
    rows.append({key: value for key, value in best_dbscan.items() if key != "labels"})

    comparison = pd.DataFrame(rows)
    comparison["coverage_adjusted_silhouette"] = comparison.get(
        "coverage_adjusted_silhouette", comparison["silhouette"] * comparison["coverage"]
    ).fillna(comparison["silhouette"] * comparison["coverage"])
    comparison.to_csv(output_dir / "model-comparison.csv", index=False)

    # Select the best K-Means solution for customer assignment and personas.
    kmeans_rows = comparison[comparison["model"] == "K-Means"]
    best_k = int(kmeans_rows.loc[kmeans_rows["silhouette"].idxmax(), "parameter"].split("=")[1])
    final_model = KMeans(n_clusters=best_k, random_state=SEED, n_init=20)
    labels = final_model.fit_predict(X)
    df["Cluster"] = labels

    profiles = (
        df.groupby("Cluster")
        .agg(
            Customers=("CustomerID", "count"),
            Mean_Age=("Age", "mean"),
            Mean_Income_k=("Annual Income (k$)", "mean"),
            Mean_Spending_Score=("Spending Score (1-100)", "mean"),
            Female_Share=("Gender", lambda values: (values == "Female").mean()),
        )
        .reset_index()
    )
    centers = df.groupby("Cluster")[FEATURES].mean()
    profiles["Persona"] = [persona_name(centers.loc[c]) for c in profiles["Cluster"]]
    profiles.to_csv(output_dir / "cluster-profiles.csv", index=False)
    df.to_csv(output_dir / "customers-with-clusters.csv", index=False)

    # Figure 1: data overview.
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    sns.countplot(data=df, x="Gender", hue="Gender", palette="Set2", legend=False, ax=axes[0])
    axes[0].set_title("Customer count by gender")
    axes[0].set_ylabel("Customers")
    sns.scatterplot(
        data=df,
        x="Annual Income (k$)",
        y="Spending Score (1-100)",
        hue="Age",
        palette="viridis",
        s=75,
        ax=axes[1],
    )
    axes[1].set_title("Income, spending and age")
    fig.tight_layout()
    fig.savefig(output_dir / "data-overview.png", dpi=180, bbox_inches="tight")
    plt.close(fig)

    # Figure 2: model selection.
    inertia = pd.DataFrame(inertia_rows)
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    axes[0].plot(inertia["k"], inertia["inertia"], marker="o", color="#2563eb")
    axes[0].set(title="K-Means elbow curve", xlabel="Number of clusters (k)", ylabel="Inertia")
    for model, group in comparison[comparison["model"] != "DBSCAN"].groupby("model"):
        ks = group["parameter"].str.extract(r"(\d+)")[0].astype(int)
        axes[1].plot(ks, group["silhouette"], marker="o", label=model)
    axes[1].axvline(best_k, linestyle="--", color="#ef4444", label=f"Selected k={best_k}")
    axes[1].set(title="Silhouette comparison", xlabel="Number of clusters (k)", ylabel="Silhouette score")
    axes[1].legend(fontsize=10)
    fig.tight_layout()
    fig.savefig(output_dir / "model-selection.png", dpi=180, bbox_inches="tight")
    plt.close(fig)

    # Figure 3: hierarchical structure.
    fig, ax = plt.subplots(figsize=(13, 6))
    dendrogram(linkage(X, method="ward"), truncate_mode="lastp", p=24, leaf_rotation=45, ax=ax)
    ax.set(title="Ward hierarchical-clustering dendrogram", xlabel="Merged customer groups", ylabel="Distance")
    fig.tight_layout()
    fig.savefig(output_dir / "hierarchical-dendrogram.png", dpi=180, bbox_inches="tight")
    plt.close(fig)

    # Figure 4: final segments in business space and PCA space.
    pca = PCA(n_components=2, random_state=SEED)
    coords = pca.fit_transform(X)
    plot_df = df.copy()
    plot_df["PC1"], plot_df["PC2"] = coords[:, 0], coords[:, 1]
    plot_df["ClusterLabel"] = plot_df["Cluster"].map(lambda x: f"Cluster {x}")
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    sns.scatterplot(
        data=plot_df,
        x="Annual Income (k$)",
        y="Spending Score (1-100)",
        hue="ClusterLabel",
        palette="tab10",
        s=85,
        ax=axes[0],
    )
    axes[0].set_title("Final customer segments")
    sns.scatterplot(data=plot_df, x="PC1", y="PC2", hue="ClusterLabel", palette="tab10", s=85, ax=axes[1])
    axes[1].set_title(f"PCA view ({pca.explained_variance_ratio_.sum():.1%} variance)")
    for ax in axes:
        ax.legend(fontsize=8, title=None)
    fig.tight_layout()
    fig.savefig(output_dir / "customer-segments.png", dpi=150, bbox_inches="tight")
    plt.close(fig)

    # Figure 5: normalized persona heatmap.
    heatmap_data = profiles.set_index("Persona")[["Mean_Age", "Mean_Income_k", "Mean_Spending_Score"]]
    normalized = (heatmap_data - heatmap_data.mean()) / heatmap_data.std(ddof=0)
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(normalized, annot=heatmap_data.round(1), fmt="", cmap="vlag", center=0, ax=ax)
    ax.set_title("Customer personas (values shown; color indicates relative level)")
    ax.set_xticklabels(["Age", "Annual income (k$)", "Spending score"], rotation=0)
    ax.set_xlabel("")
    ax.set_ylabel("")
    fig.tight_layout()
    fig.savefig(output_dir / "cluster-personas.png", dpi=180, bbox_inches="tight")
    plt.close(fig)

    best_kmeans = kmeans_rows.loc[kmeans_rows["silhouette"].idxmax()]
    best_hierarchical = comparison[comparison["model"] == "Hierarchical (Ward)"].sort_values("silhouette", ascending=False).iloc[0]
    summary = {
        "data_audit": audit,
        "features": FEATURES,
        "scaling": "StandardScaler",
        "selected_model": "K-Means",
        "selected_k": best_k,
        "kmeans_silhouette": round(float(best_kmeans["silhouette"]), 4),
        "hierarchical_best_parameter": best_hierarchical["parameter"],
        "hierarchical_best_silhouette": round(float(best_hierarchical["silhouette"]), 4),
        "dbscan_parameter": best_dbscan["parameter"],
        "dbscan_silhouette_non_noise": round(float(best_dbscan["silhouette"]), 4),
        "dbscan_coverage": round(float(best_dbscan["coverage"]), 4),
        "pca_explained_variance_2d": round(float(pca.explained_variance_ratio_.sum()), 4),
        "selection_note": "K-Means was selected for full customer assignment and interpretability; DBSCAN metrics exclude noise and are reported with coverage.",
    }
    (output_dir / "results-summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")

    print(json.dumps(summary, indent=2))
    print(f"\nArtifacts written to: {output_dir.resolve()}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=Path, default=Path("data/Mall_Customers.csv"))
    parser.add_argument("--output", type=Path, default=Path("artifacts"))
    args = parser.parse_args()
    main(args.data, args.output)
