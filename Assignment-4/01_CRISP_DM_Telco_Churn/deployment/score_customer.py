import joblib, pandas as pd

def score_customer(record: dict, model_path="telco_churn_pipeline.joblib"):
    model = joblib.load(model_path)
    frame = pd.DataFrame([record])
    probability = float(model.predict_proba(frame)[:, 1][0])
    return {"churn_probability": probability, "priority": "high" if probability >= .70 else "standard"}

if __name__ == "__main__":
    example = {"gender":"Female", "SeniorCitizen":"0", "Partner":"Yes", "Dependents":"No", "tenure":12,
               "PhoneService":"Yes", "MultipleLines":"No", "InternetService":"Fiber optic", "OnlineSecurity":"No",
               "OnlineBackup":"No", "DeviceProtection":"No", "TechSupport":"No", "StreamingTV":"No",
               "StreamingMovies":"No", "Contract":"Month-to-month", "PaperlessBilling":"Yes", "PaymentMethod":"Electronic check",
               "MonthlyCharges":80.0, "TotalCharges":960.0}
    print(score_customer(example))
