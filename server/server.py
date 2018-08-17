from flask import Flask, render_template

# App
from configure import app

# MongoDB
from pymongo import MongoClient
client = MongoClient()
db = client.flashcards

# Endpoints
from endpoints import signup_endpoints

app.register_blueprint(signup_endpoints.endpoints)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
