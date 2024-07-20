#Задание 1
# Создайте новое приложение Flask, которое будет отображать текущие дату и время на главной странице.
# Задание 2
# Создайте новое приложение Flask, создайте структуру проекта с папками static и templates,
# в папке templates должны быть 3 html файла: index, blog, contacts (главная страница, страница блога и контакты).
# Заполните их информацией и выведите силами flask сервера, используя функцию render_template()
# Обязательно на всех страницах сделайте меню, которое будет работать именно при запуске проекта через flask

from flask import Flask, render_template
import time
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/blog/")
def blog():
    return render_template("blog.html")
@app.route("/contacts/")
def contacts():
    return render_template("contacts.html")

@app.route("/hero/")
def main():
    render_template("hero.html")
@app.route('/time/')
def time():
    return "текущее время " + time.ctime()


if __name__ == "__main__":
    app.run()