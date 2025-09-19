from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def index():
    html = render_template(
        "index.html", title="Jinja2 syntax", content=r"{{ name}} data"
    )
    return html


@app.route("/user/view/1")
def userInfo():
    return render_template(
        "userInfo.html",
        idx="N-001",
        userName="gang",
        userLevel="user",
        joinDate="2021-5-15",
        isRetire="False",
    )


@app.route("/user/view/2")
def userInfo_d():
    userData = {
        "name": "Hye",
        "age": 21,
        "idx": "N-001",
        "userLevel": "admin",
        "joinDate": "2024-05-15",
        "isRetire": True,
        "retireDate": "2025-01-01",
    }

    return render_template("userInfo_d.html", data=userData)


ListData = ["Java", "JavaScript", "Python", "HTML", "CSS"]


@app.route("/list/lang")
def showLangList():
    return render_template("list_lang.html", data=ListData)


if __name__ == "__main__":
    app.run(debug=True)
