from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from werkzeug import check_password_hash, generate_password_hash

from app import db
from app.stories.models import Story, Comment
import math

mod = Blueprint('stories', __name__, url_prefix='/stories')

@mod.route('/')
def list():
    return paginate(request, Story.query, 50, "stories/list.html")

@mod.route('/<int:story_id>/')
def detail(story_id):
    story = Story.query.filter_by(id=story_id).first()
    comments = story.comments.order_by(db.desc("created")).limit(5)
    return render_template("stories/detail.html", story=story, comments=comments)

@mod.route('/<int:story_id>/comments/')
def comments(story_id):
    story = Story.query.filter_by(id=story_id).first()
    return paginate(request, Comment.query.order_by(db.desc("created")).filter_by(story_id=story_id), 50, "stories/comments.html")

def paginate(request, query, limit=50, template=None):
    if request.args.get("page"):
        page = int(request.args.get("page"))
    else:
        page = 1
    offset = (page * limit) - limit
    total_pages = int(math.ceil(float(query.count()) / float(limit)))
    if request.args.get("page") == "1":
        return redirect(request.path)
    if page > total_pages: 
        return redirect("{}?page={}".format(request.path, total_pages))
    results = query.limit(limit).offset(offset)
    pagination = {
        'current_page': page,
        'total_pages': total_pages,
        'limit': limit,
    }
    return render_template(template, results=results, pagination=pagination)

    
