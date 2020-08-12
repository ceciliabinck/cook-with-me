import os
from flask import (Flask, render_template, redirect, url_for, request, flash, session)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ['MONGO_DBNAME']
app.config["MONGO_URI"] = os.environ['MONGO_URI']
app.config["SECRET_KEY"] = os.environ['SECRET_KEY']
mongo = PyMongo(app)


@app.route('/')
@app.route('/get_home')
def get_home():
    return render_template('home.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        # check if username already exicts in db
        existing_user = mongo.db.user.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists") 
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "cookbook": request.form.get('cookbook'),
            "email": request.form.get('email')
        }
        mongo.db.user.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registraion Succesfull")
        return redirect(url_for('profile', username=session["user"]))

    return render_template('register.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exicts in db
        existing_user = mongo.db.user.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get('username').lower()
                    flash("Welcome {}", format(request.form.get('user.username')))
                    return redirect(url_for(
                        'profile', username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template('login.html')


@app.route('/profile/<username>', methods=['GET', 'POST'])
def profile(username):
    # grabe the session user from the db
    existing_user = mongo.db.user.find_one({'username': username})

    if session['user']:
        return render_template('profile.html', user=existing_user)

    return redirect(url_for('login'))


@app.route('/logout')
def logout():
    # removes user from session cookies
    flash("You have been logged out")
    session.pop('user')
    return redirect(url_for('login'))

# ------ recipes ------ #


@app.route('/get_recipes')
def get_recipes():
    return render_template('recipes.html', recipes=mongo.db.recipes.find())


@app.route('/add_recipe')
def add_recipe():
    _categories = mongo.db.categories.find()
    category_list = [category for category in _categories]
    return render_template("add_recipe.html", categories=category_list)


@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    flash("Recipe Succesfully Added")
    return redirect(url_for('get_recipes'))


@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_categories = mongo.db.categories.find()
    return render_template('edit_recipe.html', recipe=the_recipe, categories=all_categories)


@app.route('/update_recipe/<recipe_id>', methods=['POST'])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.update( {'_id': ObjectId(recipe_id)},
    {
        'recipe_name': request.form.get('recipe_name'),
        'recipe_description': request.form.get('recipe_description'),
        'cookbook_name': request.form.get('cookbook_name'),
        'recipe_image': request.form.get('recipe_image'),
        'category_name': request.form.get('category_name'),
        'difficulty_level': request.form.get('difficulty_level'),
        'prep_time': request.form.get('prep_time'),
        'cook_time': request.form.get('cook_time'),
        'total_time': request.form.get('total_time'),
        'ingredients': request.form.get('ingredients'),
        'method': request.form.get('method'),
        'tips': request.form.get('tips'),
        'vegetarian': request.form.get('vegetarian')
    })
    flash("Recipe Succesfully Updated")
    return redirect(url_for('get_recipes'))


@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    flash("Recipe Succesfully Deleted")
    return redirect(url_for('get_recipes'))

# ------ categories ------ #


@app.route('/get_categories')
def get_categories():
    categories = list(mongo.db.categories.find().sort("categorie_name", 1))
    return render_template('categories.html', categories=categories)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP", "0.0.0.0"),
            port=os.environ.get("PORT", "5000"),
            debug=True)