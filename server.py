from jinja2 import StrictUndefined
from flask import (Flask, render_template, redirect, request, flash, session)
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.secret_key = "ABC"

app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    """Homepage"""
    return render_template('homepage.html')

@app.route('/login')
def login_form():
    """show login form"""
    return render_template('login_form.html')

@app.route('/login', methods=[POST])
def login_process():
    """process login form"""

    #get username & password entered by user in login template
    username = request.form.get('username')
    password = request.form.get('password')

    #will need to check database once seeded by username, then if that fits check that username & password are equal

    #if username doesnt exist send to register page

    #if password is wrong flash incorrect password

    #if they are then add to session 

