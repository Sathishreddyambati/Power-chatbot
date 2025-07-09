import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Load token from .env file

HUGGINGFACE_API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"
headers = {
    "Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}"
}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    result = response.json()
    try:
        return result[0]['generated_text']
    except:
        return "Sorry, I couldn't get the answer."

def get_bot_response(user_input):
    return query({
        "inputs": f"[INST] {user_input} [/INST]"
    })