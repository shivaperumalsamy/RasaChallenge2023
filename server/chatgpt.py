import requests
import os
from dotenv import load_dotenv
load_dotenv()

API_URL = 'https://api.openai.com/v1/chat/completions'
API_FILE_URL = "https://api.openai.com/v1/engines/text-davinci-003/completions"

TOKEN = os.environ.get('TOKEN')
headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {TOKEN}'
}

def chat_gpt_request(content):

    data = {
        "model": "gpt-3.5-turbo",
        "messages": [ {"role": "system", "content": content}]
    };

    response = requests.post(API_URL, headers=headers, json=data)
    response.raise_for_status()
    return response.json()['choices'][0]['message']['content']

def parse_file_and_get_answer(question):
    
    file_path = "./data/train.txt"
    with open(file_path, 'r') as file:
        file_content = file.read()

    data = {
       
        "prompt" : "Answer the question as truthfully as possible, and if you're unsure of the answer, say 'Sorry, I do not know', based on the file content::\n " +file_content + "\n Question: " + question,
        "max_tokens" : 100,
        "n" : 1,
        "stop" : None,
        "temperature" : 0,
        "top_p" : 1,
        "frequency_penalty" : 0,
        "presence_penalty" : 0
    };

    response = requests.post(API_FILE_URL , headers=headers, json=data)
    response.raise_for_status()

    answer = response.json()['choices'][0]['text'].strip()
    print("answer from chatgpt::" + answer)
    return answer