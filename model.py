from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

##############################################
#Model definitions

class User(db.Model):
    """table of customer info."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String, nullable=False)
    f_name = db.Column(db.String(30), nullable=True)
    l_name = db.Column(db.String(30), nullable=True)
    email = db.Column(db.String(40), nullable=False)

    def __repr__(self):

        return f'<User user_id={self.user_id} username={self.username} password={self.password} f_name={self.f_name} l_name={self.l_name} email={self.email}>'


class Recommendation(db.Model):
    """table of recommendation info"""

    __tablename__ = 'recommendations'

    rec_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    rec_name = db.Column(db.String,)
    city_id = db.Column(db.Integer, db.ForeignKey('cities.city_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    stay_name = db.Column(db.String(100), nullable=False)
    stay_info = db.Column(db.String, nullable=True)
    eat_name = db.Column(db.String(100), nullable=False)
    eat_info = db.Column(db.String, nullable=True) 
    do_name = db.Column(db.String(100), nullable=False)
    do_info = db.Column(db.String, nullable=True)
    img_url = db.Column(db.String, nullable=True) 

    def save(self):
        """save new recs"""
        db.session.add(self)
        sb.session.commit()

    def __repr__(self):

        return f'<Recommendation rec_id={self.rec_id} city_id={self.city_id} user_id={self.user_id} stay_name={self.stay_name} stay_info={self.stay_info} eat_name={self.eat_name} eat_info={self.eat_info} do_name={self.do_name} do_info={self.do_info} img_url={self.img_url}>'

        #connect to City db backreferencing cities table
    city = db.relationship('City', backref=db.backref('recommendations'))

    user = db.relationship('User', backref=db.backref('recommendations'))


class City(db.Model):
    """table of city info."""

    __tablename__ = 'cities'

    city_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    city_name = db.Column(db.String, nullable=False)
    city_info = db.Column(db.String, nullable=False)

    def __repr__(self):

        return f'<City city_id={self.city_id} city_info={self.city_info}>'

 

###########################################################

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PstgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///trips'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
    db.create_all()

    
        