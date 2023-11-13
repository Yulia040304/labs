#!/usr/bin/env python3
import http.cookies
import os

# Видалення всіх cookies
print("Set-Cookie: form_counter=0; expires=Thu, 01 Jan 1970 00:00:00 GMT")
print("Content-type: text/html\n")
print("<html>")
print("<head>")
print("<title>Delete Cookies</title>")
print("</head>")
print("<body>")
print("<h1>All Cookies delete.</h1>")
print("</body>")
print("</html>")
