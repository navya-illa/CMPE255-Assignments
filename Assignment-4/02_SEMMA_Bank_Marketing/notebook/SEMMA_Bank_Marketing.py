# Colab source for SEMMA Bank Marketing
import io, requests, numpy as np, pandas as pd, matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, HistGradientBoostingClassifier
from sklearn.metrics import roc_auc_score, average_precision_score, classification_report, RocCurveDisplay, PrecisionRecallDisplay

# SAMPLE: define population and reproducible holdout.
url = "https://archive.ics.uci.edu/static/public/222/bank+marketing.zip"
import zipfile
z = zipfile.ZipFile(io.BytesIO(requests.get(url, timeout=30).content))
name = [n for n in z.namelist() if n.endswith("bank-full.csv")][0]
df = pd.read_csv(z.open(name), sep=";")
df = df.replace("unknown", np.nan)
df["y"] = (df["y"] == "yes").astype(int)
X, y = df.drop(columns="y"), df["y"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2, stratify=y, random_state=42)

# EXPLORE: distributions, missing values, imbalance, and candidate relationships.
display(df.head()); display(df["y"].value_counts(normalize=True)); display(df.isna().mean().sort_values(ascending=False).head())

# MODIFY: explicit transformations are fitted only on training folds through Pipeline.
num = X.select_dtypes(include=np.number).columns.tolist(); cat = X.select_dtypes(exclude=np.number).columns.tolist()
prep = ColumnTransformer([("num", Pipeline([("impute", SimpleImputer(strategy="median")), ("scale", StandardScaler())]), num),
                          ("cat", Pipeline([("impute", SimpleImputer(strategy="most_frequent")), ("onehot", OneHotEncoder(handle_unknown="ignore", sparse_output=False))]), cat)])

# MODEL: compare interpretable and nonlinear candidates.
models = {"logistic": LogisticRegression(max_iter=2000, class_weight="balanced"),
          "random_forest": RandomForestClassifier(n_estimators=250, min_samples_leaf=4, class_weight="balanced", random_state=42, n_jobs=-1),
          "hist_gradient_boosting": HistGradientBoostingClassifier(max_iter=200, random_state=42)}
rows=[]
for name, estimator in models.items():
    pipe = Pipeline([("prep", prep), ("model", estimator)])
    cv = cross_val_score(pipe, X_train, y_train, cv=StratifiedKFold(5, shuffle=True, random_state=42), scoring="roc_auc", n_jobs=-1)
    pipe.fit(X_train, y_train); prob = pipe.predict_proba(X_test)[:,1] if hasattr(pipe[-1], "predict_proba") else pipe.decision_function(X_test)
    rows.append({"model":name, "cv_auc":cv.mean(), "test_auc":roc_auc_score(y_test, prob), "test_pr_auc":average_precision_score(y_test, prob)})
display(pd.DataFrame(rows))

# ASSESS: choose a threshold with the campaign capacity documented.
final = Pipeline([("prep", prep), ("model", LogisticRegression(max_iter=2000, class_weight="balanced"))]).fit(X_train, y_train)
prob = final.predict_proba(X_test)[:,1]; threshold = np.quantile(prob, .80); pred = (prob >= threshold).astype(int)
print(classification_report(y_test, pred)); RocCurveDisplay.from_predictions(y_test, prob); plt.show(); PrecisionRecallDisplay.from_predictions(y_test, prob); plt.show()
