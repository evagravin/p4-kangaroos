from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy(app)

#database set up
class Guest(db.Model):
    post_id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    emotion = db.Column(db.String(255), nullable=False)
    update = db.Column(db.String(255), nullable=False)
    is_active = True
    is_anonymous = False
    is_authenticated = False
    def get_id(self):
        return self.username



#function creates anon post
def guest_create(post_id, name, emotion, update):
    print(' emotion is ' + emotion + ' update is ' + update)

    guest_post = Guest(name=name, emotion=emotion, update=update)
    db.session.add(guest_post)
    db.session.commit()