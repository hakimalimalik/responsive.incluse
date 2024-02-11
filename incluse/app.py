from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/waitlist", methods=["POST"])
def waitlist():
    # Extract form data
    name = request.form.get("name")
    email = request.form.get("email")
    university = request.form.get("university")

    # Connect to the SQLite database
    conn = sqlite3.connect('waitlist.db')
    cursor = conn.cursor()

    # Create the 'users' table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            university TEXT
        )
    ''')

    # Insert data into the 'users' table
    cursor.execute("INSERT INTO users (name, email, university) VALUES (?, ?, ?)", (name, email, university))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

    # Return appropriate response
    if not name:
        return render_template("failure.html")
    return render_template("success.html")

if __name__ == "__main__":
    # Use the 0.0.0.0 host to make the Flask app accessible externally
    # Get the port number from the PORT environment variable, default to 5000 if not set
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
