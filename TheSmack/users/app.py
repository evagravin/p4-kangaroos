from flask import Blueprint

signup_bp = Blueprint('signup', __name__,
                          template_folder='templates',
                          static_folder='static', static_url_path='assets')


@signup_bp.route('/')
def index():
    return "Sign up page"
