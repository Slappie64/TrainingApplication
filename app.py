
# =================================================================
# Description
# # This is the entry point of the application and routing management.
# =================================================================

# =================================================================
# Imports                                                         #
# =================================================================
# # sqlite3 - Implements a small, fast, self-contained, SQL database engine
# # Flask - Flask is a micro web framework written in Python
# # werkzeug - A comprehensive WSGI web application library.
import sqlite3
from flask import Flask, render_template
from werkzeug.exceptions import abort


# =================================================================
# Functions                                                       #
# =================================================================
# get_db_connection()
# # Connects to the database and returns a var containing the database rows.
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# get_posts()
# # Uses the database connection to select all posts where id = post_id
# # Selects the first post and returns that object.
# # If none returned abort with a 404 error.
def get_posts(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?', (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post

# =================================================================
# Application Specific                                            #
# =================================================================
# # Assign Flask(__name__) to app for better readability
app = Flask(__name__)


# =================================================================
# Flask Routes                                                    #
# =================================================================
# # Index: Home Page
# # Loading the page creates a connection to the database, fetches all posts
# # and then loads each into the index.html template.
@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)

# # Blog: Page specifically for blog posts
# # Currently just a holding item for the menu.
# # Returns a simple string 'Blog Page'.
@app.route('/blog/')
def blog():
    return 'Blog Page'