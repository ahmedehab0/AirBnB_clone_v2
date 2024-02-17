from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def HelloHBNB():
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def HBNB():
    return "HBNB"


if __name__ == "__main__":
    app.run(debug=True)
