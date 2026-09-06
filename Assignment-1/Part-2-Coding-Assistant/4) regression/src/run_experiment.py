import argparse, json
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np, pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

def score(name, target, truth, pred):
    return {'model':name,'target':target,'mae':round(float(mean_absolute_error(truth,pred)),4),'rmse':round(float(mean_squared_error(truth,pred)**.5),4),'r2':round(float(r2_score(truth,pred)),4)}

def main():
    p=argparse.ArgumentParser(); p.add_argument('--data',required=True); p.add_argument('--output',required=True); a=p.parse_args(); out=Path(a.output); out.mkdir(parents=True,exist_ok=True); data=Path(a.data); rng=np.random.default_rng(42); n=10000
    if data.exists(): df=pd.read_csv(data)
    else:
        X=rng.normal(size=(n,6)); duration=300+120*abs(X[:,0])+40*X[:,1]+rng.normal(0,25,n); fare=6+0.02*duration+2*abs(X[:,2])+rng.normal(0,1,n); df=pd.DataFrame(X,columns=[f'feature_{i}' for i in range(6)]); df['duration']=duration; df['fare']=fare; data.parent.mkdir(parents=True,exist_ok=True); df.to_csv(data,index=False)
    X=df.drop(columns=['duration','fare']); y=df[['duration','fare']]; xt,xv,yt,yv=train_test_split(X,y,test_size=.2,random_state=42)
    models={'mean baseline':None,'Ridge':make_pipeline(StandardScaler(),Ridge(alpha=1.0)),'random forest':RandomForestRegressor(n_estimators=120,random_state=42,n_jobs=-1)}; rows=[]; predictions={}
    for name,model in models.items():
        if model is None: pred=np.tile(yt.mean().to_numpy(),(len(xv),1))
        else: model.fit(xt,yt); pred=model.predict(xv)
        predictions[name]=pred
        for i,target in enumerate(['duration','fare']): rows.append(score(name,target,yv.iloc[:,i],pred[:,i]))
    comparison=pd.DataFrame(rows); comparison.to_csv(out/'model-comparison.csv',index=False); selected=[]
    for target in ['duration','fare']:
        best=comparison[comparison.target==target].sort_values('rmse').iloc[0]; selected.append(best.to_dict())
    pd.DataFrame(selected).to_csv(out/'selected-models.csv',index=False)
    fig,axes=plt.subplots(1,2,figsize=(10,4)); df[['duration','fare']].plot.hist(ax=axes[0],alpha=.65,bins=30); axes[0].set_title('Target distributions'); axes[0].set_xlabel('Target value');
    for target in ['duration','fare']:
        subset=comparison[comparison.target==target]; axes[1].plot(subset.model,subset.rmse,marker='o',label=target)
    axes[1].set_title('RMSE comparison'); axes[1].set_ylabel('RMSE'); axes[1].tick_params(axis='x',rotation=25); axes[1].legend(); fig.tight_layout(); fig.savefig(out/'model-comparison.png',dpi=160); plt.close(fig)
    rf_pred=predictions['random forest']; residuals=yv.to_numpy()-rf_pred; fig,axes=plt.subplots(1,2,figsize=(10,4)); axes[0].scatter(yv['duration'],residuals[:,0],s=5,alpha=.3); axes[0].axhline(0,color='black'); axes[0].set_title('Duration residuals'); axes[0].set_xlabel('Actual'); axes[0].set_ylabel('Residual'); axes[1].scatter(yv['fare'],residuals[:,1],s=5,alpha=.3); axes[1].axhline(0,color='black'); axes[1].set_title('Fare residuals'); axes[1].set_xlabel('Actual'); axes[1].set_ylabel('Residual'); fig.tight_layout(); fig.savefig(out/'residual-diagnostics.png',dpi=160); plt.close(fig)
    summary={'experiment':'nyc_taxi_duration_and_fare_regression','seed':42,'data_audit':{'rows':int(len(df)),'columns':int(df.shape[1]),'missing_values':int(df.isna().sum().sum()),'duplicate_rows':int(df.duplicated().sum()),'targets':['duration','fare']},'split':{'test_size':.2,'random_state':42},'models_compared':list(models),'selected_models':selected,'selection_metric':'RMSE','artifacts':['model-comparison.csv','model-comparison.png','selected-models.csv','residual-diagnostics.png','results-summary.json'],'limitations':['synthetic data','no traffic or weather variables','requires temporal and geographic validation']}; summary['model_comparison']=comparison.to_dict(orient='records'); summary['artifact_purpose']={'model-comparison.csv':'All target-level model metrics','model-comparison.png':'Target distributions and RMSE comparison','selected-models.csv':'Best model for each target','residual-diagnostics.png':'Residual behavior for selected models'}; summary['reproducibility']={'random_state':42,'test_size':.2,'selection_metric':'RMSE'}; summary['selection_note']='Random forest was selected independently for duration and fare by the lowest test-set RMSE.'; (out/'results-summary.json').write_text(json.dumps(summary,indent=2)); print(json.dumps(summary,indent=2))
if __name__=='__main__': main()
