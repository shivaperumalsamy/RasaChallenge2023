
import requests
import os
import json
import re
import time

API_URL = 'https://api.openai.com/v1/chat/completions'


def convert_to_snake_case(string):
    # Replace capital letters with underscore + lowercase letters
    converted = re.sub(r'(?<!^)(?=[A-Z])', '_', string).lower()
    return converted

def make_chat_request(prompt):
    TOKEN = os.environ.get('TOKEN')
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {TOKEN}'
    }
    

    data = {
      "model": "gpt-3.5-turbo",
      "messages": [ {"role": "system", "content": "generate 10 rasa nlu training utterances for \""+prompt +"\""}]
    };

    # TODO - COMMENTED BELOW LINES FOR DEV

    # BEGIN ---- CHATGPT REQUEST
    # response = requests.post(API_URL, headers=headers, json=data)
    # response.raise_for_status()
    # nlu_response = response.json()['choices'][0]['message']['content']
    # print(nlu_response)


    # data = {
    #   "model": "gpt-3.5-turbo",
    #   "messages": [ {"role": "system", "content": " generate 1 rasa intent name for \""+prompt +"\""}]
    # };

    
   

    # response = requests.post(API_URL, headers=headers, json=data)
    # response.raise_for_status()
    
    # intent_response = response.json()['choices'][0]['message']['content']
    # print("original:",intent_response,"\n converted:",convert_to_snake_case(intent_response))

    # END ---- CHATGPT REQUEST

    nlu_response = """1. How do I file for a divorce?
2. What are the steps to get a divorce?
3. Can you guide me on initiating the divorce process?
4. How can I legally end my marriage?
5. What is the procedure to obtain a divorce?
6. I need information on how to start the divorce proceedings.
7. Can you provide details on how to go about getting a divorce?
8. What documents do I need to file for a divorce?
9. How can I dissolve my marriage according to legal requirements?
10. Please explain the process of obtaining a divorce."""


    intent_response = "divorce_process"

    time.sleep(1)

    gen_training_data = {
        "nlu": nlu_response,
        "intent": convert_to_snake_case(intent_response)
    }
    
    return gen_training_data

