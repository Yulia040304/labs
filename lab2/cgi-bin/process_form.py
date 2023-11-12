#!/usr/bin/env python
import cgi

# Встановлення заголовка відповіді Content-type
print("Content-type: text/html\n")

# Отримання даних з форми
form = cgi.FieldStorage()
name = form.getvalue('name')
email = form.getvalue('email')
gender = form.getvalue('gender')
programming_language = form.getvalue('programming_language')
subscribe = form.getvalue('subscribe')

# Виведення HTML-відповіді
print("<html>")
print("<head>")
print("<title>Result of form processing</title>")
print("</head>")
print("<body>")
print("<h1>Result of form processing:</h1>")
print(f"<p>Name: {name}</p>")
print(f"<p>Email: {email}</p>")
print(f"<p>Gender: {gender}</p>")
print(f"<p>Programming language: {programming_language}</p>")
print(f"<p>Subscribe: {'Yes' if subscribe == 'yes' else 'No'}</p>")
print("</body>")
print("</html>")
