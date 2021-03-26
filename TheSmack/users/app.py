from flask import redirect, url_for, render_template, request, session, Blueprint
from sqlalchemy.sql import text
from werkzeug.security import generate_password_hash
from TheSmack.users.custom import apology, convert


usermenu_bp = Blueprint('usermenu', __name__,
                          template_folder='templates',
                          static_folder='static')
signup_bp = Blueprint('signup', __name__,
                      template_folder='templates',
                      static_folder='static')


login_bp = Blueprint('login', __name__,
                     template_folder='templates')

profile_bp = Blueprint('profile', __name__,
                     template_folder='templates')

@usermenu_bp.route('/')
def usermenu():
    return "Sign up/Login menu page"

@profile_bp.route('/')
def profile():
    return "Profile page"

@signup_bp.route('/')
def signup():
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
        return render_template("/users/signup.html")



@login_bp.route('/')
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
        return render_template("/users/login.html", error=False)
