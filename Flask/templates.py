from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def hello_flask():
    html = render_template("index.html")
    return html


@app.route("/view")
def view_item():
    html = render_template("iteminfo.html")
    return html


if __name__ == "__main__":
    app.run(debug=True)
