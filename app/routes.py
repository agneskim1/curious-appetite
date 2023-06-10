from flask import Blueprint, make_response, jsonify, abort, request, render_template
from app import db
from app.models.recipe import Recipe
import os
import requests
import json


recipes_bp = Blueprint("recipe", __name__, url_prefix= "/recipes")
def validate_input(input):
    try: 
        input.isalpha()
    except:
        abort(make_response({"details": "Invalid Data"}, 400))
    
    return str(input.capitalize())

@recipes_bp.route("/")
def welcome():
    ingredient = request.args.get("ingredient")
    if ingredient:
        return get_recipe_search(ingredient)
    else:
        return render_template('index.html')

def get_recipe_search(ingredient):
    path= "https://api.edamam.com/search"

    app_key= os.environ.get('API_KEY')
    app_id= os.environ.get('API_ID')
    q = validate_input(ingredient)
    
    recipe_list= []
    response = requests.get(f"https://api.edamam.com/search?q={q}&app_id={app_id}&app_key={app_key}")
    recipes_hits = response.json()["hits"]


    for recipe in recipes_hits: 
        recipe_list.append(recipe["recipe"])

    return render_template("recipes.html", recipes=recipe_list, ingredient=q)


