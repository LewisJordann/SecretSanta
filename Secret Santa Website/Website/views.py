from flask import Blueprint, request, jsonify, redirect, session, flash
from flask import render_template, url_for
views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/login', methods=["POST", "GET"])
def login():
    if request.method == 'POST':
        # get input from html form
        ### make request to db to verify account exists
        usrEmail = request.form["email"]
        session["usrEmail"] = usrEmail
        return redirect(url_for("views.success"))
    else:
        if "useEmail" in session:
            return redirect(url_for("views.success"))
        return render_template("login.html")

@views.route('/register', methods=["POST", "GET"])
def register():
    if request.method == 'POST':
        ### verify password meets requirements
        ### send request to db and create account
        ### send email verification
        pass
    return render_template("register.html")

@views.route('/success')
def success():
    if "usrEmail" in session:
        usr = session["usrEmail"]
        return f"<h1>Hello: {usr}</h1>"
    else:
        return redirect(url_for("views.login"))

@views.route('/logout')
def logout():
    session.pop("usrEmail", None)
    return redirect(url_for("views.login"))