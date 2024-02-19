#!/usr/bin/python3
"""starts a Flask Web application"""


from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)

@app.teardown_appcontext
def teardown(exception):
    """closes the storage on teardown"""
    storage.close()

@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    states= sorted(list(storage.all(State).values()), key = lambda x:x.name)
    amenities = sorted(list(storage.all(Amenity).values()), key = lambda x:x.name)
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)


if __name__ == "__main__":
    app.run(debug=True)