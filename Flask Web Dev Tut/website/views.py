from flask import Blueprint, render_template

#this is a blue print of our site

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")