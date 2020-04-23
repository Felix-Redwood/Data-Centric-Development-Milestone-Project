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
    print(element_id)
    importantbool = mongo.db.story_elements.find_one({'_id': ObjectId(element_id)})
    print(importantbool)
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
    return render_template("index.html", elements=mongo.db.story_elements.find().limit(10))

@app.route('/delete_element_home/<element_id>')
def delete_element_home(element_id):
    mongo.db.story_elements.remove({'_id': ObjectId(element_id)})
    return redirect(url_for('nav_home'))

@app.route('/nav_elements', methods=['POST', 'GET'])
def nav_elements():
    return render_template("elements.html", elements=mongo.db.story_elements.find())

@app.route('/important_elements', methods=['POST'])
def important_elements():
    return render_template("importantelements.html", elements=mongo.db.story_elements.find( {'important': True} ))

@app.route('/toggle_element_important_elements/<element_id>', methods=['POST'])
def toggle_element_important_elements(element_id):
    importantbool = mongo.db.story_elements.find({'_id': ObjectId(element_id)})
    if importantbool['important'] == True:
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

@app.route('/edit_element/<element_id>')
def edit_element(element_id):
    selected_element = mongo.db.story_elements.find_one({"_id": ObjectId(element_id)})
    all_categories = mongo.db.categories.find()
    all_subcategories = mongo.db.subcategories.find()
    return render_template("editelement.html", element=selected_element, categories=all_categories, subcategories=all_subcategories)

@app.route('/update_element/<element_id>', methods=['POST'])
def update_element(element_id):
    elements = mongo.db.story_elements
    elements.update( {'_id': ObjectId(element_id)},
    {
     'category_name':request.form.get('category_name'),
     'subcategory':request.form.get('subcategory'),
     'element_name':request.form.get('element_name'),
     'element_vignette':request.form.get('element_vignette'),
     'element_description':request.form.get('element_description'),
     'events':request.form.get('events'),
     'misc':request.form.get('misc'),
     'important':request.form.get('important')
    })
    return redirect(url_for('nav_elements'))

@app.route('/delete_element/<element_id>')
def delete_element(element_id):
    mongo.db.story_elements.remove({'_id': ObjectId(element_id)})
    return redirect(url_for('nav_elements'))

@app.route('/nav_categories', methods=['POST', 'GET'])
def nav_categories():
    return render_template("categories.html", categories=mongo.db.categories.find(), subcategories=mongo.db.subcategories.find())

@app.route('/insert_category', methods=['POST'])
def insert_category():
    categories = mongo.db.categories
    categories.insert_one(request.form.to_dict())
    return redirect(url_for('nav_categories'))

@app.route('/add_category')
def add_category():
    return render_template('addcategory.html')

@app.route('/edit_category/<category_id>')
def edit_category(category_id):
    selected_category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("editcategory.html", category=selected_category)

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

@app.route('/nav_subcategories', methods=['POST', 'GET'])
def nav_subcategories():
    return render_template("subcategories.html", subcategories=mongo.db.subcategories.find())

@app.route('/insert_subcategory', methods=['POST'])
def insert_subcategory():
    subcategories = mongo.db.subcategories
    subcategories.insert_one(request.form.to_dict())
    return redirect(url_for('nav_subcategories'))

@app.route('/add_subcategory')
def add_subcategory():
    return render_template('addsubcategory.html', categories=mongo.db.categories.find())

@app.route('/edit_subcategory/<subcategory_id>')
def edit_subcategory(subcategory_id):
    selected_subcategory = mongo.db.subcategories.find_one({"_id": ObjectId(subcategory_id)})
    all_categories = mongo.db.categories.find()
    return render_template("editsubcategory.html", subcategory=selected_subcategory, categories=all_categories)

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

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), port=int(os.environ.get('PORT')), debug=True)

