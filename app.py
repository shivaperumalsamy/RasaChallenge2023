from flask import Flask, request
from server.textgen import make_chat_request
from server.textembed import embed_nlu, embed_story, embed_domain
from dotenv import load_dotenv

load_dotenv()

# Create a Flask web application
app = Flask(__name__)

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

    
    return "Files generated successfully"




# Run the Flask application
if __name__ == '__main__':
    app.run(port=8080)
