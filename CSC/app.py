from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Create database
def init_db():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS appointments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        phone TEXT,
        email TEXT,
        service TEXT,
        date TEXT,
        message TEXT
    )
    """)
    conn.commit()
    conn.close()

init_db()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/income")
def income():
    return render_template("income.html")

@app.route("/pan")
def pan():
    return render_template("pan.html")

@app.route("/EWS")
def caste():
    return render_template("EWS.html")

@app.route("/domocile")
def domocile():
    return render_template("domocile.html")

@app.route("/non-creamy-layer")
def non_creamy_layer():
    return render_template("non-creamy-layer.html")

@app.route("/birth")
def birth():
    return render_template("birth.html")

@app.route("/death")
def death():
    return render_template("death.html")

@app.route("/senior")
def senior():
    return render_template("senior.html")

@app.route("/affidavit")
def affidavit():
    return render_template("affidavit.html")


@app.route("/contact", methods=["GET","POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        phone = request.form["phone"]
        email = request.form["email"]
        service = request.form["service"]
        date = request.form["date"]
        message = request.form["message"]

        conn = sqlite3.connect("database.db")
        cur = conn.cursor()
        cur.execute("""
        INSERT INTO appointments(name, phone, email, service, date, message)
        VALUES (?,?,?,?,?,?)
        """, (name, phone, email, service, date, message))
        conn.commit()
        conn.close()

        return "<h2>Appointment Submitted Successfully!</h2>"

    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
