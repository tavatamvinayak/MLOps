from fastapi import FastAPI
from pydantic import BaseModel
from predict import make_prediction

app = FastAPI()

class ChurnInput(BaseModel):
    tenure: int
    monthly_charges: float
    contract_type: str
    internet_service: str
    payment_method: str

@app.post("/predict")
async def predict_churn(input_data: ChurnInput):
    prediction = make_prediction(input_data.dict())
    return {"churn_probability": float(prediction)}