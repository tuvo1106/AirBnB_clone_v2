#!/usr/bin/python3

"""
Write a script that starts a Flask web application
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def close(self):
    """Closes current app"""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """Returns states and id"""
    state = None
    return render_template('10-hbnb_filters.html', state=state)


app.run(host="0.0.0.0", port="5000")
