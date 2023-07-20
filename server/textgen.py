
import requests
import os
import json
import yake
import re
import time
from server.chatgpt import chat_gpt_request

def convert_to_snake_case(string):
    # Replace capital letters with underscore + lowercase letters
    converted = re.sub(r'(?<!^)(?=[A-Z])', '_', string).lower()
    return converted

def make_chat_request(prompt):

    print("inside make_chat_request:::")

    kw_extractor = yake.KeywordExtractor(top=1, stopwords=None) # Extract intent from Yet Another Keyword Extractor (Yake)
    keywords = kw_extractor.extract_keywords(prompt)
    intent_response = "get_" + keywords[0][0].replace(" ",'_').lower()
    print(intent_response)
    ENV = os.environ.get('ENV', "DEV")

    if "PROD" in ENV:

        # CHATBOT - Get list of utterances call
        data = "generate 10 rasa nlu training utterances for \""+prompt +"\""
        nlu_response = chat_gpt_request(data)
        print(nlu_response)
        
    else:
    
        nlu_response = """- How do I file for a divorce?
    - What are the steps to get a divorce?
    - Can you guide me on initiating the divorce process?
    - How can I legally end my marriage?
    - What is the procedure to obtain a divorce?
    - I need information on how to start the divorce proceedings.
    - Can you provide details on how to go about getting a divorce?
    - What documents do I need to file for a divorce?
    - How can I dissolve my marriage according to legal requirements?
    - Please explain the process of obtaining a divorce."""


        intent_response = "divorce_process"
        time.sleep(1) # to just add some delay on hardcoded value

    # Construct return variable
    gen_training_data = {
        "nlu": nlu_response,
        "intent": convert_to_snake_case(intent_response)
    }
    
    return gen_training_data

