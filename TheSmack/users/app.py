from flask import redirect, url_for, render_template, request, session, Blueprint, Flask
from sqlalchemy.sql import text
from TheSmack.users.user import user_create
from TheSmack.users.custom import apology, convert
from flask_sqlalchemy import SQLAlchemy


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
success_bp = Blueprint('success', __name__,
                       template_folder='templates')

app = Flask(__name__)

# database setup
dbURI = 'sqlite:///TheSmack.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = dbURI
db = SQLAlchemy(app)
db.init_app(app)


@usermenu_bp.route('/')
def usermenu():
    return "Sign up/Login menu page"

@profile_bp.route('/')
def profile():
    return "Profile page"

@signup_bp.route('/' , methods = ['POST', 'GET'])
def signup():
    """Register user"""
    if request.method == "POST":
        print("posting")
        
        # Make sure they put in their username
        if not request.form.get("username"):
            return apology("must provide username", 403)
        # Make sure they put in a password
        elif not request.form.get("password"):
            return apology("must provide password", 403)
        # Make sure the passwords match
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("passwords must match", 403)

        #get username and password from form
        username = request.form['username']
        password = request.form['password']
        bio = request.form['bio']
        #calls user_create function from user.py
        user_create(username, password, bio)

        return render_template("/users/profile.html")
    else:
        return render_template("/users/signup.html")

@success_bp.route('/')
def success():
    return render_template('/users/success.html')

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
