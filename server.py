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

@app.route('logout')
def log_out():
    """log the user out"""

    session.pop('username', NONE)
    flash('Your are now logged out')
    return redirect('/')


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


@app.route('/search_city')
def city_name_search():

    #request to get city name

    city_name = request.args.get('city_name')
    #pull in object info for that specific city to get city id
    city_obj = City.query.filter_by(city_name=city_name).one()

    #get the user rec object for all cities of that name
    recs = city_obj.recommendations

    return render_template('username_search.html', recs=recs, city_name=city_name)

@app.route('/create_rec')
def create_rec():
    """sends user to the new create page"""
    #if value == 'create':
    return render_template('create_rec.html')
    #else:



@app.route('/create_rec', methods = ['POST'])
def add_rec_to_db():
    """recordes info submitted by user, creates the objects for the db, and adds to the db"""

    # Update session on login
    user_id = session['user_id']

    # Create all of these objects: city, stay, do, eat
    stay = Stay(stay_name= request.form.get('stay_name'), stay_info = request.form.get('stay_info'))
    eat = Eat(eat_name= request.form.get('eat_name'), eat_info = request.form.get('eat_info'))
    do = Do(do_name= request.form.get('do_name'), do_info = request.form.get('do_info'))

    city = City(city_name= request.form.get('city_name'), city_info = request.form.get('city_info'))

    recommendation = Recommendation(rec_name = request.form.get('rec_name'), user_id=user_id)


    #create the objects
    # recomendation = Recommendation(city_name = request.form.get('city_name'), rec_name = request.form.get('rec_name'),
    #                     city_info = request.form.get('city_info'), stay_name = request.form.get('stay_name'), 
    #                     stay_info = request.form.get('stay_info'), eat_name = request.form.get('eat_name'), 
    #                     eat_info = request.form.get('eat_info'), do_name = request.form.get('do_name'),
    #                     do_info = request.form.get('do_info'), user_id=user_id)

    #call the save function to add to the database
    Recommendation.save(recomendation)
    flash("Awesome! You've created a recommendation")
    return redirect('/')
    #return redirect(f'/recommendations/{recommendations.rec_id}')



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


