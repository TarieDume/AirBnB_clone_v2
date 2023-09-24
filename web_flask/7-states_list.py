#!/usr/bin/python3
""" This script runs an app with Flask framework """
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def session_teardown(exception):
    """ function for teardown """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def html_display():
    """ function called with /states_list route """
    states = storage.all(State)
    dict_to_html = {value.id: value.name for value in states.values()}
    return render_template('7-states_list.html',
                           Table="States",
                           items=dict_to_html)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
