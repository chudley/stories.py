import os
import sys
_basedir = os.path.abspath(os.path.dirname(__file__))

WORDS = "var/words.txt"

if os.environ.get('STORIES_ENV') and os.environ['STORIES_ENV'] == 'production':
    DB_USER = "pg_stories"
    DB_PASS = os.environ.get('STORIES_DB_PASS')
    DB_NAME = "db_stories"
    DB_URL = os.environ.get('STORIES_DB_URL')

    SQLALCHEMY_DATABASE_URI = "postgresql://{}:{}@{}/{}".format(DB_USER, DB_PASS, DB_URL, DB_NAME)
else:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'app.db')

STORIES_PER_PAGE = 50
DATABASE_CONNECT_OPTIONS = {}
DEBUG = True
SECRET_KEY = 'development key'
