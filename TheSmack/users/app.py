from flask import Blueprint

usermenu_bp = Blueprint('usermenu', __name__,
                          template_folder='templates',
                          static_folder='static', static_url_path='assets')
signup_bp = Blueprint('signup', __name__,)

# not sure if we need to identify static and template folder for all bp
login_bp = Blueprint('login', __name__,)


@usermenu_bp.route('/')
def usermenu():
    return "Sign up/Login menu page"

@signup_bp.route('/')
def signup():
    return "Signup page"

@login_bp.route('/')
def login():
    return "Login page"