# Colab/source script for SEMMA Bank Marketing
from pathlib import Path
import io, json, zipfile, requests, numpy as np, pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score, cross_val_predict
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, HistGradientBoostingClassifier
from sklearn.metrics import roc_auc_score, average_precision_score, classification_report, RocCurveDisplay, PrecisionRecallDisplay, precision_score, recall_score
try:
    from IPython.display import display
except ImportError:
    def display(x): print(x)
ROOT=Path(__file__).resolve().parents[1]; ART=ROOT/"artifacts"; ART.mkdir(exist_ok=True)
url="https://archive.ics.uci.edu/ml/machine-learning-databases/00222/bank.zip"; r=requests.get(url,timeout=60); r.raise_for_status()
z=zipfile.ZipFile(io.BytesIO(r.content)); name=[n for n in z.namelist() if n.endswith("bank-full.csv")][0]; df=pd.read_csv(z.open(name),sep=";").replace("unknown",np.nan); df["y"]=(df["y"]=="yes").astype(int)
json.dump({"excluded_features":["duration"],"reason":"duration is measured during campaign contact and is unavailable for pre-contact targeting"},open(ART/"leakage_decision.json","w"),indent=2)
df=df.drop(columns=["duration"]); X,y=df.drop(columns="y"),df["y"]; X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=.2,stratify=y,random_state=42)
display(df.head()); display(df["y"].value_counts(normalize=True)); df.isna().mean().sort_values(ascending=False).to_csv(ART/"missingness.csv"); df["y"].value_counts(normalize=True).rename("share").to_csv(ART/"target_distribution.csv")
plt.figure(figsize=(5,4)); df["y"].value_counts().plot.bar(); plt.title("Bank marketing target balance"); plt.tight_layout(); plt.savefig(ART/"class_balance.png",dpi=160); plt.close()
num=X.select_dtypes(include=np.number).columns.tolist(); cat=X.select_dtypes(exclude=np.number).columns.tolist()
prep=ColumnTransformer([("num",Pipeline([("impute",SimpleImputer(strategy="median")),("scale",StandardScaler())]),num),("cat",Pipeline([("impute",SimpleImputer(strategy="most_frequent")),("onehot",OneHotEncoder(handle_unknown="ignore",sparse_output=False))]),cat)])
models={"logistic":LogisticRegression(max_iter=2000,class_weight="balanced"),"random_forest":RandomForestClassifier(n_estimators=250,min_samples_leaf=4,class_weight="balanced",random_state=42,n_jobs=-1),"hist_gradient_boosting":HistGradientBoostingClassifier(max_iter=200,random_state=42)}
cv=StratifiedKFold(5,shuffle=True,random_state=42); rows=[]; fitted={}
for name,estimator in models.items():
    pipe=Pipeline([("prep",prep),("model",estimator)]); scores=cross_val_score(pipe,X_train,y_train,cv=cv,scoring="roc_auc",n_jobs=-1); pipe.fit(X_train,y_train); prob=pipe.predict_proba(X_test)[:,1]
    rows.append({"model":name,"cv_auc_mean":scores.mean(),"cv_auc_std":scores.std(),"test_roc_auc":roc_auc_score(y_test,prob),"test_pr_auc":average_precision_score(y_test,prob)}); fitted[name]=pipe
results=pd.DataFrame(rows).sort_values("cv_auc_mean",ascending=False); results.to_csv(ART/"model_comparison.csv",index=False); display(results)
best_name=results.iloc[0]["model"]; best=fitted[best_name]; oof=cross_val_predict(Pipeline([("prep",prep),("model",models[best_name])]),X_train,y_train,cv=cv,method="predict_proba",n_jobs=-1)[:,1]
threshold=float(np.quantile(oof,.80)); prob=best.predict_proba(X_test)[:,1]; pred=(prob>=threshold).astype(int)
metrics={"selected_model":best_name,"campaign_contact_fraction":.20,"threshold":threshold,"roc_auc":roc_auc_score(y_test,prob),"pr_auc":average_precision_score(y_test,prob),"precision_at_capacity":precision_score(y_test,pred,zero_division=0),"recall_at_capacity":recall_score(y_test,pred,zero_division=0)}
json.dump(metrics,open(ART/"evaluation_metrics.json","w"),indent=2); pd.DataFrame(classification_report(y_test,pred,output_dict=True)).T.to_csv(ART/"classification_report.csv")
import joblib; joblib.dump(best,ART/"bank_marketing_pipeline.joblib")
RocCurveDisplay.from_predictions(y_test,prob); plt.title(f"SEMMA ROC — {best_name}"); plt.tight_layout(); plt.savefig(ART/"roc_curve.png",dpi=160); plt.close()
PrecisionRecallDisplay.from_predictions(y_test,prob); plt.title(f"SEMMA Precision-Recall — {best_name}"); plt.tight_layout(); plt.savefig(ART/"precision_recall_curve.png",dpi=160); plt.close()
print(json.dumps(metrics,indent=2))

