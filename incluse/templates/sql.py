import sqlite3

# Connect to the SQLite database (this will create the database file if it doesn't exist)
conn = sqlite3.connect('waitlist.db')

# Create a cursor object to execute SQL statements
cursor = conn.cursor()

# Define the schema for the 'users' table
cursor.execute('''
   CREATE TABLE IF NOT EXISTS users (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       name TEXT NOT NULL,
       email TEXT NOT NULL,
       university TEXT
   )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()
