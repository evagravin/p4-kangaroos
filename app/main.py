from flask import Flask, flash, jsonify, redirect, url_for, render_template, request, session, current_app, g
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from TheSmack.users.app import usermenu_bp, signup_bp, login_bp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
import random

from custom import apology, convert, convertList
app = Flask(__name__)

# database setup
dbURI = 'sqlite:///chess.db'
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

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        formUser = request.form["username"]  # using name as dictionary key
        resultproxy = db.engine.execute(
            text("SELECT * FROM users WHERE username=:username;").execution_options(autocommit=True),
            username=formUser)

        user = convert(resultproxy)

        # troubleshooting
        if user == False:
            return render_template("login.html", error=True)

        # set the user id
        session.clear()
        session["user_id"] = user["id"]

        # redirects us to the user page
        return redirect(url_for("user1", usr=user["username"]))
    else:
        return render_template("login.html", error=False)

@app.route('/newuser/', methods=["GET", "POST"])
def new_user():
    """Register user"""
    if request.method == "POST":
        # Make sure they put in their username
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Make sure they put in a password
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Make sure the passwords match
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("passwords must match", 403)

        fullname = request.form.get("name")
        print(request.form.get("bio") == '')

        # Insert all the values into the database
        db.engine.execute(
            text("INSERT INTO users (username, hash, name, bio) VALUES (:user, :hash, :name, :bio);").execution_options(
                autocommit=True),
            user=request.form.get("username"),
            hash=generate_password_hash(request.form.get("password")),
            name=fullname, bio=request.form.get("bio"))

        return redirect("/login")
    else:
        return render_template("signup.html")



if __name__ == "__main__":
    app.run(port='3000', host='127.0.0.1')