from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about')
def about_me():
    return render_template("#")


@app.route('/portfolio')
def portfolio():
    return render_template("portfolio.html")


@app.route('/portfolio/fur_salon')
def fur_salon():
    return render_template("index_fur_salon.html")


@app.route('/portfolio/boogle')
def boogle():
    return render_template("boogle_index.html")


@app.route('/portfolio/fakebook')
def fakebook():
    return render_template("fakebook_index.html")


if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)
