from flask import Blueprint, request, jsonify, redirect, session, flash
from flask import render_template, url_for
import re
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
        # grab email and password from user
        email = request.form["signupEmail"]
        password = request.form["signupPassword"]
        confirmPassword = request.form["signupConfirmPassword"]

        # regex for email and password
        emailFormat = '^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$'
        passwordFormat = '^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$'
        
        # confirm email matches format
        if not re.search(emailFormat, email):
            ### return invalid email format
            return "<h1> Failed Email </h1>"
        # confirm password matches format
        if not re.search(passwordFormat, password):
            ### return invalid password format
            return "<h1> Failed Password </h1>"
        # validate that password and the confirm password are the same
        if confirmPassword != password:
            return "<h1> Passwords dont match </h1>"

        ### make request to db for account creation and send email verification

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