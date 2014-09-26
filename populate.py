from app import db
from config import WORDS
from app.users.models import User
from app.stories.models import Story, Comment
import random
import json
import datetime
import os
import requests

if(os.path.isfile("app.db")):
    os.system("rm app.db")

db.drop_all()
db.create_all()

if not os.path.isfile(WORDS):
    print("No words list exists; downloading...")
    r = requests.get("http://www.freescrabbledictionary.com/twl06.txt")
    with open(WORDS, "w+") as f:
        f.write(r.text)
else:
    print("Words list exists; skipping")

print("Creating users")
for i in range(1, 100):
    username = random.choice(list(open(WORDS)))
    if "'" in username:
        username = username.split("'")[0]
    u = User("{}{}".format(username.strip(), random.randint(0, 2000)), "email{}@example.com".format(i), "password", datetime.datetime.now())
    db.session.add(u)
    db.session.commit()
print("done")

u = User.query.all()
paragraphs = json.loads(open("var/lorem.json", "r").read())
print("Creating stories")
for i in range(1, 1000):
    number_of_paragraphs = random.randint(1, 20)
    story_content = ""
    for x in range(0, number_of_paragraphs):
        story_content += "{}\n\n".format(random.choice(paragraphs))
    s = Story(1, "Story {}".format(i), story_content, datetime.datetime.now())
    s.user_id = random.randint(1, len(u))
    db.session.add(s)
    db.session.commit()
print("done")

print("Creating comments ")
s = Story.query.all()
for i in range(1, 10000):
    c = Comment(1, 1, random.choice(paragraphs), datetime.datetime.now())
    c.user_id = random.randint(1, len(u))
    c.story_id = random.randint(1, len(s))
    db.session.add(c)
    db.session.commit()
print("done")
