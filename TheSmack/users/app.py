from flask import render_template, request, Blueprint, Flask,redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from TheSmack.users.user import user_create, validate_user
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
logout_bp = Blueprint('logout', __name__,
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


@login_bp.route('/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        #username and password variables from form
        username = request.form['username']
        password = request.form['password']
        #just to check if username and password was collected
        print(username +" " + password)
        #calls validate_user function from user.py
        user = validate_user(username, password)

        if user:
            #if validate_user = true, log user in and return profile.html template
            login_user(user)
            db.session.commit()
            return render_template("users/profile.html")
    else:
        print('Bar')
        #if validate_user = false, return login page
    return render_template("/users/login.html")


@logout_bp.route('/')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home.html'))