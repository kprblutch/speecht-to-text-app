import os

from flask import Flask
from . import db
from . import auth
from . import index


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'app.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Link to the initiaton function of the DB
    db.init_app(app)

    # Link to the blueprint to allow authentication
    app.register_blueprint(auth.bp)

    # Link the blueprint of the index
    app.register_blueprint(index.bp)
    app.add_url_rule('/', endpoint='index')

    return app
