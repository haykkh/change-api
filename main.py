from typing import Optional

from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/data")
def read_data():
    return json.load(open('../scrape/data.json'))