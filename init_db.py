# =================================================================
# Description
# # The purpose of this module is to initilize the database and add two posts.
# =================================================================

# =================================================================
# Imports                                                         #
# =================================================================
# # sqlite3 - Implements a small, fast, self-contained, SQL database engine
import sqlite3

# =================================================================
# Application Specific                                            #
# =================================================================
# Create a variable for the database connection.
connection = sqlite3.connect('database.db')
# Open the database connection.
with open('schema.sql') as f:
    connection.executescript(f.read())
# Create a variable for the connection cursor.
# This is used to navigate through the database using executed commands.
cur = connection.cursor()

# Use the cursor object to run the command "INSERT INTO posts (title, content) VALUES (?, ?)"
cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)", ('First Post','Content for first post'))
# Use the cursor object to run the command "INSERT INTO posts (title, content) VALUES (?, ?)"
cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)", ('Second Post','Content for second post'))
# Use the cursor object to commit these changes.
connection.commit()
# Use the cursor object to close the database connection.
connection.close()