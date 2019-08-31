#!/usr/bin/python3

"""
Write a script that starts a Flask web application
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.user import User

app = Flask(__name__)


@app.teardown_appcontext
def close(self):
    """Closes current app"""
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns hbnb"""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    places = storage.all(Place).values()
    table = {}
    for p, u in storage._DBStorage__session.query(Place, User).filter(Place.user_id == User.id):
        table[p.user_id] = "{} {}".format(u.first_name, u.last_name)
    return render_template('100-hbnb.html', **locals())


app.run(host="0.0.0.0", port="5000")
