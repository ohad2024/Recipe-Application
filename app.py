from flask import Flask, render_template, request
from dataclasses import dataclass
import sqlite3

app = Flask(__name__)

@dataclass
class Recipe:
    id: int
    title: str
    ingredients: str
    instructions: str
    

def get_db_connection():
    conn = sqlite3.connect('recipes.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    recipes = conn.execute('SELECT * FROM recipes').fetchall()
    conn.close()
    return render_template('index.html', recipes=recipes)

@app.route('/<int:recipe_id>')
def recipe(recipe_id):
    conn = get_db_connection()
    recipe = conn.execute('SELECT * FROM recipes WHERE id = ?', (recipe_id,)).fetchone()
    conn.close()
    return render_template('recipe.html', recipe=recipe)

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_term = request.form['search']
        conn = get_db_connection()
        recipes = conn.execute('SELECT * FROM recipes WHERE ingredients LIKE ?', ('%' + search_term + '%',)).fetchall()
        conn.close()
        return render_template('search.html', recipes=recipes, search_term=search_term)
    return render_template('search.html', recipes=[])

if __name__ == '__main__':
    app.run(debug=True)
