from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def hello_flask():
    html = render_template("index_static.html")
    return html


@app.route("/view")
def view_item():
    return render_template("item.html", name="gang", age=20, addr="Seoul")


@app.route("/base")
def bast():
    html = render_template("/static/html/base.html")
    return html


if __name__ == "__main__":
    app.run(debug=True)
