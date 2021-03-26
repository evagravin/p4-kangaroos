from flask import Blueprint



trending_bp = Blueprint('trending', __name__,
                        template_folder='templates',
                        static_folder='static')

createSmack_bp = Blueprint('createSmack', __name__,
                        template_folder='templates',
                        static_folder='static')

smackDM_bp = Blueprint('smackDM', __name__,
                           template_folder='templates',
                           static_folder='static')

searchresults_bp = Blueprint('searchresults', __name__,
                       template_folder='templates',
                       static_folder='static')


@trending_bp.route('/')
def trending():
    return "Trending Page"

@searchresults_bp.route('/')
def results():
    return "Search results page"


@createSmack_bp.route('/')
def createSmack():
    return "Create a Smack page"

@smackDM_bp.route('/')
def smackDM():
    return "Smack(DM) someone"



