from BaseHTTPServer import HTTPServer
from BaseHTTPServer import BaseHTTPRequestHandler
import json

class JSONRequestHandler (BaseHTTPRequestHandler):

    def do_GET(self):

        #send response code:
        self.send_response(200)
        #send headers:
        self.send_header("Content-type", "application/json")
        # send a blank line to end headers:
        self.wfile.write("\r\n")

        try:
            output = open('data.json', 'r').read()
        except Exception:
            output = "{'error': 'Could not find file " + self.path[1:] + ".json'" + "}"
        self.wfile.write(output)

server = HTTPServer(("localhost", 8080), JSONRequestHandler)
server.serve_forever()

