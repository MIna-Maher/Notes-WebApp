import os
from flask import Flask ###import flask class.

def create_app(test_config=None) :
    app = Flask(__name__)  ###https://flask.palletsprojects.com/en/1.0.x/api/#flask.Flask
    app.config.from_mapping(
        SECRET_KEY=os.environ.get('SECRET_KEY', default='dev')
    
    )
    if test_config is None :
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
    
    
    return app