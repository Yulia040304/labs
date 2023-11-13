#!/usr/bin/env python
import html
import http.cookies
import os
import cgi


def sanitize_input(value):
    return html.escape(value)

# Отримання даних з форми
form = cgi.FieldStorage()
name = sanitize_input(form.getvalue('name') or "Не вказано")
email = sanitize_input(form.getvalue('email') or "Не вказано")
gender = sanitize_input(form.getvalue('gender') or "Не вказано")
programming_language = sanitize_input(form.getvalue('programming_language') or "Не вказано")
subscribe = "yes" if form.getvalue('subscribe') == 'yes' else "no"

# Отримання значення cookies
cookies_str = os.environ.get("HTTP_COOKIE", "")
cookies = http.cookies.SimpleCookie(cookies_str)

# Створення або отримання cookies
form_counter_cookie = cookies.get('form_counter')
form_counter = int(form_counter_cookie.value) + 1 if form_counter_cookie else 1
cookies['form_counter'] = str(form_counter)
cookies['form_counter']['expires'] = 86400  # Налаштування терміну життя в секундах (24 години)
cookies['form_counter']['path'] = '/cgi-bin'

# Виведення HTML-відповіді
print("Content-type: text/html\n")
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
print(f"<p>Subscribe: {subscribe}</p>")
print(f"<p>The number of completed forms: {form_counter}</p>")

# Форма для видалення cookies
print("<form method='post' action='/cgi-bin/delete_cookies.py'>")
print("<input type='submit' name='delete_cookies' value='Delete Cookies'>")
print("</form>")

print("</body>")
print("</html>")
