from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from TheSmack.users.app import signup_bp

app = Flask(__name__)

# database setup
dbURI = 'sqlite:///chess.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = dbURI
db = SQLAlchemy(app)
db.init_app(app)


app = Flask(__name__)
app.register_blueprint(signup_bp, url_prefix='/signup')



#home page route
@app.route('/')
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(port='3000', host='127.0.0.1')