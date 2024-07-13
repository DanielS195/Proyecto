from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_bootstrap import Bootstrap
from datetime import timedelta
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__, static_url_path='/static')
Bootstrap(app)
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(minutes=5)

# Configuración de la base de datos
client = MongoClient('mongodb://localhost:27017/')
db = client['user_db']
users = db['users']

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user = users.find_one({"email": email})
        if user and check_password_hash(user["password"], password):
            session["user"] = user["name"]
            session["email"] = user["email"]
            return redirect(url_for("user_dashboard"))
        else:
            flash("Login Unsuccessful. Please check your email and password")
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        users.insert_one({
            "name": name,
            "email": email,
            "password": hashed_password
        })
        flash("Registration Successful!")
        return redirect(url_for("login"))
    return render_template("register.html")

@app.route("/user_dashboard")
def user_dashboard():
    if "email" in session:
        email = session["email"]
        user = users.find_one({"email": email})
        return render_template("user_dashboard.html", user=user)
    else:
        return redirect(url_for("login"))

@app.route("/admin")
def admin():
    if "email" in session and session["email"] == "admin@example.com":
        all_users = users.find()
        return render_template("admin_dashboard.html", users=all_users)
    else:
        flash("You are not authorized to view this page")
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("user", None)
    session.pop("email", None)
    flash("You have been logged out!")
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
