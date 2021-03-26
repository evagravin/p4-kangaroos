from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from TheSmack.users.app import usermenu_bp, signup_bp, login_bp, profile_bp
from TheSmack.social_media.app import trending_bp, createSmack_bp, smackDM_bp, searchresults_bp, aboutus_bp
from TheSmack.minilabs.app import ava_minilab_bp, risa_minilab_bp, eva_minilab_bp, linda_minilab_bp, minilabMenu_bp


app = Flask(__name__)

# database setup
dbURI = 'sqlite:///TheSmack.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = dbURI
db = SQLAlchemy(app)
db.init_app(app)


app = Flask(__name__)
app.register_blueprint(usermenu_bp, url_prefix='/usermenu')
app.register_blueprint(signup_bp, url_prefix='/signup')
app.register_blueprint(login_bp, url_prefix='/login')
app.register_blueprint(trending_bp, url_prefix='/trending')
app.register_blueprint(createSmack_bp, url_prefix='/createsmack')
app.register_blueprint(smackDM_bp, url_prefix='/smackDM')
app.register_blueprint(profile_bp, url_prefix='/profile')
app.register_blueprint(searchresults_bp, url_prefix='/searchresults')
app.register_blueprint(ava_minilab_bp, url_prefix='/avaminilab')
app.register_blueprint(risa_minilab_bp, url_prefix='/risaminilab')
app.register_blueprint(linda_minilab_bp, url_prefix='/lindaminilab')
app.register_blueprint(eva_minilab_bp, url_prefix='/evaminilab')
app.register_blueprint(minilabMenu_bp, url_prefix='/minilabmenu')
app.register_blueprint(aboutus_bp, url_prefix='/aboutus')

#home page route
@app.route('/')
def home():
    return render_template("home.html")





if __name__ == "__main__":
    app.run(port='3000', host='127.0.0.1')