from flask import Flask, request
from server.textgen import make_chat_request
from server.textembed import embed_nlu, embed_story, embed_domain
from server.rasa_services import train_rasa_model
from server.util import write_content_to_file
# from server.kb import get_kb_answer
from dotenv import load_dotenv
from flask_cors import CORS

load_dotenv()

# Create a Flask web application
app = Flask(__name__)

CORS(app)

@app.route('/')
def root():
    return 'Server is On...'

# Define a route and its corresponding handler
@app.route('/status')
def checkServer():
    return 'Hi, the server is alive!'

@app.route('/train', methods=['POST'])
def train():

    data = request.json
    
    gen_nlu_training_data = make_chat_request(data['request'])
 
    embed_nlu(gen_nlu_training_data)
    embed_domain(gen_nlu_training_data, data['response'])
    embed_story(gen_nlu_training_data)
    train_rasa_model()
    
    return "Rasa train completed successfully"

@app.route('/train-kb', methods=['POST'])
def train_knowledgebase():

    data = request.json
    
    write_content_to_file('data/train.txt', data['response'])
    
    return "Added content to the train file successfully"

# @app.route('/kb', methods=['POST'])
# def get_kb():
#     data = request.json 
#     response = get_kb_answer(data['request'])
#     return response

# Run the Flask application
if __name__ == '__main__':
    app.run(port=8080)
