#!/usr/bin/env python
from http.server import CGIHTTPRequestHandler, HTTPServer  # Замініть цей рядок

# Вказати шлях до теки, де знаходяться CGI-сценарії
cgi_dir = "/cgi-bin"  # Змінено шлях до теки CGI-сценаріїв

# Запустити CGI-сервер на порту 8000
server_address = ("", 8000)
httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
httpd.cgi_directories = [cgi_dir]

print(f"Сервер слухає на порту {server_address[1]}...")
httpd.serve_forever()
