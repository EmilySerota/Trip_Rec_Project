from jinja2 import StrictUndefined
from flask import Flask, render_template, redirect, request, flash, session

from flask_debugtoolbar import DebugToolbarExtension

from model import User, City, Recommendation, connect_to_db, db

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
    username = username.lower()
    password = request.form.get('password')

    #check database for username
    user = User.query.filter_by(username = username).first()

    #if username doesnt exist send to register page
    if not user:
        flash("That username doesn't exist yet! Register here.")
        return redirect('/register')

    #if password is wrong flash incorrect password
    elif password != user.password:
        flash('Incorrect password')
        return redirect('/login')

    #if they are correct then add to session 
    else:
        session['username'] = username
        flash("You're logged in! Start reviewing!")
        return redirect('/')

@app.route('/logout')
def log_out():
    """log the user out"""

    session.pop('username')
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
    username = username.lower()
    password = request.form.get('password')
    fname = request.form.get('fname')
    lname = request.form.get('lname')
    email = request.form.get('email')

    #if username is not already in database add
    if not User.query.filter_by(username = username).all():
        new_user = User(username=username, password=password, f_name=fname, l_name=lname, email=email)
        db.session.add(new_user)
        db.session.commit()

        flash('Now simply log in and start reviewing!')
        return redirect('/')
    else:
        flash('User already exists! Choose a new username.')
        return redirect('/register')

@app.route('/search_city')
def city_name_search():


    #request to get city name
    city_name = request.args.get('city_name')
    city_name = city_name.lower()

    #pull in object info for that specific city - purpose: to get city id
    city_obj = City.query.filter_by(city_name=city_name).first()

    #get the user rec object for all cities of that name
    if city_obj == None:
        flash("Sorry, a recommendation for that city hasnt been created yet! You should create one!")
        return redirect('/')
    else:
        recs = city_obj.recommendations 
        return render_template('city_search.html', recs=recs, city_name=city_name)




@app.route('/search_username')
def username_search():

    #request to get username
    username = request.args.get('username')
    username = username.lower()

    #pull in object info for that sepcific user 
    user_obj = User.query.filter_by(username=username).first()

    if user_obj == None:
        flash("Sorry, that username doesn't exist yet!")
        return redirect('/')
    else:
    #get all the recs for that user 
        user_recs = user_obj.recommendations
        return render_template('username_search.html', user_recs=user_recs, username=username)



@app.route('/create_rec')
def create_rec():
    """sends user to the new create page"""

    return render_template('create_rec.html')




@app.route('/create_new_rec', methods = ['POST'])
def add_rec_to_db():
    """recordes info submitted by user, creates the objects for the db, and adds to the db"""

    # Update session on login CAN THIS BE EASIER? Now I"m getting the username in the session, 
    #then getting that user's user object, then get the user id to pass into the rec id
    username = session['username']
    user_obj = User.query.filter_by(username=username).first()
    user_id = user_obj.user_id

    #need to pass in the city id that is created in the city table as well. Right now the city_id field is blank in rec table.


    #get the city_name & info separately since we need city_name for query anyway
    city_name = request.form.get('city_name')
    city_name = city_name.lower()
    city_info = request.form.get('city_info')


    #create the city obj if it doesn't exist other wise get the city_id for recs instantiation.
    city_obj = City.query.filter_by(city_name=city_name).first()
        
    if city_obj == None:
        city = City(city_name=city_name, city_info=city_info)
        db.session.add(city)
        db.session.commit()
        city_id = city.city_id
    else:    
        city_id = city_obj.city_id

    #add to the database
    recommendation = Recommendation(rec_name = request.form.get('rec_name'), stay_name= request.form.get('stay_name'), 
                stay_info = request.form.get('stay_info'), eat_name= request.form.get('eat_name'), 
                eat_info = request.form.get('eat_info'), do_name= request.form.get('do_name'), 
                do_info = request.form.get('do_info'), user_id=user_id, city_id=city_id)

    #call the save function to add to the database
    db.session.add(recommendation)
    db.session.commit()

    flash("Awesome! You've created a recommendation")
    return redirect(f'/view_recommendation/{recommendation.rec_id}')



@app.route('/recommendations/edit')
def edit_page():
    """return list of a user's recommendations - can select edit to view then edit from this page"""

    #get username & user id info
    username = session['username']
    user_obj = User.query.filter_by(username=username).first()
    user_id = user_obj.user_id

    #get a list of recommendations that the user_id has created
    user_recs = Recommendation.query.filter_by(user_id=user_id).all()

    return render_template('username_search.html', user_recs=user_recs, username=username)




@app.route('/view_recommendation/<int:rec_id>')
def view_rec(rec_id):
    """show an individual recommendation"""

    recommendation = Recommendation.query.get(rec_id)
    return render_template('recommendation_view.html', recommendation=recommendation)




@app.route('/rec_edit/<int:rec_id>')
def edit_rec(rec_id):
    """renders recommendation so the user can make edits"""

    recommendation = Recommendation.query.get(rec_id)
    return render_template('recommendation_edit.html', recommendation=recommendation)



@app.route('/recommendations/<int:rec_id>', methods=['POST'])
def update_recommendation(rec_id):
    """updates the new information in the database and returns the view page"""

    #get current recommendation object
    recommendation = Recommendation.query.get(rec_id)

    #get information entered by user
    new_rec_name = request.form.get('rec_name')
    new_city_info = request.form.get('city_info')
    new_stay_name = request.form.get('stay_name')
    new_stay_info = request.form.get('stay_info')
    new_eat_name = request.form.get('eat_name')
    new_eat_info = request.form.get('eat_info')
    new_do_name= request.form.get('do_name')
    new_do_info = request.form.get('do_info')

    #dont have to get user id or city id since that won't change

    #check to see if each block of info has changed, and if it has update the information
    if recommendation.rec_name != new_rec_name:
        recommendation.rec_name = new_rec_name
    if recommendation.city.city_info != new_city_info:
        recommendation.city.city_info = new_city_info
    if recommendation.stay_name != new_stay_name:
        recommendation.stay_name = new_stay_name
    if recommendation.stay_info != new_stay_info:
        recommendation.stay_info = new_stay_info
    if recommendation.eat_name != new_eat_name:
        recommendation.eat_name = new_eat_name
    if recommendation.eat_info != new_eat_info:
        recommendation.eat_info = new_eat_info
    if recommendation.do_name != new_do_name:
        recommendation.do_name = new_do_name
    if recommendation.do_info != new_do_info:
        recommendation.do_info = new_do_info

    #add and save updated information within database
    db.session.add(recommendation)
    db.session.commit()

    return redirect(f'/view_recommendation/{recommendation.rec_id}')


@app.route('/rec_delete/<int:rec_id>')
def delete(rec_id):
    """delete a recommendation from the db"""

    #get the information for that recommendation object
    recommendation = Recommendation.query.get(rec_id)

    #delete and commit
    db.session.delete(recommendation)
    db.session.commit()

    flash("You've successfully deleted your recommendation")
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


