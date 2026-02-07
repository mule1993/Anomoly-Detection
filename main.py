from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Anomaly Detection Service")

# This defines what the 'input' to our model looks like
class Transaction(BaseModel):
    transaction_id: str
    amount: float

@app.get("/")
def home():
    return {"status": "Model is Online", "version": "0.1.0-baseline"}

@app.post("/predict")
def predict(data: Transaction):
    # THE INFRASTRUCTURE RULE: 
    # Label everything as 0 (No Anomaly) for now.
    return {
        "transaction_id": data.transaction_id,
        "prediction": 0,
        "model_version": "baseline_constant_zero"
    }


# Automatically pulls from the .env file when run via Docker
import os
from sqlalchemy import create_engine
DB_URL = os.getenv("DATABASE_URL", "postgresql://admin:secret@localhost:5432/fraud_detection")
engine = create_engine(DB_URL)
