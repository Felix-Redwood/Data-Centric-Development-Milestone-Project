import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'story_database'
app.config["MONGO_URI"] = env.MONGO_URI

mongo = PyMongo(app)

@app.route('/')
@app.route('/nav_home')
def nav_home():
    return render_template("index.html", elements=mongo.db.story_elements.find())

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), port=int(os.environ.get('PORT')), debug=True)