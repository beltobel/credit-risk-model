from fastapi import FastAPI
from pydantic import BaseModel
import mlflow.pyfunc
import pandas as pd
from src.api.pydantic_models import CustomerRequest, PredictionResponse

app = FastAPI()

# Load model from MLflow registry
MODEL_NAME = "CreditRiskBestModel"
MODEL_STAGE = "Production"
model = mlflow.pyfunc.load_model(model_uri=f"models:/{MODEL_NAME}/{MODEL_STAGE}")

@app.post("/predict", response_model=PredictionResponse)
def predict(request: CustomerRequest):
    data = pd.DataFrame([request.dict()])
    proba = model.predict(data)
    return PredictionResponse(risk_probability=float(proba[0]))