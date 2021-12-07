# -*- encoding: utf-8 -*-
"""
Copyright (c) 2021 - present Boyuanshi.com
"""

from flask_migrate import Migrate
from sys import exit
from decouple import config
from apps.partext.models import init_partext_db
from apps.config import config_dict, default_file, init_partext
from apps import create_app
from apps.db import db

# WARNING: Don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True, cast=bool)

# The configuration
get_config_mode = 'Debug' if DEBUG else 'Production'

try:
    # Load the configuration using the default values
    app_config = config_dict[get_config_mode.capitalize()]

except KeyError:
    exit('Error: Invalid <config_mode>. Expected values [Debug, Production] ')

app = create_app(app_config)
Migrate(app, db)

# if init_partext == True:
#     with app.app_context():
#         init_partext_db(default_file['file'])


if DEBUG:
    app.logger.info('DEBUG       = ' + str(DEBUG))
    app.logger.info('Environment = ' + get_config_mode)
    app.logger.info('DBMS        = ' + app_config.SQLALCHEMY_DATABASE_URI)

if __name__ == "__main__":
    app.run()