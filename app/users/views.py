from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from werkzeug import check_password_hash, generate_password_hash

from app import db
from app.users.models import User
from app.stories.models import Comment, Story
from app.stories.views import paginate

mod = Blueprint('users', __name__, url_prefix='/users')

@mod.route('/')
def list():
    return paginate(request, User.query, 50, "users/list.html")

@mod.route('/<int:user_id>/')
def detail(user_id):
    user = User.query.filter_by(id=user_id).first()
    stories = user.stories.order_by(db.desc("created")).limit(5)
    comments = user.comments.order_by(db.desc("created")).limit(5)
    return render_template("users/detail.html", user=user, stories=stories, comments=comments)

@mod.route('/<int:user_id>/comments/')
def comments(user_id):
    return paginate(request, Comment.query.order_by(db.desc("created")).filter_by(user_id=user_id), 50, "users/comments.html")

@mod.route('/<int:user_id>/stories/')
def stories(user_id):
    return paginate(request, Story.query.order_by(db.desc("created")).filter_by(user_id=user_id), 50, "users/stories.html")
