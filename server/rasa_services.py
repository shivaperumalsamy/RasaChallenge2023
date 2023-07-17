import yaml
from yaml import SafeLoader
import requests
import os
import json
from dotenv import load_dotenv
import re
import rasa


def train_rasa_model():
    # f_domain = open("domain.yml", 'r')
    # f_nlu = open("data/nlu.yml", 'r')
    # f_stories = open("data/stories.yml", 'r')
    # f_config = open("config.yml", 'r')

    # headers = {
    #     'Content-Type': 'application/yaml'
    #     # 'Authorization': f'Bearer {TOKEN}'
    # }
    # data = f_domain.read() +  '\n' + f_nlu.read() +  '\n'  + f_stories.read() + '\n' + f_config.read()
    # print("*******data::::")
    # # print(yaml.load(data))
    # # data2 = yaml.dump(yaml.load(data), sort_keys=False)
    # data = re.sub(r'version:.*', '', data)
    # print(data)


    # # requests.post(os.environ.get('HOST_NAME') + '/model/train', headers=headers, json=data)

    config = 'config.yml'
    training_files = './data/'
    domain = 'domain.yml'
    output = './models/'
    rasa.train(domain, config, [training_files], output, fixed_model_name='latest_model')

