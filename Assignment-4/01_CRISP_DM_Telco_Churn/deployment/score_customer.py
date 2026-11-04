import json, joblib, pandas as pd
from pathlib import Path

HERE=Path(__file__).resolve().parents[1]
def score_customer(record: dict, model_path=None):
    model_path=model_path or HERE/"artifacts/telco_churn_pipeline.joblib"
    model=joblib.load(model_path); probability=float(model.predict_proba(pd.DataFrame([record]))[:,1][0])
    metrics=json.load(open(HERE/"artifacts/evaluation_metrics.json"))
    threshold=float(metrics["threshold"])
    return {"churn_probability":probability,"priority":"high" if probability>=threshold else "standard","threshold":threshold}
if __name__=="__main__":
    example={"gender":"Female","SeniorCitizen":"0","Partner":"Yes","Dependents":"No","tenure":12,"PhoneService":"Yes","MultipleLines":"No","InternetService":"Fiber optic","OnlineSecurity":"No","OnlineBackup":"No","DeviceProtection":"No","TechSupport":"No","StreamingTV":"No","StreamingMovies":"No","Contract":"Month-to-month","PaperlessBilling":"Yes","PaymentMethod":"Electronic check","MonthlyCharges":80.0,"TotalCharges":960.0}
    print(score_customer(example))

