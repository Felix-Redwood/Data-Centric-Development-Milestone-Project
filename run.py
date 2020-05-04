# This file contains the functions that render the templates in the 'templates'
# directory. These functions also pass through values, such as 'elements' or
# 'categories' that help to render elements in each page.

import os
import json

from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)


def import_mongouri():
    """If there is an env.py file containing the MONGO_URI, then the MONGO_URI
    will be provided from that. If not, the program will search the local
    environment for the MONGO_URI."""
    if os.path.exists("env.py"):
        import env
        app.config["MONGO_URI"] = env.MONGO_URI
    else:
        app.config["MONGO_URI"] = os.environ.get('MONGO_URI')


import_mongouri()


app.config["MONGO_DBNAME"] = 'story_database'


mongo = PyMongo(app)


"""Error Handler - Redirects to 404.html upon a 404 error."""

@app.errorhandler(404)
def page_not_found(e):
    print("error 404, page not found")
    return render_template('404.html'), 404


"""Homepage."""

@app.route('/')
@app.route('/nav_home', methods=['POST', 'GET'])
def nav_home():
    return render_template("index.html",
                            elements=mongo.db.story_elements.find().limit(10))


@app.route('/important_home', methods=['POST'])
def important_home():
    return render_template("indeximportant.html",
                            elements=mongo.db.story_elements.find({'important': True}).limit(10))


@app.route('/toggle_element_important_home/<element_id>', methods=['POST'])
def toggle_element_important_home(element_id):
    print(element_id)
    importantbool = mongo.db.story_elements.find_one({'_id': ObjectId(element_id)})
    """The importantbool variable contains the 'important' status of the element,
    which is a boolean. When a user switches an element's 'important' status,
    this function changes that boolean in the MongoDB database and reloads
    the page."""
    if importantbool['important'] is True:
        mongo.db.story_elements.update_one(
       {'_id':ObjectId(element_id)},
       {'$set':{"important":False}}
        )
    else:
        mongo.db.story_elements.update_one(
       {'_id':ObjectId(element_id)},
       {'$set':{"important":True}}
        )
    assert type(importantbool['important']) is bool, "'important' not stored as Boolean"
    return render_template("index.html",
                            elements=mongo.db.story_elements.find().limit(10))


@app.route('/delete_element_home/<element_id>')
def delete_element_home(element_id):
    mongo.db.story_elements.remove({'_id': ObjectId(element_id)})
    return redirect(url_for('nav_home'))


"""Elements Page."""

@app.route('/nav_elements', methods=['POST', 'GET'])
def nav_elements():
    return render_template("element/elements.html",
                            elements=mongo.db.story_elements.find())


@app.route('/important_elements', methods=['POST'])
def important_elements():
    return render_template("element/important.html",
                            elements=mongo.db.story_elements.find( {'important': True} ))


@app.route('/toggle_element_important_elements/<element_id>', methods=['POST'])
def toggle_element_important_elements(element_id):
    importantbool = mongo.db.story_elements.find_one({'_id': ObjectId(element_id)})
    if importantbool['important'] == True:
        mongo.db.story_elements.update_one(
       {'_id': ObjectId(element_id)},
       {'$set': { "important" : False }}
        )
    else:
        mongo.db.story_elements.update_one(
       {'_id': ObjectId(element_id)},
       {'$set': { "important" : True }}
        )
    assert type(importantbool['important']) is bool, "'important' not stored as Boolean"
    return render_template("element/elements.html", elements=mongo.db.story_elements.find())


@app.route('/edit_element/<element_id>')
def edit_element(element_id):
    selected_element = mongo.db.story_elements.find_one({"_id": ObjectId(element_id)})
    all_categories = mongo.db.categories.find()
    all_subcategories = mongo.db.subcategories.find()
    return render_template("element/edit.html",
                            element=selected_element,
                            categories=all_categories,
                            subcategories=list(all_subcategories))


@app.route('/update_element/<element_id>', methods=['POST'])
def update_element(element_id):
    """As 'important' is a boolean, this 'if' function checks whether the
    'important' toggle is on or not, and sets the value of a variable named
    'important' accordingly."""
    if request.form.get('important') == 'on':
        important = True
    else:
        important = False
    elements = mongo.db.story_elements
    elements.update({'_id': ObjectId(element_id)},
    {
     'category_name':request.form.get('category_name'),
     'subcategory':request.form.get('subcategory'),
     'element_name':request.form.get('element_name'),
     'element_vignette':request.form.get('element_vignette'),
     'element_description':request.form.get('element_description'),
     'events':request.form.get('events'),
     'misc':request.form.get('misc'),
     'important':(important)
    })
    assert type(important) is bool, "'important' not stored as Boolean"
    return redirect(url_for('nav_elements'))


@app.route('/insert_element', methods=['POST'])
def insert_element():
    elements = mongo.db.story_elements
    """Here we use to_dict, to ensure that the forms contents are in a format
    that MongoDB can read."""
    elements.insert_one(request.form.to_dict())
    return redirect(url_for('nav_elements'))


@app.route('/add_element')
def add_element():
    return render_template('element/add.html',
                            categories=list(mongo.db.categories.find()),
                            subcategories=list(mongo.db.subcategories.find()))


@app.route('/delete_element/<element_id>')
def delete_element(element_id):
    mongo.db.story_elements.remove({'_id': ObjectId(element_id)})
    return redirect(url_for('nav_elements'))


"""Categories Page."""

@app.route('/nav_categories', methods=['POST', 'GET'])
def nav_categories():
    return render_template("category/categories.html",
                            categories=list(mongo.db.categories.find()),
                            subcategories=list(mongo.db.subcategories.find()))


@app.route('/insert_category', methods=['POST'])
def insert_category():
    categories = mongo.db.categories
    categories.insert_one(request.form.to_dict())
    return redirect(url_for('nav_categories'))


@app.route('/add_category')
def add_category():
    return render_template('category/add.html')


@app.route('/edit_category/<category_id>')
def edit_category(category_id):
    selected_category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("category/edit.html", category=selected_category)


@app.route('/update_category/<category_id>', methods=['POST'])
def update_category(category_id):
    categories = mongo.db.categories
    categories.update( {'_id': ObjectId(category_id)},
    {
     'category_name':request.form.get('category_name'),
     'category_description':request.form.get('category_description')
    })
    return redirect(url_for('nav_categories'))


@app.route('/delete_category/<category_id>')
def delete_category(category_id):
    mongo.db.categories.remove({'_id': ObjectId(category_id)})
    return redirect(url_for('nav_categories'))


"""Subcategories Page."""

@app.route('/nav_subcategories', methods=['POST', 'GET'])
def nav_subcategories():
    return render_template("subcategory/subcategories.html",
                            subcategories=mongo.db.subcategories.find())


@app.route('/insert_subcategory', methods=['POST'])
def insert_subcategory():
    subcategories = mongo.db.subcategories
    subcategories.insert_one(request.form.to_dict())
    return redirect(url_for('nav_subcategories'))


@app.route('/add_subcategory')
def add_subcategory():
    return render_template('subcategory/add.html',
                            categories=mongo.db.categories.find())


@app.route('/edit_subcategory/<subcategory_id>')
def edit_subcategory(subcategory_id):
    selected_subcategory = mongo.db.subcategories.find_one({"_id": ObjectId(subcategory_id)})
    all_categories = mongo.db.categories.find()
    assert type() is bool, "'important' not stored as Boolean"
    return render_template("subcategory/edit.html",
                            subcategory=selected_subcategory,
                            categories=all_categories)


@app.route('/update_subcategory/<subcategory_id>', methods=['POST'])
def update_subcategory(subcategory_id):
    subcategories = mongo.db.subcategories
    subcategories.update( {'_id': ObjectId(subcategory_id)},
    {
     'category_name':request.form.get('category_name'),
     'subcategory':request.form.get('subcategory'),
     'subcategory_description':request.form.get('subcategory_description')
    })
    return redirect(url_for('nav_subcategories'))


@app.route('/delete_subcategory/<subcategory_id>')
def delete_subcategory(subcategory_id):
    mongo.db.subcategories.remove({'_id': ObjectId(subcategory_id)})
    return redirect(url_for('nav_subcategories'))


"""Search Results Page."""

@app.route('/search_results', methods=['POST', 'GET'])
def search_results():
    """This function queries the story_database text indexes in MongoDB. It
    takes the search_inquiry, i.e the text sent through the search form and
    searches through the text in each index."""
    categories_results = mongo.db.categories.find({'$text': {'$search':request.form.get('search_inquiry')}})
    subcategories_results = mongo.db.subcategories.find({'$text': {'$search':request.form.get('search_inquiry')}})
    elements_results = mongo.db.story_elements.find({'$text': {'$search':request.form.get('search_inquiry')}})
    return render_template("searchresults.html",
                        categories=list(categories_results),
                        subcategories=list(subcategories_results),
                        elements=list(elements_results))

"""Help Page."""

@app.route('/nav_help')
def nav_help():
    return render_template("help.html")

"""Miscellaneous"""

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), port=int(os.environ.get('PORT')), debug=True)