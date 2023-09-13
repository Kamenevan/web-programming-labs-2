from flask import Flask
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
    return """
<!doctype html>
<html>
    <head>
        <title>Каменева Наталья Анатольевна, лабораторная 1</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

        <h1>web-сервер на flask</h1>

        <footer>
            &copy; Наталья Каменева, ФБИ-13, 3 курс, 2023
        </footer>
    </body>
<html>
""" 
@app.route("/lab1")
def lab1():
    return """
<!doctype html>
<html>
    <head>
        <title>Каменева Наталья Анатольевна, лабораторная 1</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

        <h1>web-сервер на flask</h1>
            Flask — фреймворк для создания веб-приложений на языке
            программирования Python, использующий набор инструментов
            Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
            называемых микрофреймворков — минималистичных каркасов
            веб-приложений, сознательно предоставляющих лишь самые базовые возможности
        <footer>
            &copy; Наталья Каменева, ФБИ-13, 3 курс, 2023
        </footer>

    </body>
<html>
"""