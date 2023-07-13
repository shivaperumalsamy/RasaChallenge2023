import re

def embed_nlu(nlu_json):

    yml_str = '\n'

    # Intent replace
    yml_str += "- intent: " + nlu_json['intent'] +"\n"
    yml_str += "  examples: |\n"

    for e in nlu_json['nlu'].split("\n"):
        yml_str += re.sub(r'^\d+\.\s', "    - ", e) +"\n"
    
    print("*****")
    print(yml_str)
    with open("data/nlu.yml",'a') as fp:
        fp.write(yml_str)
