#!/usr/bin/python3
"""
Start a Flask web application
"""
from flask import Flask

app = Flask(__name__)

# Route to display "Hello HBNB!"
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Print output as 'Hello HBNB!'
    """
    return 'Hello HBNB!'

# New route for AirBnB one-page
@app.route('/airbnb-onepage/', strict_slashes=False)
def hello_airbnb_onepage():
    """
    Print output as 'Hello AirBnB one-page!'
    """
    return 'Hello AirBnB one-page!'

if __name__ == '__main__':
    """
    Run the Flask app on 0.0.0.0, port 5000
    """
    app.run(host='0.0.0.0', port=5000)

