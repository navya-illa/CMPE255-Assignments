# Colab/source script for CRISP-DM Telco Customer Churn
from pathlib import Path
import io, json, requests, joblib, numpy as np, pandas as pd
import matplotlib.pyplot as plt, seaborn as sns
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score, cross_val_predict
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, roc_auc_score, average_precision_score, confusion_matrix, RocCurveDisplay, PrecisionRecallDisplay, recall_score, precision_score
try:
    from IPython.display import display
except ImportError:
    def display(x): print(x)
ROOT = Path(__file__).resolve().parents[1]; ART = ROOT / "artifacts"; ART.mkdir(exist_ok=True)
url = "https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/data/Telco-Customer-Churn.csv"
r = requests.get(url, timeout=60); r.raise_for_status()
df = pd.read_csv(io.BytesIO(r.content)).replace({"No internet service":"No", "No phone service":"No"})
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
df["SeniorCitizen"] = df["SeniorCitizen"].astype(str); df = df.drop(columns=["customerID"]); df["Churn"] = (df["Churn"] == "Yes").astype(int)
display(df.head())
quality = pd.DataFrame({"missing":df.isna().sum(), "missing_pct":df.isna().mean(), "dtype":df.dtypes.astype(str)}); quality.to_csv(ART/"data_quality.csv")
df["Churn"].value_counts(normalize=True).rename("share").to_csv(ART/"target_distribution.csv")
plt.figure(figsize=(5,4)); sns.countplot(data=df,x="Churn"); plt.title("Telco churn class balance"); plt.tight_layout(); plt.savefig(ART/"class_balance.png",dpi=160); plt.close()
X,y=df.drop(columns="Churn"),df["Churn"]; X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=.2,stratify=y,random_state=42)
num=X.select_dtypes(include=np.number).columns.tolist(); cat=X.select_dtypes(exclude=np.number).columns.tolist()
preprocess=ColumnTransformer([("num",Pipeline([("impute",SimpleImputer(strategy="median")),("scale",StandardScaler())]),num),("cat",Pipeline([("impute",SimpleImputer(strategy="most_frequent")),("onehot",OneHotEncoder(handle_unknown="ignore"))]),cat)])
models={"logistic":LogisticRegression(max_iter=2000,class_weight="balanced"),"random_forest":RandomForestClassifier(n_estimators=300,min_samples_leaf=5,class_weight="balanced",random_state=42,n_jobs=-1)}
cv=StratifiedKFold(5,shuffle=True,random_state=42); rows=[]; fitted={}
for name,model in models.items():
    pipe=Pipeline([("prep",preprocess),("model",model)]); scores=cross_val_score(pipe,X_train,y_train,cv=cv,scoring="roc_auc",n_jobs=-1); pipe.fit(X_train,y_train); p=pipe.predict_proba(X_test)[:,1]
    rows.append({"model":name,"cv_auc_mean":scores.mean(),"cv_auc_std":scores.std(),"test_roc_auc":roc_auc_score(y_test,p),"test_pr_auc":average_precision_score(y_test,p)}); fitted[name]=pipe
results=pd.DataFrame(rows).sort_values("cv_auc_mean",ascending=False); results.to_csv(ART/"model_comparison.csv",index=False); display(results)
best_name=results.iloc[0]["model"]; best=fitted[best_name]
oof=cross_val_predict(Pipeline([("prep",preprocess),("model",models[best_name])]),X_train,y_train,cv=cv,method="predict_proba",n_jobs=-1)[:,1]
threshold=float(np.quantile(oof,.70)); prob=best.predict_proba(X_test)[:,1]; pred=(prob>=threshold).astype(int)
metrics={"selected_model":best_name,"outreach_fraction":.30,"threshold":threshold,"roc_auc":roc_auc_score(y_test,prob),"pr_auc":average_precision_score(y_test,prob),"precision_at_budget":precision_score(y_test,pred,zero_division=0),"recall_at_budget":recall_score(y_test,pred,zero_division=0)}
json.dump(metrics,open(ART/"evaluation_metrics.json","w"),indent=2); pd.DataFrame(classification_report(y_test,pred,output_dict=True)).T.to_csv(ART/"classification_report.csv"); joblib.dump(best,ART/"telco_churn_pipeline.joblib")
RocCurveDisplay.from_predictions(y_test,prob); plt.title(f"CRISP-DM ROC — {best_name}"); plt.tight_layout(); plt.savefig(ART/"roc_curve.png",dpi=160); plt.close()
PrecisionRecallDisplay.from_predictions(y_test,prob); plt.title(f"CRISP-DM Precision-Recall — {best_name}"); plt.tight_layout(); plt.savefig(ART/"precision_recall_curve.png",dpi=160); plt.close()
plt.figure(figsize=(4,4)); sns.heatmap(confusion_matrix(y_test,pred),annot=True,fmt="d",cmap="Blues"); plt.title("Churn decisions at outreach cutoff"); plt.xlabel("Predicted"); plt.ylabel("Actual"); plt.tight_layout(); plt.savefig(ART/"confusion_matrix.png",dpi=160); plt.close()
print(json.dumps(metrics,indent=2))

