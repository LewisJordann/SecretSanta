from flask import Blueprint, request, jsonify, redirect, session, flash
from flask import render_template, url_for
import re
from Website import auth

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/login', methods=["POST", "GET"])
def login():
    if request.method == 'POST':
        try:
            # grab email from form and try and sign in
            usrEmail = request.form["loginEmail"]
            usrPassword = request.form["loginPassword"]
            user = auth.sign_in_with_email_and_password(usrEmail, usrPassword)
            session['user'] = usrEmail
            return redirect(url_for("views.success"))
        except:
            flash("An Error has occurred trying to sign in.","info")
            return redirect(url_for("views.login"))
    else:
        if "user" in session:
            return redirect(url_for("views.success"))
        else:
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
            flash("Email does not match proper format.", "info")
            return redirect(url_for("views.register"))

        # confirm password matches format
        if not re.search(passwordFormat, password):
            flash("Password does not follow proper format.", "info")
            return redirect(url_for("views.register"))

        # validate that password and the confirm password are the same
        if confirmPassword != password:
            flash("Passwords do not match.", "info")
            return redirect(url_for("views.register"))
        
        # create user in firebase and send email confirmation
        try:
            user = auth.create_user_with_email_and_password(email, password)
            auth.send_email_verification(user['idToken'])
            flash("Account verification has been sent to your email.", "info")
            return redirect(url_for("views.login"))
        except:
            flash("An Error has occurred with registering.","info")
            return redirect(url_for("views.register"))

    else:
        return render_template("register.html")

@views.route('/success')
def success():
    if "user" in session:
        usr = session["user"]
        return f"<h1>Hello: {usr}</h1>"
    else:
        return redirect(url_for("views.login"))

@views.route('/logout')
def logout():
    session.pop("user", None)
    flash("You have logged out.", "info")
    return redirect(url_for("views.login"))