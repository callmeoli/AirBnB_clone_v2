#!/usr/bin/python3

""" a script thet starts Flask web app """

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def HBHB():
    return 'HBNB'

@app.route('/c/<string:text>', strict_slashes=False)                                                     
def C(text):                                               
    return 'C {}'.format(text.replace("_", " "))

@app.route('/python/')
@app.route('/python/<string:text>')                                                     
def python(text= 'is cool'):                                            
    return 'Python {}'.format(text.replace("_", " "))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
