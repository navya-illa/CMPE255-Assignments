import json, joblib, pandas as pd
from pathlib import Path
HERE=Path(__file__).resolve().parents[1]
def score_customer(record: dict, model_path=None):
    model_path=model_path or HERE/"artifacts/bank_marketing_pipeline.joblib"
    model=joblib.load(model_path); probability=float(model.predict_proba(pd.DataFrame([record]))[:,1][0])
    metrics=json.load(open(HERE/"artifacts/evaluation_metrics.json")); threshold=float(metrics["threshold"])
    return {"subscription_probability":probability,"priority":"contact" if probability>=threshold else "do_not_prioritize","threshold":threshold}
if __name__=="__main__":
    print("Pass a pre-contact bank customer dictionary to score_customer(record).")

