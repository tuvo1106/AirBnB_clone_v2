#!/usr/bin/python3

"""
Write a script that starts a Flask web application
"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Returns 'Hello HBNB@'"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns 'HBNB'"""
    return 'HBNB'


@app.route('/c/<var>', strict_slashes=False)
def c(var):
    """Returns 'c/<var>'"""
    return 'C %s' % var.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """Returns 'python/<var>'"""
    return 'Python %s' % text.replace('_', ' ')


@app.route('/number/<int:n>')
def num(n):
    """Returns '/number/n'"""
    return '%d is a number' % n


@app.route('/number_template/<int:n>')
def num_template(n):
    """Returns a template with the number in url"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def odd_or_even(n):
    """Returns a template with odd or even number"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
