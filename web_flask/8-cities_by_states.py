#!/usr/bin/python3
"""starts a Flask Web application"""


from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

@app.teardown_appcontext
def teardown(exception):
    """closes the storage on teardown"""
    storage.close()

@app.route("/cities_by_states", strict_slashes = False)
def ciites_by_states():
    """returns html page with all the cities related to astate in the database"""

    states = sorted(list(storage.all(State).values()), key = lambda x:x.name)
    cities = sorted(states.cities, key = lambda x:x.name)
    return render_template('8-cities_by_states.html', states=states, cities = cities)


if __name__ == '__main__':
    app.run(debug=True)
