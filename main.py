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

#from flask_socketio import SocketIO



app = Flask(__name__)

#socketio = SocketIO(app)


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
@app.route('/', methods=['GET','POST'])
def generator():
    most_recent_smack = Guest.query.order_by(Guest.post_id.desc()).first()
    # call to random joke web api
    url = 'https://official-joke-api.appspot.com/jokes/programming/random'
    response = requests.get(url)
    # formatting variables from return
    setup = response.json()[0]['setup']
    punchline = response.json()[0]['punchline']
    url = 'https://www.boredapi.com/api/activity'
    response = requests.get(url)
    st = response.json()
    type = st['type']
    activity = st['activity']
    return render_template("home.html", recent=most_recent_smack, setup=setup, punchline=punchline, type=type, activity=activity)

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


def messageReceived(methods=['GET', 'POST']):
    print('message  received.')

#@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    #socketio.emit('my response', json, callback=messageReceived)



if __name__ == "__main__":
    app.run(port='3000', host='127.0.0.1')