from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy(app)

#database set up
class User(db.Model):
    username = db.Column(db.String(255), primary_key=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    school = db.Column(db.String(255), nullable=False)
    bio = db.Column(db.String(256), nullable=False)
    is_active = True
    is_anonymous = False
    is_authenticated = False
    def get_id(self):
        return self.username


#function creates user
def user_create(username, password, school, bio):
    print('User name is ' + username + ' password is ' + password + ' school is ' + school + ' bio is ' + bio)

    new_user = User(username=username, password=password, school=school, bio=bio)
    db.session.add(new_user)
    db.session.commit()



#function for logging in
def validate_user(username, password):
    testuser=User.query.filter_by(username=username).first()
    if testuser:
        print("got user")
        if testuser.password == password:
            testuser.is_authenticated = True
            return testuser
    return None

def get_users(school):
    return User.query.filter_by(school=school).all()













