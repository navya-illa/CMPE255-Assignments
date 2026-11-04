# Colab source for CRISP-DM Telco Customer Churn

import io, os, requests, joblib, numpy as np, pandas as pd
import matplotlib.pyplot as plt, seaborn as sns
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, roc_auc_score, average_precision_score, confusion_matrix, RocCurveDisplay, PrecisionRecallDisplay

# Business understanding: target=Churn, success=high recall at a defined outreach budget.
url = "https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/data/Telco-Customer-Churn.csv"
df = pd.read_csv(io.BytesIO(requests.get(url, timeout=30).content))
df = df.replace({"No internet service":"No", "No phone service":"No"})
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
df["SeniorCitizen"] = df["SeniorCitizen"].astype(str)
df = df.drop(columns=["customerID"])
df["Churn"] = (df["Churn"] == "Yes").astype(int)

# Data understanding
display(df.head())
display(df.isna().sum().sort_values(ascending=False).head())
display(df["Churn"].value_counts(normalize=True))
sns.countplot(data=df, x="Churn"); plt.title("Class balance"); plt.show()

# Data preparation: split before fitting preprocessing to avoid leakage.
X, y = df.drop(columns="Churn"), df["Churn"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2, stratify=y, random_state=42)
num = X.select_dtypes(include=np.number).columns.tolist()
cat = X.select_dtypes(exclude=np.number).columns.tolist()
preprocess = ColumnTransformer([("num", Pipeline([("impute", SimpleImputer(strategy="median")), ("scale", StandardScaler())]), num),
                                ("cat", Pipeline([("impute", SimpleImputer(strategy="most_frequent")), ("onehot", OneHotEncoder(handle_unknown="ignore"))]), cat)])

# Modeling and cross-validation
models = {
    "logistic": LogisticRegression(max_iter=2000, class_weight="balanced"),
    "random_forest": RandomForestClassifier(n_estimators=300, min_samples_leaf=5, class_weight="balanced", random_state=42, n_jobs=-1)
}
results = []
for name, model in models.items():
    pipe = Pipeline([("prep", preprocess), ("model", model)])
    cv = cross_val_score(pipe, X_train, y_train, cv=StratifiedKFold(5, shuffle=True, random_state=42), scoring="roc_auc", n_jobs=-1)
    pipe.fit(X_train, y_train)
    p = pipe.predict_proba(X_test)[:,1]
    results.append({"model":name, "cv_auc_mean":cv.mean(), "test_auc":roc_auc_score(y_test,p), "test_pr_auc":average_precision_score(y_test,p)})
display(pd.DataFrame(results))

best = Pipeline([("prep", preprocess), ("model", LogisticRegression(max_iter=2000, class_weight="balanced"))]).fit(X_train, y_train)
prob = best.predict_proba(X_test)[:,1]
threshold = np.quantile(prob, .70)  # outreach top 30%; document this policy explicitly
pred = (prob >= threshold).astype(int)
print(classification_report(y_test, pred))
RocCurveDisplay.from_predictions(y_test, prob); plt.show()
PrecisionRecallDisplay.from_predictions(y_test, prob); plt.show()

os.makedirs("deployment", exist_ok=True)
joblib.dump(best, "deployment/telco_churn_pipeline.joblib")
print("Saved deployment/telco_churn_pipeline.joblib")
