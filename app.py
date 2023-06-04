from flask import Flask,jsonify,request
from flask_cors import CORS
import openai
import requests


app=Flask(__name__)

CORS(app)


@app.post('/getrecipe')



def getrecipe():
    URL = "https://api.openai.com/v1/chat/completions"
    key='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'

    data=request.json
    ingredients=data['ingredients']
    prompt = "Please prove a recipe for listed items"+' '+ingredients


    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}],

    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {key}"
    }

    response=requests.post(URL, headers=headers, json=payload, stream=False)

    return response.content
