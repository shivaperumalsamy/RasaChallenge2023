from flask import Flask
from server.textgen import make_chat_request
from server.textembed import embed_nlu
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

@app.route('/train')
def train():
    train_sent = "How to get divorce?"
    gen_training_data = make_chat_request(train_sent)
    print(gen_training_data)
    embed_nlu(gen_training_data)
    return "hii"


# Run the Flask application
if __name__ == '__main__':
    app.run(port=8080)
