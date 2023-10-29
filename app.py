from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
    return redirect("/menu", code=302)
@app.route("/menu")
def menu():
     return '''
<!doctype html>
<html>
    <head>
        <title> НГТУ, ФБ, Лабораторные работы </title>
    </head>
    <body>
    <header>
        НГТУ, ФБ, WEB- программирование, часть 2. Список лабораторных, меню 
    </header>
    <ol> 
        <li> 
            <a href="/lab1" target="_blank"> Лабораторная работа 1 </a> 
        </li> 
    </ol> 

        <h1>web-сервер на flask</h1>
        
        <a href="/lab1">Первая лабораторная работа</a>

        <footer>
            &copy; Наталья Каменева, ФБИ-13, 3 курс, 2023
        </footer>
    </body>
<html>
'''
@app.route("/lab1")
def lab1():
    return '''
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
        <p>
            Flask — фреймворк для создания веб-приложений на языке
            программирования Python, использующий набор инструментов
            Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
            называемых микрофреймворков — минималистичных каркасов
            веб-приложений, сознательно предоставляющих лишь самые базовые возможности 
        </p>
            <a href="/menu" target="_blank"> Меню </a>
        <ol>
        <h2>Реализованные роуты</h2>
        </ol>
        <ol>
                <li>
                    <a href="/lab1/oak" target="_blank">Дуб</a>
                </li>
                <li>
                    <a href="/lab1/student" target="_blank">ФИО студента НГТУ</a>
                </li>
                <li>
                    <a href="/lab1/python" target="_blank">Язык программирования Python</a>
                </li>
                <li>
                    <a href="/lab1/cat" target="_blank">Кошки в Древнем Египте</a>
                </li>
        </ol>
        <footer>
            &copy; Наталья Каменева, ФБИ-13, 3 курс, 2023
        </footer>
    </body>
</html>
'''
@app.route('/lab1/oak')
def oak():
    return '''
    <!doctype html>
    <header>
        НГТУ, ФБ, WEB- программирование, часть 2. 
    </header>
    <html>
        <body>
        <h1>Дуб</h1>
        <img src="''' + url_for('static', filename='oak.jpg') + '''">
        <link rel="stylesheet" href="''' +url_for('static', filename='lab1.css')+'''">
            <footer>
            &copy; Каменева Наталья Анатольевна, ФБИ-11, 3 курс, 2023
            </footer>
        </body>
    </html>
    '''
@app.route('/lab1/student')
def nstu():
    return '''
    <!doctype html>
    <header>
        НГТУ, ФБ, WEB- программирование, часть 2. 
    </header>
    <html>
        <body>
            <h1>Каменева Наталья Анатольевна</h1>
            <img src="''' + url_for('static', filename='student.jpg') + '''">
            <link rel="stylesheet" href="''' +url_for('static', filename='lab1.css')+'''"
            <footer> 
                &copy; Каменева Наталья Анатольевна, ФБИ-11, 3 курс, 2023
            </footer>
        </body>
    </html>
    '''
@app.route('/lab1/python')
def python():
    return '''
    <!doctype html>
    <html>
    <header>
        НГТУ, ФБ, WEB- программирование, часть 2. 
    </header>
        <body>
        <p>
        Python — это язык программирования, который широко используется в интернет-приложениях, разработке
        программного обеспечения, науке о данных и машинном обучении (ML). Разработчики используют Python,
        потому что он эффективен, прост в изучении и работает на разных платформах. Программы на языке 
        Python можно скачать бесплатно, они совместимы
        </p>
        <img src="''' + url_for('static', filename='python.jpg') + '''">

        <link rel="stylesheet" href="''' +url_for('static', filename='lab1.css')+'''">
        <footer>
            &copy; Каменева Наталья Анатольевна, ФБИ-13, 3 курс, 2023
        </footer>
        </body>
    </html>
    '''
@app.route('/lab1/cat')
def cat():
    return '''
    <!doctype html>
    <html>
    <header>
            НГТУ, ФБ, WEB- программирование, часть 2. 
    </header>
        <body>
            <h1>Кошки в Древнем Египте</h1> <br>
            <p> Кошки в Древнем Египте достигли высокого статуса. 
            Они охраняли жизненно важные посевы от грызунов и стали объектом восхищения.
            Однако мурлыки не просто поедали мышей и крыс. Они также играли определённую роль в загробной жизни человека.
            Древние египтяне носили амулеты с кошками, чтобы призвать защиту и благословение Бастет. Бесчисленные скульптуры 
            кошек были сделаны в её честь и преподнесены в качестве жертвоприношений.</p> 
            <img src="''' + url_for('static', filename='cat.jpg') + '''">    
            <footer>
                &copy; Каменева Натальпя Анатольевна, ФБИ-11, 3 курс, 2023
            </footer> 
        </body>
    </html>
    '''