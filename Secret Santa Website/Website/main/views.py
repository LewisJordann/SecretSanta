from Website.models.User import User
from Website.models.Event import Event
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
            account = User(request.form["loginEmail"], request.form["loginPassword"], None)
            user = auth.sign_in_with_email_and_password(account.email, account.password)
            session['user'] = account.email
            return redirect(url_for("views.events"))
        except:
            flash("We couldn't log you in. Please check your email and password and try again.","info")
            return redirect(url_for("views.login"))
    else:
        # if user exists in cookies, stay signed in
        if "user" in session:
            return redirect(url_for("views.events"))
        else:
            return render_template("login.html")

@views.route('/register', methods=["POST", "GET"])
def register():
    if request.method == 'POST':
        # grab email, password, and confirmPassword from user and store in object
        account = User(request.form["signupEmail"], request.form["signupPassword"], request.form["signupConfirmPassword"])
        
        # confirm email matches format
        if not account.validateEmailSyntax:
            flash("Email does not match proper format.", "info")
            return redirect(url_for("views.register"))

        # confirm password matches format
        if not account.validatePasswordSyntax:
            flash("Password does not follow proper format.", "info")
            return redirect(url_for("views.register"))

        # validate that password and the confirm password are the same
        if account.confirmPassword != account.password:
            flash("Passwords do not match.", "info")
            return redirect(url_for("views.register"))
        
        # create user in firebase and send email confirmation
        try:
            user = auth.create_user_with_email_and_password(account.email, account.password)
            auth.send_email_verification(user['idToken'])
            flash("Account verification has been sent to your email.", "info")
            return redirect(url_for("views.login"))
        except:
            flash("An Error has occurred with registering.","info")
            return redirect(url_for("views.register"))

    else:
        return render_template("register.html")

@views.route('/forgotpassword', methods=["POST", "GET"])
def forgotPassword():
    if request.method == 'POST':
        email = request.form["Email"]
        auth.send_password_reset_email(email)
        flash("Check your email to reset your password.", "info")
        return render_template("forgotpasswordsent.html")
    else:
        return render_template("forgotpassword.html")

@views.route('/events')
def events():
    if "user" in session:
        usr = session["user"]
        # grab info from firebase and store it in a object list

        # pass object list to html page through render_template
        # https://stackoverflow.com/questions/45558349/flask-display-database-from-python-to-html
        return render_template("events.html")
    else:
        return redirect(url_for("views.login"))

@views.route('/logout')
def logout():
    session.pop("user", None)
    flash("You have logged out.", "info")
    return redirect(url_for("views.login"))