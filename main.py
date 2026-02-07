from fastapi import FastAPI
from pydantic import BaseModel
import os
from sqlalchemy import create_engine

app = FastAPI()

# This reads from the .env variables injected by Docker
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

# This defines what the 'input' to our model looks like
class Transaction(BaseModel):
    transaction_id: str
    amount: float

@app.get("/health")
def health():
    return {"status": "connected", "project": os.getenv("PROJECT_NAME")}

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




