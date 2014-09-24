from flask import Flask, render_template
from flask.ext.markdown import Markdown
from flask.ext.sqlalchemy import SQLAlchemy
import socket

app = Flask(__name__)
Markdown(app)
app.config.from_object('config')

db = SQLAlchemy(app)

#@app.errorhandler(404)
#def not_found(error):
#    return render_template('404.html'), 404

from app.users.views import mod as usersModule
app.register_blueprint(usersModule)

from app.stories.views import mod as storiesModule
app.register_blueprint(storiesModule)

from app.pages.views import mod as pagesModule
app.register_blueprint(pagesModule)

@app.context_processor
def node():
    return dict(node=socket.gethostname())
