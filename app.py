from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager

# If you get an error on the next line on Python 3.4.0, change to: Flask('app')
# where app matches the name of this file without the .py extension.
app = Flask(__name__)
app.config['CSRF_ENABLED'] = True
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://docker:docker@192.168.59.103:5432/docker'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask_template.db'
app.config['SECRET_KEY'] ='you will never guess it !'
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

from routes import *
from models import *

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app

if __name__ == '__main__':
    import os
    host = os.environ.get('SERVER_HOST', 'localhost')
    try:
        port = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        port = 5555
    app.debug = True
    app.run(host, port)
