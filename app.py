from flask import Flask, request
from server.textgen import make_chat_request
from server.textembed import embed_nlu, embed_story, embed_domain
from server.rasa_services import train_rasa_model
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




# Run the Flask application
if __name__ == '__main__':
    app.run(port=8080)
