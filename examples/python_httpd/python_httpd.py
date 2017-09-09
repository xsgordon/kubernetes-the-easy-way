#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import socket
import httplib
import os
from urlparse import urlparse

PORT_NUMBER = 8080

#This class will handles any incoming request from
#the browser
class myHandler(BaseHTTPRequestHandler):

    #Handler for the GET requests
    def do_GET(self):

        query = urlparse(self.path).query

        if len(query) == 0:
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            # Send the html message
            self.wfile.write("<p>Hello World from %s!</p><img src='?image' align='center' />" % socket.gethostname())
        else:
            try:
                conn = httplib.HTTPConnection(os.environ['HTTPD_SERVICE_NAME'])

                conn.request("GET", "/")

                resp = conn.getresponse()

                self.send_response(resp.status)

                for header in resp.getheaders():
                    if header[0] == "content-type":
                        self.send_header(header[0], header[1])
                        self.end_headers()
                        break

                self.wfile.write(resp.read())

                conn.close()
            except (socket.gaierror, KeyError):
                print "No hello-catz-imaged-service found."
                self.send_response(404)


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
