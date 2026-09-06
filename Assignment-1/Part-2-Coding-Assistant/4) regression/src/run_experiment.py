import argparse, json
from pathlib import Path
import numpy as np, pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

def main():
    p=argparse.ArgumentParser(); p.add_argument('--data'); p.add_argument('--output',required=True); a=p.parse_args(); out=Path(a.output); out.mkdir(parents=True,exist_ok=True); data=Path(a.data)
    rng=np.random.default_rng(42); n=10000
    if data.exists(): df=pd.read_csv(data)
    else:
        X=rng.normal(size=(n,6)); duration=300+120*abs(X[:,0])+40*X[:,1]+rng.normal(0,25,n); fare=6+0.02*duration+2*abs(X[:,2])+rng.normal(0,1,n); df=pd.DataFrame(X,columns=[f'feature_{i}' for i in range(6)]); df['duration']=duration; df['fare']=fare; data.parent.mkdir(parents=True,exist_ok=True); df.to_csv(data,index=False)
    X=df.drop(columns=['duration','fare']); xt,xv,yt,yv=train_test_split(X,df[['duration','fare']],test_size=.2,random_state=42); model=RandomForestRegressor(n_estimators=120,random_state=42,n_jobs=-1).fit(xt,yt)
    pred=model.predict(xv); result={}
    for i,name in enumerate(['duration','fare']): result[name]={'rmse':round(float(mean_squared_error(yv.iloc[:,i],pred[:,i])**.5),4),'r2':round(float(r2_score(yv.iloc[:,i],pred[:,i])),4)}
    pd.DataFrame(result).T.to_csv(out/'selected-models.csv'); (out/'results-summary.json').write_text(json.dumps(result,indent=2)); print(result)
if __name__=='__main__': main()
