from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy(app)

#database set up
class Anon(db.Model):
    name = db.Column(db.String(255), primary_key=True, nullable=False)
    emotion = db.Column(db.String(255), nullable=False)
    update = db.Column(db.String(255), nullable=False)
    is_active = True
    is_anonymous = False
    is_authenticated = False
    def get_id(self):
        return self.username



#function creates anon post
def anon_create(name, emotion, update):
    print(' emotion is ' + emotion + ' update is ' + update)

    anon_post = Anon(name=name, emotion=emotion, update=update)
    db.session.add(anon_post)
    db.session.commit()