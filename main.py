from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from TheSmack.users.app import usermenu_bp, signup_bp, login_bp
from TheSmack.social_media.app import trending_bp, createSmack_bp, smackDM_bp


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

#home page route
@app.route('/')
def home():
    return render_template("home.html")



if __name__ == "__main__":
    app.run(port='3000', host='127.0.0.1')