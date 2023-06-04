from flask import Flask,jsonify,request
from flask_cors import CORS
from dotenv import load_dotenv
import openai
import requests
import os

app=Flask(__name__)

CORS(app)
load_dotenv()

@app.post('/getrecipe')



def getrecipe():
    URL = "https://api.openai.com/v1/chat/completions"
    key= os.environ.get('apikey')

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
