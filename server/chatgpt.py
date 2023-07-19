import requests
import os
from dotenv import load_dotenv
load_dotenv()

API_URL = 'https://api.openai.com/v1/chat/completions'

def chat_gpt_request(content):

    TOKEN = os.environ.get('TOKEN')
    headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {TOKEN}'
    }

    data = {
        "model": "gpt-3.5-turbo",
        "messages": [ {"role": "system", "content": content}]
    };

    response = requests.post(API_URL, headers=headers, json=data)
    response.raise_for_status()
    return response.json()['choices'][0]['message']['content']