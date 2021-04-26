import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = True
    SECRET_KEY = 'bd11ed9625dba9f37dccc7d967b056f5'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'Database/app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
