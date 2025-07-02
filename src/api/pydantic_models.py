from pydantic import BaseModel

class CustomerRequest(BaseModel):
    # Add all features your model expects, e.g.:
    Amount: float
    Value: float
    Total_Transaction_Amount: float
    Avg_Transaction_Amount: float
    Transaction_Count: float
    Std_Transaction_Amount: float
    Transaction_Hour: float
    Transaction_Day: float
    Transaction_Month: float
    Transaction_Year: float
    Recency: float
    Frequency: float
    Monetary: float
    # Add all other required features...

class PredictionResponse(BaseModel):
    risk_probability: float