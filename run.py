import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)

def import_mongouri():
    if os.path.exists("env.py"):
        import env
        app.config["MONGO_URI"] = env.MONGO_URI
    else:
        app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

import_mongouri()

app.config["MONGO_DBNAME"] = 'story_database'

mongo = PyMongo(app)

@app.errorhandler(404)
def page_not_found(e):
    print("error 404, page not found")
    return render_template('404.html'), 404

@app.route('/')
@app.route('/nav_home', methods=['POST', 'GET'])
def nav_home():
    return render_template("index.html", elements=mongo.db.story_elements.find())

@app.route('/important_home', methods=['POST'])
def important_home():
    return render_template("indeximportant.html", elements=mongo.db.story_elements.find( {'important': True} ))
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), port=int(os.environ.get('PORT')), debug=True)