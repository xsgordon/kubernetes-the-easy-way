#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from random import choice
import socket
import os

PORT_NUMBER = 8080

CONTENT_TYPES = {"jpg": "image/jpeg",
                 "jpeg": "image/jpeg",
                 "png": "image/png",
                 "gif": "image/gif"}


STATIC_CAT="./Cat_Melon.jpg"

DYNAMIC_CATZ="./catz"

#This class will handles any incoming request from
#the browser
class myHandler(BaseHTTPRequestHandler):

    def is_image(self, filename):
        return filename.lower()[filename.rfind('.')+1:] in CONTENT_TYPES


    def get_content_type(self, filename):
        return CONTENT_TYPES[filename[filename.rfind('.')+1:].lower()]


    #Handler for the GET requests
    def do_GET(self):
        self.send_response(200)

        cat_of_the_day = STATIC_CAT
        if ( os.path.isdir(DYNAMIC_CATZ) ):
            images = [f for f in os.listdir(DYNAMIC_CATZ) if self.is_image(f)]
            cat_of_the_day = "%s/%s" % (DYNAMIC_CATZ, choice(images))

        self.send_header('Content-type', self.get_content_type(cat_of_the_day))
        self.end_headers()
        # Send the html message
        self.wfile.write(file(cat_of_the_day, "rb").read())


try:
    #Create a web server and define the handler to manage the
    #incoming request
    server = HTTPServer(('', PORT_NUMBER), myHandler)
    print 'Started httpserver on port ' , PORT_NUMBER

    #Wait forever for incoming http requests
    server.serve_forever()

except KeyboardInterrupt:
    print '^C received, shutting down the web server'
    server.socket.close()
