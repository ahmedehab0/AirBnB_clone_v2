#!/usr/bin/python3
""" runs a flask application"""


from flask import Flask, render_template
from models import storage



app = Flask(__name__)

@app.teardown_appcontext
def teardown(exception):
    """closes the storage on teardown"""
    storage.close()

@app.route("/states_list", strict_slashes=False)
def states_list():
    """return html page with all states presend in dbstorage"""

    states = sorted(list(storage.all("State").values()), key = lambda x:x.name)
    return render_template('7-states_list.html', states=states)

if __name__ == "__main__":
    app.run(debug=True)
