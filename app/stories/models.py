from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref
from app import db
from sqlalchemy.ext.hybrid import hybrid_property

class Story(db.Model):

    __tablename__ = 'stories_story'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users_user.id'))
    user = db.relationship("User", backref=backref('stories_story', order_by=id))
    title = db.Column(db.String(50), unique=True)
    content = db.Column(db.String(10000))
    created = db.Column(db.DateTime)
    comments = db.relationship("Comment", backref="stories_comment", lazy="dynamic")

    def __init__(self, user_id=None, title=None, content=None, created=None):
        self.user_id = user_id
        self.title = title
        self.content = content
        self.created = created

    @hybrid_property
    def comment_count(self):
        return self.comments.count()

    def __repr__(self):
        return '<Story %r>' % (self.title)

class Comment(db.Model):
    __table_name__ = "stories_comment"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users_user.id'))
    user = db.relationship("User", backref=backref('stories_comment', order_by=id))
    story_id = db.Column(db.Integer, db.ForeignKey('stories_story.id'))
    story = db.relationship("Story", backref=backref('stories_story', order_by=id))
    content = db.Column(db.String(1000))
    created = db.Column(db.DateTime)

    def __init__(self, user_id=None, story_id=None, content=None, created=None):
        self.user_id = user_id
        self.story_id = story_id
        self.content = content
        self.created = created

