from flask import Blueprint, render_template
from app.stories.models import Story
from app import db

mod = Blueprint('pages', __name__)

@mod.route('/')
def home():
    stories = Story.query.order_by(db.desc("created")).limit(10)
    return render_template("pages/home.html", stories=stories)
