import os
from flask import Flask, render_template, redirect, url_for, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = "cook"
app.config["MONGO_URI"] = os.environ('MONGO_URI')
mongo = PyMongo(app)

#------ recipes ------#

@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    return render_template('recipes.html', recipes=mongo.db.recipes.find())

#------ categories ------#

@app.route('/get_categories')
def get_categories():
    return render_template('home.html',
    categories=mongo.db.categories.find())


if __name__ == "__main__":
    app.run(host=os.environ.get("IP", "0.0.0.0"),
            port=os.environ.get("PORT", "5000"),
            debug=True)