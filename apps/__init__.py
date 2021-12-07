# -*- encoding: utf-8 -*-
"""
Copyright (c) 2021 - present Boyuanshi.com
"""

from flask import Flask
from flask_login import LoginManager
from .db import db
from importlib import import_module
from apps.partext.models import init_partext_db
from apps.config import default_file, init_partext

login_manager = LoginManager()


def register_extensions(app):
    db.init_app(app)
    login_manager.init_app(app)


def register_blueprints(app):
    for module_name in ('authentication', 'home', 'partext'):
        module = import_module('apps.{}.routes'.format(module_name))
        app.register_blueprint(module.blueprint)


def configure_database(app):

    @app.before_first_request
    def initialize_database():
        db.create_all()
        if init_partext == True:
            with app.app_context():
                init_partext_db(default_file['file'])

    @app.teardown_request
    def shutdown_session(exception=None):
        db.session.remove()

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    register_extensions(app)
    register_blueprints(app)
    configure_database(app)
    return app
