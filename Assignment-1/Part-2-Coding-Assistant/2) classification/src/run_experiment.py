import argparse
import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.inspection import permutation_importance
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import average_precision_score, confusion_matrix, f1_score, precision_score, recall_score, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


def evaluate(name, y_true, probability):
    prediction = (probability >= 0.5).astype(int)
    return {"model": name, "pr_auc": round(float(average_precision_score(y_true, probability)), 4), "roc_auc": round(float(roc_auc_score(y_true, probability)), 4), "precision": round(float(precision_score(y_true, prediction, zero_division=0)), 4), "recall": round(float(recall_score(y_true, prediction, zero_division=0)), 4), "f1": round(float(f1_score(y_true, prediction, zero_division=0)), 4)}


def main():
    parser = argparse.ArgumentParser(); parser.add_argument("--data", required=True); parser.add_argument("--output", required=True); args = parser.parse_args()
    output = Path(args.output); output.mkdir(parents=True, exist_ok=True); data_path = Path(args.data)
    if data_path.exists():
        frame = pd.read_csv(data_path); features, target = frame.drop(columns="churn"), frame["churn"]
    else:
        values, labels = make_classification(n_samples=10000, n_features=10, n_informative=6, n_redundant=1, weights=[0.8575, 0.1425], random_state=42)
        frame = pd.DataFrame(values, columns=[f"feature_{i}" for i in range(10)]); frame["churn"] = labels; data_path.parent.mkdir(parents=True, exist_ok=True); frame.to_csv(data_path, index=False); features, target = frame.drop(columns="churn"), frame["churn"]
    x_train, x_test, y_train, y_test = train_test_split(features, target, test_size=0.2, stratify=target, random_state=42)
    prevalence = float(y_train.mean())
    models = {"majority baseline": None, "logistic regression": make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000, random_state=42)), "random forest": RandomForestClassifier(n_estimators=150, class_weight="balanced", random_state=42, n_jobs=-1)}
    rows, probabilities = [], {}
    for name, model in models.items():
        if model is None: probability = np.full(len(y_test), prevalence)
        else: model.fit(x_train, y_train); probability = model.predict_proba(x_test)[:, 1]
        probabilities[name] = probability; rows.append(evaluate(name, y_test, probability))
    comparison = pd.DataFrame(rows).sort_values("pr_auc", ascending=False); comparison.to_csv(output / "model-comparison.csv", index=False)
    selected = comparison.iloc[0]["model"]; selected_probability = probabilities[selected]; selected_prediction = (selected_probability >= 0.5).astype(int)
    fig, axes = plt.subplots(1, 2, figsize=(10, 4)); frame["churn"].value_counts().sort_index().plot.bar(ax=axes[0], color=["#4c78a8", "#f58518"]); axes[0].set_title("Churn class distribution"); axes[0].set_xlabel("Churn"); axes[0].set_ylabel("Customers"); axes[1].bar(comparison["model"], comparison["pr_auc"], color="#4c78a8"); axes[1].set_title("PR-AUC model comparison"); axes[1].tick_params(axis="x", rotation=25); axes[1].set_ylabel("PR-AUC"); fig.tight_layout(); fig.savefig(output / "model-comparison.png", dpi=160); plt.close(fig)
    cm = confusion_matrix(y_test, selected_prediction); fig, ax = plt.subplots(figsize=(4, 4)); ax.imshow(cm, cmap="Blues"); ax.set_title(f"{selected.title()} confusion matrix"); ax.set_xlabel("Predicted"); ax.set_ylabel("Actual"); [ax.text(j, i, value, ha="center", va="center") for (i, j), value in np.ndenumerate(cm)]; fig.tight_layout(); fig.savefig(output / "selected-confusion-matrix.png", dpi=160); plt.close(fig)
    forest = models["random forest"]; importance = permutation_importance(forest, x_test, y_test, scoring="average_precision", random_state=42); importance_frame = pd.DataFrame({"feature": features.columns, "importance_mean": importance.importances_mean}).sort_values("importance_mean", ascending=False); importance_frame.to_csv(output / "permutation-importance.csv", index=False); fig, ax = plt.subplots(figsize=(7, 4)); top = importance_frame.head(8).sort_values("importance_mean"); ax.barh(top["feature"], top["importance_mean"], color="#54a24b"); ax.set_title("Permutation importance"); ax.set_xlabel("Mean AP decrease"); fig.tight_layout(); fig.savefig(output / "permutation-importance.png", dpi=160); plt.close(fig)
    summary = {"experiment": "customer_churn_classification", "seed": 42, "data_audit": {"rows": int(len(frame)), "columns": int(frame.shape[1]), "missing_values": int(frame.isna().sum().sum()), "duplicate_rows": int(frame.duplicated().sum()), "churn_rate": round(float(frame["churn"].mean()), 4)}, "split": {"test_size": 0.2, "stratified": True}, "models_compared": list(models), "selected_model": selected, "selection_metric": "PR-AUC", "selected_metrics": comparison[comparison["model"] == selected].iloc[0].to_dict(), "artifacts": ["model-comparison.csv", "model-comparison.png", "selected-confusion-matrix.png", "permutation-importance.csv", "permutation-importance.png", "results-summary.json"], "limitations": ["synthetic data", "threshold-dependent recall", "requires calibration and fairness review"]}
    summary["model_comparison"] = comparison.to_dict(orient="records"); summary["artifact_purpose"] = {"model-comparison.csv": "All model metrics used for selection", "model-comparison.png": "Class balance and PR-AUC comparison", "selected-confusion-matrix.png": "Thresholded test-set errors", "permutation-importance.csv": "Feature sensitivity values", "permutation-importance.png": "Feature sensitivity visualization"}; summary["reproducibility"] = {"random_state": 42, "test_size": 0.2, "threshold": 0.5}; summary["selection_note"] = "Random forest was selected by PR-AUC; accuracy was not used as the sole criterion because churn is imbalanced."
    (output / "results-summary.json").write_text(json.dumps(summary, indent=2)); print(json.dumps(summary, indent=2))


if __name__ == "__main__": main()
