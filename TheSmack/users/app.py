from flask import Blueprint, render_template

usermenu_bp = Blueprint('usermenu', __name__,
                          template_folder='templates',
                          static_folder='static', static_url_path='assets')
signup_bp = Blueprint('signup', __name__,)

# not sure if we need to identify static and template folder for all bp
login_bp = Blueprint('login', __name__,)


@usermenu_bp.route('/')
def usermenu():
    return "Sign up/Login menu page"

@signup_bp.route('/signup/')
def signup():
    return render_template("signup.html")

@login_bp.route('/login/')
def login():
    return render_template("login.html")


