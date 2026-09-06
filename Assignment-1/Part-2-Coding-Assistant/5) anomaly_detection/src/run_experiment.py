import argparse, json
from pathlib import Path
import numpy as np, pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.metrics import average_precision_score, roc_auc_score

def main():
    p=argparse.ArgumentParser(); p.add_argument('--data'); p.add_argument('--output',required=True); a=p.parse_args(); out=Path(a.output); out.mkdir(parents=True,exist_ok=True); data=Path(a.data); rng=np.random.default_rng(42); n=10000
    if data.exists(): df=pd.read_csv(data)
    else:
        y=(rng.random(n)<.035).astype(int); X=rng.normal(size=(n,6)); X[y==1]+=rng.normal(3,1,(y.sum(),6)); df=pd.DataFrame(X,columns=[f'signal_{i}' for i in range(6)]); df['anomaly']=y; data.parent.mkdir(parents=True,exist_ok=True); df.to_csv(data,index=False)
    X=df.drop(columns=['anomaly']); y=df['anomaly']; model=IsolationForest(contamination=float(y.mean()),random_state=42).fit(X); score=-model.score_samples(X); result={'model':'Isolation Forest','pr_auc':round(float(average_precision_score(y,score)),4),'roc_auc':round(float(roc_auc_score(y,score)),4),'anomaly_rate':round(float(y.mean()),4)}; pd.DataFrame([result]).to_csv(out/'model-comparison.csv',index=False); (out/'results-summary.json').write_text(json.dumps(result,indent=2)); print(result)
if __name__=='__main__': main()
