# -*- encoding: utf-8 -*-
"""
Copyright (c) 2021 - present Boyuanshi.com
"""

import os
from decouple import config

class Config(object):

    basedir = os.path.abspath(os.path.dirname(__file__))

    # Set up the App SECRET_KEY
    SECRET_KEY = config('SECRET_KEY', default='S#perS3crEt_007')

    # This will create a file in <app> FOLDER
    SQLALCHEMY_DATABASE_URI = '{}://{}:{}@{}:{}/{}'.format(
        config('DB_ENGINE', default='mysql+pymysql'),
        config('DB_USERNAME', default='sql_politics_cor'),
        config('DB_PASS', default='t3TJDFJEZAKSdk3n'),
        config('DB_HOST', default='localhost'),
        config('DB_PORT', default=3306),
        config('DB_NAME', default='sql_politics_cor')
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False

    # Security
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = 3600

    # PostgreSQL database
    SQLALCHEMY_DATABASE_URI = '{}://{}:{}@{}:{}/{}'.format(
        config('DB_ENGINE', default='mysql+pymysql'),
        config('DB_USERNAME', default='root'),
        config('DB_PASS', default='root'),
        config('DB_HOST', default='localhost'),
        config('DB_PORT', default=3306),
        config('DB_NAME', default='flask_user')
    )

class DebugConfig(Config):
    DEBUG = True

# Load all possible configurations
config_dict = {
    'Production': ProductionConfig,
    'Debug': DebugConfig
}

default_file = {
    'zh': 'upload/3aube_CN_para_utf8.txt',
    'fr': 'upload/3aube_FR_para_utf8.txt',
    'file': 'upload/Macron20201212-FRCN.txt'
}

init_partext = False
