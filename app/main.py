from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
import mlflow.sklearn
import pandas as pd
from fastapi.encoders import jsonable_encoder
from typing import List

app = FastAPI()

# Data model representing input
class Record(BaseModel):
    season: int
    mnth: int
    holiday: int
    weekday: int
    workingday: int
    weathersit: int
    temp: float
    atemp: float
    hum: float
    windspeed: float


@app.on_event("startup")
async def startup_load_model():
    global MODEL
    MODEL = mlflow.sklearn.load_model("./model")

@app.post("/predict")
async def predict(data: List[Record]):  
    input_df = pd.DataFrame(jsonable_encoder(data))

    model_output = MODEL.predict(input_df)

    response = int(model_output)

    return {"data": response}

@app.get("/")
def read_root():
    return {"data":"Hello World"}
