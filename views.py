from flask import render_template, redirect, url_for, Blueprint, request
from favs import fav_bands, add_to_list # a file I have with data, functions and variables on
# from app import app

my_view = Blueprint('my_view', __name__)

@my_view.route("/")    
def home():
    return render_template('index.html')

@my_view.route("/contact")   # when the url is our_app/contact
def contact():
    return render_template('contact.html') #return contact.html

@my_view.route("/about", methods=["GET", "POST"])   # when the url is our_app/about
def about():
    if request.method == "POST": # if the browser is submitting a post request - almost all submits are POST requests
        new_band=request.form["add_band"] #makes a new variable called new band from the form post
        fav_bands.append(new_band) #perform the function (which we import from my favs.py file and import on line 2) with the paramter new_band which we make on line 18

    return render_template('about.html', fav_bands=fav_bands) #return about.html with this variable taken from my py file favs, which we import on line 2

@my_view.route("/home")   #specifies the url the user would type in for this function to occur
def home_redirect():
    return redirect(url_for("my_view.home"))   #return the url for the home function specified on line 8

@my_view.route("/homepage")
def homeb_redirect():
    return redirect(url_for("my_view.home"))