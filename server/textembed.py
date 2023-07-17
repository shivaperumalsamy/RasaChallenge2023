import re
import yaml
from yaml import SafeLoader
import pyaml


def embed_nlu(nlu_json):

    yml_str = "\n\n"

    # Intent replace
    yml_str += "- intent: " + nlu_json['intent'] +"\n"
    yml_str += "  examples: |\n"

    for e in nlu_json['nlu'].split("\n"):
        mod_str = re.sub(r'^\d+\.\s', "- ", e) +"\n"
        yml_str += '    ' + mod_str

    
    
    print("***** nlu *********")
    print(yml_str)
    with open("data/nlu.yml",'a') as fp:
        fp.write(yml_str)


def embed_story(nlu_data ):

    story_str = '\n'
    story_str += '- story: story_'+ nlu_data['intent'] + '\n'
    story_str += '  steps:\n'
    story_str += "  - intent: " + nlu_data['intent'] + '\n'
    story_str += "  - action: utter_" + nlu_data['intent'] + '\n'

    print("******** story ******** ")
    print(story_str)

    with open("data/stories.yml",'a') as fp:
        fp.write(story_str)
    

def embed_domain(nlu_data, story_response ):

    domain_data = ''

    domain_data = open("domain.yml", 'r')

    domain_data_json = yaml.load(domain_data, Loader=SafeLoader)
    domain_data_json['intents'].append(nlu_data['intent'])
    domain_data_json['responses']['utter_' + nlu_data['intent']]= [{"text":story_response}]
    print("domain_data_json")
    print(domain_data_json)

    f_out = open("domain.yml", 'w')
    for yaml_obj in domain_data_json:

        domain_obj = {}
        domain_obj[yaml_obj] = domain_data_json[yaml_obj]
        print(domain_obj)

        f_out.write(yaml.dump(domain_obj, sort_keys=False))
        f_out.write("\n")



