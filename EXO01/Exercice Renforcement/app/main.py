from flask import app

@app.route("/")
@app.route("/home")
def home():
    return "Hello world!"