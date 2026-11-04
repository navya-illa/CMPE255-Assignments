# Colab source for KDD Online Retail knowledge discovery
import io, requests, numpy as np, pandas as pd, matplotlib.pyplot as plt, seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from mlxtend.frequent_patterns import apriori, association_rules

# SELECTION: choose valid invoices and define customer/product discovery questions.
url = "https://archive.ics.uci.edu/static/public/352/online+retail.xlsx"
df = pd.read_excel(io.BytesIO(requests.get(url, timeout=60).content))
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
df = df.dropna(subset=["CustomerID", "Description"])
df = df[~df["InvoiceNo"].astype(str).str.startswith("C")]
df = df[(df["Quantity"] > 0) & (df["UnitPrice"] > 0)]
df["Revenue"] = df["Quantity"] * df["UnitPrice"]

# PREPROCESSING: validate transactional data and create customer-level features.
snapshot = df["InvoiceDate"].max() + pd.Timedelta(days=1)
rfm = df.groupby("CustomerID").agg(Recency=("InvoiceDate", lambda x: (snapshot-x.max()).days),
                                     Frequency=("InvoiceNo", "nunique"), Monetary=("Revenue", "sum"))
rfm = rfm.replace([np.inf, -np.inf], np.nan).dropna()

# TRANSFORMATION: log-transform skewed RFM features and standardize.
X = np.log1p(rfm)
Z = StandardScaler().fit_transform(X)

# DATA MINING: choose k using silhouette, then profile segments.
scores=[]
for k in range(2, 9):
    labels = KMeans(n_clusters=k, n_init=20, random_state=42).fit_predict(Z)
    scores.append((k, silhouette_score(Z, labels)))
display(pd.DataFrame(scores, columns=["k","silhouette"]))
best_k = max(scores, key=lambda x:x[1])[0]
rfm["segment"] = KMeans(n_clusters=best_k, n_init=20, random_state=42).fit_predict(Z)
display(rfm.groupby("segment")[['Recency','Frequency','Monetary']].median())

# INTERPRETATION: basket matrix and validated association rules.
basket = (df[df["InvoiceNo"].isin(df["InvoiceNo"].value_counts().loc[lambda s:s>=2].index)]
          .groupby(["InvoiceNo", "Description"])["Quantity"].sum().unstack(fill_value=0))
basket = basket.gt(0).astype(bool)
freq = apriori(basket, min_support=0.02, use_colnames=True)
rules = association_rules(freq, metric="lift", min_threshold=1.1).sort_values(["lift","confidence"], ascending=False)
display(rules[["antecedents","consequents","support","confidence","lift"]].head(20))
rfm.to_csv("segment_profiles.csv"); rules.to_csv("association_rules.csv", index=False)
