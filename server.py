from jinja2 import StrictUndefined
from flask import Flask, render_template, redirect, request, flash, session

from flask_debugtoolbar import DebugToolbarExtension

from model import User, City, Recommendation, Stay, Eat, Do, connect_to_db, db

app = Flask(__name__)

app.secret_key = "ABC"

#######################################################################



@app.route('/')
def index():
    """Homepage"""
    return render_template('homepage.html')



@app.route('/login')
def login_form():
    """show login form"""
    return render_template('login_form.html')



@app.route('/login', methods=['POST'])
def login_process():
    """process login form"""

    #get username & password entered by user in login template
    username = request.form.get('username')
    password = request.form.get('password')

    #will need to check database for username, then if that fits check that username & password are equal
    user = User.query.filter_by(username = username).first()

    #if username doesnt exist send to register page
    if not user:
        return redirect('/register')

    #if password is wrong flash incorrect password
    elif password != user.password:
        flash('Incorrect password')
        return redirect('/login')

    #if they are then add to session 
    else:
        session['username'] = username
        return redirect('login')

@app.route('/register')
def reg_form():
    """show register form"""
    return render_template('reg_form.html')

@app.route('/register', methods=['POST'])
def reg_process():
    """process registration"""

    username = request.form.get('username')
    password = request.form.get('password')
    fname = request.form.get('fname')
    lname = request.form.get('lname')
    email = request.form.get('email')

    #if username is not already in database add
    if not User.query.filter_by(username = username).all():
        new_user = User(username=username, password=password, f_name=fname, l_name=lname, email=email)
        db.session.add(new_user)
        db.session.commit()

    return redirect('/')


##############################################################

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True
    # make sure templates, etc. are not cached in debug mode
    app.jinja_env.auto_reload = app.debug

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(port=5001, host='0.0.0.0')


