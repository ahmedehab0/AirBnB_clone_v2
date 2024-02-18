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

@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """display “C ” followed by the value of the text variable"""
    return 'C ' + text.replace('_', ' ')

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """display “python ” followed by the value of the text variable"""
    return 'Python ' + text.replace('_', ' ')

@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
        return '{:d} is a number'.format(n)


if __name__ == "__main__":
    app.run(debug=True)
