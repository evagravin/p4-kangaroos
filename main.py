from flask import Flask, render_template

app = Flask(__name__)

#home page route
@app.route('/')
def home():
    return render_template("layout.html")

if __name__ == "__main__":
    app.run(port='3000', host='127.0.0.1')