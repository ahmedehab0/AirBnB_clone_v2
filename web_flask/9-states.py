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

@app.route("/states", strict_slashes=False)
def states_list():
    """return html page with all states presend in dbstorage"""

    states = sorted(list(storage.all("State").values()), key = lambda x:x.name)
    return render_template('9-states.html', states=states)

@app.route("/states/<state_id>", strict_slashes=False)
def states_id(state_id):
    states = sorted(list(storage.all(State).values()), key = lambda x:x.name)
    found_state = None
    for state in states:
        if state_id == state.id:
            found_state = state

    return render_template('9-states.html', found_state=found_state, state_id=state_id)


if __name__ == "__main__":
    app.run(debug=True)
