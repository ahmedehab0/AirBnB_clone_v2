#!/usr/bin/python3
"""starts a Flask Web application"""


from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
app = Flask(__name__)

@app.teardown_appcontext
def teardown(exception):
    """closes the storage on teardown"""
    storage.close()

@app.route("/hbnb", strict_slashes=False)
def hbnb_filters():
    states= sorted(list(storage.all(State).values()), key = lambda x:x.name)
    amenities = sorted(list(storage.all(Amenity).values()), key = lambda x:x.name)
    places = sorted(list(storage.all(Place).values()), key = lambda x:x.name)

    return render_template('100-hbnb.html', states=states, amenities=amenities, places=places)


if __name__ == "__main__":
    app.run(debug=True)
