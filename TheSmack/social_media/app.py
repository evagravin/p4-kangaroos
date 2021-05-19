from flask import Blueprint, render_template, request
from TheSmack.social_media.post import post_create


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

aboutus_bp = Blueprint('aboutus', __name__,
                       template_folder='templates',
                       static_folder='static')
smackmenu_bp = Blueprint('smackmenu', __name__,
                         template_folder='templates',
                         static_folder='static')

@aboutus_bp.route('/')
def aboutus():
    return render_template ("digitalPortfolios.html")

@smackmenu_bp.route('/')
def smackmenu():
    return render_template("smackMenu.html")


@trending_bp.route('/')
def trending():
    return "Trending Page"

@searchresults_bp.route('/')
def results():
    return "Search results page"

@createSmack_bp.route('/', methods=['POST', 'GET'])
#@login_required
def createSmack():
    if request.method == 'POST':
        emotion = request.form['emotion']
        update = request.form['update']
        post_create(username, emotion, update)
        return render_template("/users/profile.html")
    else:
        print('bar')
    return render_template("/media/smackPost.html")


@smackDM_bp.route('/')
def smackDM():
    return "Smack(DM) someone"



