import requests
from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from TheSmack.users.app import usermenu_bp, signup_bp, login_bp, profile_bp, logout_bp
from TheSmack.social_media.app import createSmack_bp, smackDM_bp, searchresults_bp, aboutus_bp, smackmenu_bp, guestSmack_bp, smacks_bp
from TheSmack.users.user import User
from TheSmack.social_media.guest import Guest
from TheSmack.minilabs.app import minilab_bp
from TheSmack.bubblesort.app import bubblesort_bp
from TheSmack.groups.app import groups_bp
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from TheSmack.social_media.quote import Quotes
import random



app = Flask(__name__)


# database setup
dbURI = 'sqlite:///TheSmack.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = dbURI
db = SQLAlchemy(app)
db.init_app(app)
app.config['SECRET_KEY'] = '5678123'
bootstrap = Bootstrap(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
app.register_blueprint(usermenu_bp, url_prefix='/usermenu')
app.register_blueprint(signup_bp, url_prefix='/signup')
app.register_blueprint(login_bp, url_prefix='/login')
app.register_blueprint(createSmack_bp, url_prefix='/createsmack')
app.register_blueprint(smackDM_bp, url_prefix='/smackDM')
app.register_blueprint(profile_bp, url_prefix='/profile')
app.register_blueprint(searchresults_bp, url_prefix='/searchresults')
app.register_blueprint(minilab_bp, url_prefix='/minilab')
app.register_blueprint(aboutus_bp, url_prefix='/digitalPortfolios')
app.register_blueprint(smackmenu_bp, url_prefix='/smackmenu')
app.register_blueprint(logout_bp, url_prefix='/logout')
app.register_blueprint(bubblesort_bp, url_prefix='/bubblesort')
app.register_blueprint(guestSmack_bp, url_prefix='/guestSmack')
app.register_blueprint(smacks_bp, url_prefix='/smacks')
app.register_blueprint(groups_bp, url_prefix='/groups')


#home page route
@app.route('/', methods=['GET'])
def index():
    most_recent_smack = Guest.query.order_by(Guest.name.desc()).all()
    # call to random quote web api
    url = 'https://api.quotable.io/random'
    response = requests.get(url)
    st = response.json()
    quote = st['content']
    author = st['author']
    return render_template("home.html", recent=most_recent_smack, quote=quote, author=author)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.route('/faq')
def frequently_asked_questions():
    return render_template("/faq.html")

@app.route('/get_quote')
def get_quote():
    id = random.randint(1,34)
    q = Quotes.query.get(id)
    response = jsonify({'Quote': q.Quote})
    return response, 200

if __name__ == "__main__":
    app.run(port='3000', host='127.0.0.1')