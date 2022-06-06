# -*- coding: utf-8 -*-

from fastapi import FastAPI
from api_request import OneThesisPredictionRequest
from predict import PredictNumbers
import json
import webbrowser
import requests

app = FastAPI()
print(111111)
@app.get("/health_check")
async def health_check():
	return {"message": "ok"}
print(22222)
# api_url = "http://localhost:8001/thesis/one-theis-predictions-1"
# api_url = "http://0.0.0.0:8001/thesis/one-theis-predictions-1"
api_url = "http://host.docker.internal:8001/thesis/one-theis-predictions-1"



def use_requests(api_url, myjson):
    response = requests.post(api_url, json = myjson)
    print("response text :",response.text)
    json_response = json.loads(response.text)
    print("json response:",json_response)
    labels = json_response['labels']
    return labels

@app.post("/thesis/one-theis-predictions")
async def oneBookPredict(item:OneThesisPredictionRequest):
        res = {}
        res["thesis_id"] = item.thesis_id
        test_ids = PredictNumbers(item.text)
        res["test_ids"] =  test_ids
        # my = {'test_ids': test_ids}
        myobj = {'test_ids': test_ids}

        labels = use_requests(api_url,myobj)
        return labels
print(33333)
