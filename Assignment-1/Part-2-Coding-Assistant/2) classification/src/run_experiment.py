import argparse, json
from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import average_precision_score, roc_auc_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

def main():
    p=argparse.ArgumentParser(); p.add_argument('--data'); p.add_argument('--output', required=True); a=p.parse_args()
    out=Path(a.output); out.mkdir(parents=True, exist_ok=True); data=Path(a.data)
    if data.exists(): df=pd.read_csv(data); X=df.drop(columns=['churn']); y=df['churn']
    else:
        X,y=make_classification(n_samples=10000,n_features=10,n_informative=6,n_redundant=1,weights=[.8575,.1425],random_state=42)
        df=pd.DataFrame(X,columns=[f'feature_{i}' for i in range(10)]); df['churn']=y; data.parent.mkdir(parents=True,exist_ok=True); df.to_csv(data,index=False)
    xt,xv,yt,yv=train_test_split(X,y,test_size=.2,stratify=y,random_state=42)
    model=make_pipeline(StandardScaler(),LogisticRegression(max_iter=1000,random_state=42)); model.fit(xt,yt); prob=model.predict_proba(xv)[:,1]; pred=(prob>=.5).astype(int)
    result={'model':'Logistic regression','pr_auc':round(float(average_precision_score(yv,prob)),4),'roc_auc':round(float(roc_auc_score(yv,prob)),4),'f1':round(float(f1_score(yv,pred)),4),'rows':int(len(df))}
    pd.DataFrame([result]).to_csv(out/'model-comparison.csv',index=False); (out/'results-summary.json').write_text(json.dumps(result,indent=2)); print(result)
if __name__=='__main__': main()
