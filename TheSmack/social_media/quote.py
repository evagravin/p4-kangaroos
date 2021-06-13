from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy(app)

#database set up
class Quotes(db.Model):
    Quote_id = db.Column(db.Integer, primary_key=True, nullable=False)
    Quote = db.Column(db.String(255), nullable=False)
    is_active = True
    is_anonymous = False
    is_authenticated = False
    def get_id(self):
        return self.username



