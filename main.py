from flask import Flask, redirect, url_for, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from TheSmack.users.app import usermenu_bp, signup_bp, login_bp
from werkzeug.security import generate_password_hash
from TheSmack.users.custom import apology, convert

app = Flask(__name__)

# database setup
dbURI = 'sqlite:///TheSmack.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = dbURI
db = SQLAlchemy(app)
db.init_app(app)


app = Flask(__name__)
app.register_blueprint(usermenu_bp, url_prefix='/usermenu')
app.register_blueprint(signup_bp, url_prefix='/signup')
app.register_blueprint(login_bp, url_prefix='/login')

#home page route
@app.route('/')
def home():
    return render_template("home.html")



if __name__ == "__main__":
    app.run(port='3000', host='127.0.0.1')