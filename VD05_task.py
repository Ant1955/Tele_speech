# Создайте свой HTML-шаблон (файл base.html).
# Создайте страницы home.html и about.html,
# которые будут расширять шаблон и заполнять его контентом.

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    context = {
        "title": "все фильмы о Гарри Поттере"
    }
    return render_template("index.html", **context)

@app.route("/blog/")
def blog():
    context = {
        "title": "Карточки с информацией о героях",
    }
    return render_template("blog.html", **context)

@app.route("/hero/")
def hero():
    context = {
        "title": "Краткое описание героев",
    }
    return render_template("hero.html", **context)


if __name__ == "__main__":
    app.run()