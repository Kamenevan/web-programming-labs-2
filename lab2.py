from flask import Blueprint, redirect, url_for, render_template
lab2 = Blueprint ('lab2',__name__)

@lab2.route("/lab2/example")
def example():
    name = 'Наталья Каменева'
    group = 'ФБИ-13'
    course = '3'
    lab_name= '2'
    fruits = [
        {'name':'яблоки', 'price': 100},
        {'name':'груши', 'price': 120},
        {'name':'апельсины', 'price': 80},
        {'name':'мандарины', 'price': 95},
        {'name':'манго', 'price': 321},
        ]
    books=[
        {'booktitle' : 'Ночной портье', 'author' : 'Ирвин Шоу', 'genre' : 'Роман', 'numpages' : 352},
        {'booktitle' : 'Преступление и наказание', 'author' : 'Федор Достоевский', 'genre' : 'Роман', 'numpages' : 608},    
        {'booktitle' : 'Война и мир. Том 2', 'author' : 'Лев Толстой', 'genre' : 'Роман', 'numpages' : 416},   
        {'booktitle' : 'Маленький принц', 'author' : ' Антуан де Сент-Экзюпери', 'genre' : 'Сказка', 'numpages' : 128}, 
        {'booktitle' : 'Евгений Онегин',  'author' : 'Александр Пушкин', 'genre'  : 'Роман',  'numpages' : '456'},  
        {'booktitle' : 'Дневник памяти', 'author' : 'Николас Спаркс', 'genre' : 'Любовный роман', 'numpages' : 256},
        {'booktitle' : '451 градус по Фаренгейту', 'author' : 'Рей Бредбери', 'genre' : 'Роман-антиутопия', 'numpages' : 288},
        {'booktitle' : 'Мастер и Маргарита', 'author' : 'Михаил Булгаков', 'genre' : 'Любовный роман', 'numpages' : 480},
        {'booktitle' : 'Цветы для Элджернона', 'author' : 'Даниел Киз', 'genre' : 'Научная фантастика', 'numpages' : 384},
        {'booktitle' : 'Герой нашего времени', 'author' : 'Михаил Лермонтов', 'genre' : 'Роман', 'numpages' : 288}, 
        ]
    return render_template('example.html', name=name, group=group, course=course, lab_name=lab_name, fruits=fruits, books=books)  

@lab2.route ('/lab2/')
def lab2():
    return render_template('lab2.html')

@lab2.route ('/lab2/topphoto')
def topphoto():
    return render_template('topphoto.html')