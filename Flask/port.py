from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_flask():
    return "<html><body><p>returnd document from Flask server</p><p>Hi 8080:)</p></html></body>"


@app.route("/item/100")
def show_item():
    return "100th response"


@app.route("/list")
def show_list():
    return "100th response"


if __name__ == "__main__":
    app.run(debug=True, port=8080)
