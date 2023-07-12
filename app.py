from flask import Flask

# Create a Flask web application
app = Flask(__name__)

# Define a route and its corresponding handler
@app.route('/status')
def checkServer():
    return 'Hi, the server is alive!'

# Run the Flask application
if __name__ == '__main__':
    app.run(port=8080)
