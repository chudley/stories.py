from app import db
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.hybrid import hybrid_property

class User(db.Model):

    __tablename__ = 'users_user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120))
    created = db.Column(db.DateTime)
    stories = db.relationship("Story", backref="users_user", lazy="dynamic")
    comments = db.relationship("Comment", backref="users_user", lazy="dynamic")

    def __init__(self, name=None, email=None, password=None, created=None):
        self.name = name
        self.email = email
        self.password = password
        self.created = created

    @hybrid_property
    def comment_count(self):
        return self.comments.count()

    @hybrid_property
    def story_count(self):
        return self.stories.count()

    def __repr__(self):
        return '<User %r>' % (self.name)
