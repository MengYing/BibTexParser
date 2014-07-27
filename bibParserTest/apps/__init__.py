from flask import Flask
from .models import db
from .parserViews import module
from flask.ext.sqlalchemy import SQLAlchemy


__all__ = ('create_app','app')


def _init_db(app):
    db.init_app(app)
    db.app = app
    #db.create_all()

app = Flask(__name__)
#app.SERVER_NAME = '0.0.0.0:6000'
app.config.from_object('config')

_init_db(app)
app.register_blueprint(module)


def create_app(name=None):
    if name is None:
        name = __name__
    app = Flask(name)
    #app.SERVER_NAME = '127.0.0.1:6000'
    app.config.from_object('config')

    _init_db(app)
    app.register_blueprint(module)
    return app
