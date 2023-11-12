#!/usr/bin/env python
from http.server import CGIHTTPRequestHandler, HTTPServer

# Вказати шлях до теки, де знаходяться CGI-сценарії
cgi_dir = "form.html"

# Запустити CGI-сервер на порту 8000
server_address = ("", 8000)
httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
httpd.cgi_directories = [cgi_dir]

print(f"Сервер слухає на порту {server_address[1]}...")
httpd.serve_forever()
