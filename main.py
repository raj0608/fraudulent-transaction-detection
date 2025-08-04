from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load saved model
model = joblib.load("fraud_detection_rf.pkl")

# Classification threshold from your tuning
THRESHOLD = 0.45  

# Request body format
class TransactionFeatures(BaseModel):
    features: list  # Expecting list of numeric features in correct order

app = FastAPI(title="Fraud Detection API")

@app.get("/")
def home():
    return {"message": "Fraud Detection API is running!"}

@app.post("/predict")
def predict(data: TransactionFeatures):
    # Convert input list to numpy array
    features_array = np.array(data.features).reshape(1, -1)
    
    # Predict probability
    prob = model.predict_proba(features_array)[0][1]
    prediction = int(prob >= THRESHOLD)
    
    return {
        "fraud_probability": float(prob),
        "is_fraud": prediction
    }
