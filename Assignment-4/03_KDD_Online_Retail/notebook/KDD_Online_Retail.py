# Colab/source script for KDD Online Retail knowledge discovery
from pathlib import Path
import os
import io, json, requests, numpy as np, pandas as pd
import matplotlib.pyplot as plt, seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from mlxtend.frequent_patterns import apriori, association_rules
try:
    from IPython.display import display
except ImportError:
    def display(x): print(x)
ROOT=Path(__file__).resolve().parents[1]; ART=ROOT/"artifacts"; ART.mkdir(exist_ok=True)
url="https://archive.ics.uci.edu/ml/machine-learning-databases/00352/Online%20Retail.xlsx"; local_path=os.getenv("KDD_DATA_PATH")
if local_path:
    df=pd.read_excel(local_path)
else:
    r=requests.get(url,timeout=120); r.raise_for_status(); df=pd.read_excel(io.BytesIO(r.content))
raw_rows=len(df); df["InvoiceDate"]=pd.to_datetime(df["InvoiceDate"]); df["Description"]=df["Description"].astype("string").str.strip().str.upper()
df=df.dropna(subset=["CustomerID","Description"]); df=df[~df["InvoiceNo"].astype(str).str.startswith("C")]; df=df[(df["Quantity"]>0)&(df["UnitPrice"]>0)]; df["Revenue"]=df["Quantity"]*df["UnitPrice"]
pd.DataFrame({"raw_rows":[raw_rows],"clean_rows":[len(df)],"removed_rows":[raw_rows-len(df)]}).to_csv(ART/"preprocessing_summary.csv",index=False)
snapshot=df["InvoiceDate"].max()+pd.Timedelta(days=1); rfm=df.groupby("CustomerID").agg(Recency=("InvoiceDate",lambda x:(snapshot-x.max()).days),Frequency=("InvoiceNo","nunique"),Monetary=("Revenue","sum")).replace([np.inf,-np.inf],np.nan).dropna()
Z=StandardScaler().fit_transform(np.log1p(rfm)); scores=[]
for k in range(2,9):
    labels=KMeans(n_clusters=k,n_init=20,random_state=42).fit_predict(Z); scores.append((k,silhouette_score(Z,labels)))
score_df=pd.DataFrame(scores,columns=["k","silhouette"]); score_df.to_csv(ART/"cluster_silhouette_scores.csv",index=False); display(score_df)
best_k=int(score_df.loc[score_df["silhouette"].idxmax(),"k"]); model=KMeans(n_clusters=best_k,n_init=20,random_state=42); rfm["segment"]=model.fit_predict(Z); rfm.groupby("segment")[["Recency","Frequency","Monetary"]].median().to_csv(ART/"segment_profiles.csv")
plt.figure(figsize=(7,4)); sns.barplot(data=score_df,x="k",y="silhouette"); plt.title("KDD cluster selection"); plt.tight_layout(); plt.savefig(ART/"cluster_selection.png",dpi=160); plt.close()
invoice_sizes=df["InvoiceNo"].value_counts(); valid_invoices=invoice_sizes[invoice_sizes>=2].index; basket=(df[df["InvoiceNo"].isin(valid_invoices)].groupby(["InvoiceNo","Description"])["Quantity"].sum().unstack(fill_value=0).gt(0))
min_count=max(2,int(len(basket)*.01)); keep=basket.sum().loc[lambda s:s>=min_count].index; basket=basket[keep]
freq=apriori(basket,min_support=.02,use_colnames=True); rules=association_rules(freq,metric="lift",min_threshold=1.1).sort_values(["lift","confidence"],ascending=False); rules=rules[(rules["support"]>=.02)&(rules["confidence"]>=.20)]
rules[["antecedents","consequents","support","confidence","lift"]].head(100).to_csv(ART/"association_rules.csv",index=False)
json.dump({"best_k":best_k,"customers":int(len(rfm)),"valid_invoices":int(len(basket)),"frequent_itemsets":int(len(freq)),"rules":int(len(rules))},open(ART/"knowledge_summary.json","w"),indent=2)
display(rules[["antecedents","consequents","support","confidence","lift"]].head(20)); print("Artifacts written to",ART)

