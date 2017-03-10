import os
basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
PROFILE = True

PREFIX = '/api/v1'

DATABASE = 'puppenc'
SQLALCHEMY_DATABASE_CONN = 'mysql://root:puppenc@172.17.0.2'

SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_CONN + '/' + DATABASE
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False

THREADS_PER_PAGE = 8
