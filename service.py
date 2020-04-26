from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!\n"

@app.route("/user/<username>")
def show_user(username):
    return "User: %s\n" % username