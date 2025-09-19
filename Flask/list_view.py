from flask import Flask
from flask import render_template

app = Flask(__name__)

contents = [
    {
        "idx": 1,
        "title": "Java study",
        "author": "gnag",
        "content": "lookieso",
        "wDate": "2025-05-15",
    },
    {
        "idx": 2,
        "title": "Python study",
        "author": "hye",
        "content": "newme",
        "wDate": "2025-05-15",
    },
    {
        "idx": 3,
        "title": "Flask study",
        "author": "rin",
        "content": "chageup",
        "wDate": "2025-05-15",
    },
]


@app.route("/")
def index():
    return render_template("list.html", data=contents)


@app.route("/view")
def view():
    result = contents[0]
    return render_template("view.html", data=result)


if __name__ == "__main__":
    app.run(debug=True)
