from flask_sqlalchemy import SQLAlchemy 

db = SQAlchemy()

##############################################
#Model definitions

class User(db.Model):
    """table of customer info."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.string(30), nullable=False)
    f_name = db.Column(db.String(20), nullable=True)
    l_name = db.Column(db.String(30), nullable=True)
    email = db.Column(db.String(40), nullable=False)

    def __repr__(self):

        return f'<User user_id={self.user_id} username={self.username} password={self.password} f_name={self.f_name} l_name={self.l_name} email={self.email}>'


class Recommendation(db.Model):
    """table of recommendation info"""

    __tablename__ = 'recommendations'

    rec_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    city_id = db.Column(db.Integer, db.ForeignKey(cities.city_id))
    user_id = db.Column(db.Integer, db.ForeignKey(users.user_id))

    def __repr__(self):

        return f'<Recommendation rec_id={self.rec_id} city_id={self.city_id} user_id={self.user_id}>'


class City(db.Model):
    """table of city info."""

    __tablename__ = 'cities'

    city_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    city_info = db.Column(db.String, nullable=False)
    stay_id = db.Column(db.Integer, db.ForeignKey('stays.stay_id'))
    eat_id = db.Column(db.Integer, db.ForeignKey('eats.eat_id'))
    do_id = db.Column(db.Integer, db.ForeignKey('dos.do_id'))

    def __repr__(self):

        return f'<City city_id={self.city_id} city_info={self.city_info} stay_id={self.stay_id} eat_id={self.eat_id} do_id={self.do_id}>'

class Stay(db.Model):
    """table of places to stay - recommendations"""

    __tablename__ = 'stays'

    stay_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    stay_name = db.Column(db.String(100), nullable=False)
    stay_info = db.Column(db.String, nullable=True)
    city_id = db.Column(db.Integer, db.ForeignKey('cities.city_id'))

    def __repr__(self):

        return f'<Stay stay_id={self.stay_id} stay_name={self.stay_name} stay_info={self.stay_info} city_id={self.city_id} >'

class Eat(db.Model):
    """table of places to eat - recommendations"""

    __tablename__ = 'eats'

    eat_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    eat_name = db.Column(db.String(100), nullable=False)
    eat_info = db.Column(db.String, nullable=True)    
    city_id = db.Column(db.Integer, db.ForeignKey('cities.city_id'))

    def __repr__(self):

        return f'<Eat eat_id={self.eat_id} eat_name={self.eat_name} eat_info={self.eat_info} city_id={self.city_id} >'

class Do(db.Model):
    """table of things/activities to do - recommendations"""

    __tablename__ = 'dos'

    do_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    do_name = db.Column(db.String(100), nullable=False)
    do_info = db.Column(db.String, nullable=True)    
    city_id = db.Column(db.Integer, db.ForeignKey('cities.city_id'))

    def __repr__(self):

        return f'<Do do_id={self.do_id} do_name={self.do_name} do_info={self.do_info} city_id={self.city_id} >'


















        