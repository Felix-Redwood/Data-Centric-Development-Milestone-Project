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
    return render_template("index.html", elements=mongo.db.story_elements.find().limit(10))

@app.route('/important_home', methods=['POST'])
def important_home():
    return render_template("indeximportant.html", elements=mongo.db.story_elements.find( {'important': True} ).limit(10))

@app.route('/toggle_element_important_home/<element_id>', methods=['POST'])
def toggle_element_important_home(element_id):
    importantbool = mongo.db.story_elements.find({'_id': ObjectId(element_id)})
    if importantbool({'important': True}):
        mongo.db.story_elements.updateOne(
       {'_id': ObjectId(element_id)},
       {'$set': { "important.$" : False }}
        )
    else:
        mongo.db.story_elements.updateOne(
       {'_id': ObjectId(element_id)},
       {'$set': { "important.$" : True }}
        )
    return render_template("index.html", elements=mongo.db.story_elements.find().limit(10))

@app.route('/nav_elements', methods=['POST', 'GET'])
def nav_elements():
    return render_template("elements.html", elements=mongo.db.story_elements.find())

@app.route('/important_elements', methods=['POST'])
def important_elements():
    return render_template("importantelements.html", elements=mongo.db.story_elements.find( {'important': True} ))

@app.route('/toggle_element_important_elements/<element_id>', methods=['POST'])
def toggle_element_important_elements(element_id):
    importantbool = mongo.db.story_elements.find({'_id': ObjectId(element_id)})
    if importantbool({'important': True}):
        mongo.db.story_elements.updateOne(
       {'_id': ObjectId(element_id)},
       {'$set': { "important.$" : False }}
        )
    else:
        mongo.db.story_elements.updateOne(
       {'_id': ObjectId(element_id)},
       {'$set': { "important.$" : True }}
        )
    return render_template("elements.html", elements=mongo.db.story_elements.find())


@app.route('/nav_categories', methods=['POST', 'GET'])
def nav_categories():
    subcategories = mongo.db.subcategories.find()
    categories=mongo.db.categories.find()
    subcat_name = str(mongo.db.subcategories.category_name)
    cat_name = str(mongo.db.categories.category_name)
    return render_template("categories.html", categories=mongo.db.categories.find(), subcategories=mongo.db.subcategories.find(), cat_name=cat_name, subcat_name=subcat_name)

@app.route('/insert_category', methods=['POST'])
def insert_category():
    categories = mongo.db.categories
    category_doc = ({"category_name": request.form.get('category_name')},
                    {"category_description": request.form.get('category_description')})
    categories.insert_one(category_doc)
    return redirect(url_for('nav_categories'))

@app.route('/add_category')
def add_category():
    return render_template('addcategory.html')

@app.route('/delete_category/<category_id>')
def delete_category(category_id):
    mongo.db.categories.remove({'_id': ObjectId(category_id)})
    return redirect(url_for('nav_categories'))

@app.route('/nav_subcategories', methods=['POST', 'GET'])
def nav_subcategories():
    return render_template("subcategories.html", subcategories=mongo.db.subcategories.find())

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), port=int(os.environ.get('PORT')), debug=True)

