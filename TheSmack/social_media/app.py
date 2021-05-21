from flask import Blueprint, render_template, request, app, redirect, url_for
from flask_login import LoginManager,login_required, current_user, logout_user
from TheSmack.social_media.post import post_create
from TheSmack.social_media.guest import guest_create



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
guestSmack_bp = Blueprint('anonSmack', __name__,
                         template_folder='templates',
                         static_folder='static')


@login_required
def logout():
    logout_user()
    return redirect(url_for('home.html'))

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

@guestSmack_bp.route('/', methods=['POST', 'GET'])
def GuestSmack():
    if request.method == 'POST':
        name = request.form['name']
        emotion = request.form['emotion']
        update = request.form['update']
        guest_create(name, emotion, update)
        return render_template("/media/smacks.html")
    else:
        print('bar')
    return render_template("/media/smackPost_guest.html")



@smackDM_bp.route('/')
def smackDM():
    return "Smack(DM) someone"



