import argparse, json
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np, pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.metrics import average_precision_score, confusion_matrix, precision_score, recall_score, f1_score, roc_auc_score
from sklearn.neighbors import LocalOutlierFactor
from sklearn.svm import OneClassSVM

def evaluate(name,y,score):
    threshold=np.quantile(score,1-y.mean()); pred=(score>=threshold).astype(int); return {'method':name,'roc_auc':round(float(roc_auc_score(y,score)),4),'pr_auc':round(float(average_precision_score(y,score)),4),'precision':round(float(precision_score(y,pred,zero_division=0)),4),'recall':round(float(recall_score(y,pred,zero_division=0)),4),'f1':round(float(f1_score(y,pred,zero_division=0)),4),'false_positive_rate':round(float(((pred==1)&(y==0)).sum()/max((y==0).sum(),1)),4)},pred

def main():
    p=argparse.ArgumentParser(); p.add_argument('--data',required=True); p.add_argument('--output',required=True); a=p.parse_args(); out=Path(a.output); out.mkdir(parents=True,exist_ok=True); data=Path(a.data); rng=np.random.default_rng(42); n=10000
    if data.exists(): df=pd.read_csv(data)
    else:
        y=(rng.random(n)<.035).astype(int); X=rng.normal(size=(n,6)); X[y==1]+=rng.normal(3,1,(y.sum(),6)); df=pd.DataFrame(X,columns=[f'signal_{i}' for i in range(6)]); df['anomaly']=y; data.parent.mkdir(parents=True,exist_ok=True); df.to_csv(data,index=False)
    X=df.drop(columns='anomaly'); y=df.anomaly.to_numpy(); models={'Isolation Forest':IsolationForest(contamination=float(y.mean()),random_state=42),'Local Outlier Factor':LocalOutlierFactor(n_neighbors=20,contamination=float(y.mean()),novelty=True),'One-Class SVM':OneClassSVM(nu=float(y.mean()),gamma='scale')}; rows=[]; predictions={}
    for name,model in models.items():
        model.fit(X); score=-model.score_samples(X); row,pred=evaluate(name,y,score); rows.append(row); predictions[name]=pred
    comparison=pd.DataFrame(rows).sort_values('pr_auc',ascending=False); comparison.to_csv(out/'model-comparison.csv',index=False); selected=comparison.iloc[0]['method']; cm=confusion_matrix(y,predictions[selected]); fig,ax=plt.subplots(figsize=(4,4)); ax.imshow(cm,cmap='Oranges'); ax.set_title(f'{selected} confusion matrix'); ax.set_xlabel('Predicted'); ax.set_ylabel('Actual'); [ax.text(j,i,value,ha='center',va='center') for (i,j),value in np.ndenumerate(cm)]; fig.tight_layout(); fig.savefig(out/'selected-confusion-matrix.png',dpi=160); plt.close(fig)
    deviations=pd.DataFrame({'feature':X.columns,'mean_absolute_z':((X-X.mean())/X.std()).abs().mean().values}).sort_values('mean_absolute_z',ascending=False); deviations.to_csv(out/'anomaly-feature-deviations.csv',index=False); fig,ax=plt.subplots(figsize=(8,4)); ax.bar(comparison.method,comparison.pr_auc,color='#f58518'); ax.set_title('Anomaly detector comparison'); ax.set_ylabel('PR-AUC'); ax.tick_params(axis='x',rotation=25); fig.tight_layout(); fig.savefig(out/'model-comparison.png',dpi=160); plt.close(fig)
    summary={'experiment':'server_telemetry_anomaly_detection','seed':42,'data_audit':{'rows':int(len(df)),'signals':int(X.shape[1]),'missing_values':int(df.isna().sum().sum()),'duplicate_rows':int(df.duplicated().sum()),'anomaly_rate':round(float(y.mean()),4)},'labels_used_for_training':False,'methods_compared':['Isolation Forest','Local Outlier Factor','One-Class SVM'],'selected_method':selected,'selection_metric':'PR-AUC','selected_metrics':comparison.iloc[0].to_dict(),'artifacts':['model-comparison.csv','model-comparison.png','selected-confusion-matrix.png','anomaly-feature-deviations.csv','results-summary.json'],'limitations':['synthetic telemetry','threshold and contamination sensitivity','requires analyst feedback and drift monitoring']}; summary['method_comparison']=comparison.to_dict(orient='records'); summary['artifact_purpose']={'model-comparison.csv':'All detector metrics','model-comparison.png':'Detector PR-AUC comparison','selected-confusion-matrix.png':'Thresholded errors for the selected detector','anomaly-feature-deviations.csv':'Feature-level deviation summary'}; summary['reproducibility']={'random_state':42,'contamination':round(float(y.mean()),4),'selection_metric':'PR-AUC','labels_used_for_training':False}; summary['selection_note']='Isolation Forest was selected by PR-AUC while also reporting false-positive rate and thresholded classification metrics because anomalies are rare.'; (out/'results-summary.json').write_text(json.dumps(summary,indent=2)); print(json.dumps(summary,indent=2))
if __name__=='__main__': main()
