from typing import Optional

from fastapi import FastAPI, Response

import json


app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/data")
def read_data():
    data = json.load(open('/home/ec2-user/data.json'))
    res =  f"""<?xml version="1.0"?>
    <data>
        <signatures>{data['signatures']}</signatures>
        <views>{data['views']}</views>
        <shares>{data['shares']}</shares>
    </data>
    """
    return Response(content=res, media_type="application/xml")