#!/usr/bin/env python3

from http.server import CGIHTTPRequestHandler, HTTPServer

handler = CGIHTTPRequestHandler

handler.cgi_directories = ['/cgi-bin', '/htbin']  # this is the default

#server = HTTPServer(('localhost', 80), handler)
#server = HTTPServer(('18.212.18.67', 80), handler)
server = HTTPServer(('172.26.11.182', 80), handler)

server.serve_forever()
