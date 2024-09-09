from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db 
#this is a blue print of our site

auth = Blueprint('auth', __name__)

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('pass1')
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfuly', category='success')
            else:
                flash('Incorrect Password', category='error')
        else:
            flash('Email must be greater than 4 characters', category='error')
    return render_template('login.html', boolean=True)

@auth.route('/logout')
def logout():
    return render_template("login.html")

@auth.route('/sign-up', methods = ['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('fname')
        password1 = request.form.get('pass1')
        password2 = request.form.get('pass2')

        if len(email) < 4:
            flash('Email must be greater than 4 characters', category='error')
        elif len(firstName) < 2:
            flash('firstName must be greater than 1 characters', category='error')
        elif password1 != password2:
            flash('Passwords must match', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters', category='error')
        else: 
            # add user to databasegn
            new_user = User(email=email, firstName=firstName, password=generate_password_hash(password1))
            db.session.add(new_user)
            db.session.commit()
            flash('Account Created!', category='success')
            return redirect(url_for("views.home"))
    return render_template("sign_up.html")
