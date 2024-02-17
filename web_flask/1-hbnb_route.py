#!/usr/bin/python3
"""
starts a Flask web application
"""


from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def HelloHBNB():
    """returns hello hbnb"""

    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """returns hbnb"""

    return "HBNB"


if __name__ == "__main__":
    app.run(debug=True)
