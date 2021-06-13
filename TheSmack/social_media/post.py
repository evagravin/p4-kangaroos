from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy(app)

#database set up
class Posts(db.Model):
    post_id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String(255), nullable=False)
    emotion = db.Column(db.String(255), nullable=False)
    update = db.Column(db.String(255), nullable=False)
    is_active = True
    is_anonymous = False
    is_authenticated = False
    def get_id(self):
        return self.username


#function creates post
def post_create(post_id, username, emotion, update):
    print('User name is ' + username + ' emotion is ' + emotion + ' update is ' + update)

    new_post = Posts(post_id=post_id, username=username, emotion=emotion, update=update)
    db.session.add(new_post)
    db.session.commit()




