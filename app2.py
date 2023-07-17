from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import json
from server.textgen import make_chat_request
from server.textembed import embed_nlu, embed_story, embed_domain
from dotenv import load_dotenv

class SSEHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        if self.path == '/train':
            # Set the response status code
            self.send_response(200)
            # Set the response headers
            self.send_header('Content-Type', 'text/event-stream')
            self.send_header('Cache-Control', 'no-cache')
            self.send_header('Access-Control-Allow-Origin', 'http://localhost:5500')  # Allow requests from any origin
            self.send_header('Access-Control-Allow-Methods', 'POST')  # Allow only POST requests
            self.send_header('Access-Control-Allow-Headers', 'Content-Type')  # Allow only Content-Type header
            self.end_headers()
            
            # Read the content length from the request headers
            content_length = int(self.headers['Content-Length'])
            # Read the request body data
            post_data = self.rfile.read(content_length)
            
            try:
                # Parse the JSON data from the request body
                data = json.loads(post_data)
                
                # Generate the training data
                gen_nlu_training_data = make_chat_request(data['request'])

                message = 'data: Generated Training data SSE!\n\n'  
                # Send the SSE message
                self.wfile.write(message.encode('utf-8'))
                self.wfile.flush()

                embed_nlu(gen_nlu_training_data)
                message = 'data: Generated NLU content SSE!\n\n'  
                # Send the SSE message
                self.wfile.write(message.encode('utf-8'))
                self.wfile.flush()

                embed_domain(gen_nlu_training_data, data['response'])
                message = 'data: Generated Domain content SSE!\n\n'  
                # Send the SSE message
                self.wfile.write(message.encode('utf-8'))
                self.wfile.flush()

                embed_story(gen_nlu_training_data)
                message = 'data: Generated Story data SSE!\n\n'  
                # Send the SSE message
                self.wfile.write(message.encode('utf-8'))
                self.wfile.flush()

                
                print("Files generated successfully")

                
                    
            except ValueError:
                self.send_error(400, 'Invalid JSON data')
        else:
            self.send_response(404)
            self.end_headers()

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', 'http://localhost:5500')  # Allow requests from any origin
        self.send_header('Access-Control-Allow-Methods', 'POST')  # Allow only POST requests
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')  # Allow only Content-Type header
        BaseHTTPRequestHandler.end_headers(self)

if __name__ == '__main__':
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, SSEHandler)
    print('Server running on port 8080...')
    httpd.serve_forever()
