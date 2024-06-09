from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import uuid
import secrets
from datetime import datetime, timezone
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin
from flask_marshmallow import Marshmallow


login_manager = LoginManager()
ma = Marshmallow()
db = SQLAlchemy()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):

    id = db.Column(db.String, primary_key = True)
    first_name = db.Column(db.String(150), nullable = True, default = '')
    last_name = db.Column(db.String(150), nullable = True, default = '')
    email = db.Column(db.String(150), nullable = False)
    password = db.Column(db.String, nullable = True, default = '')
    token = db.Column(db.String, default = '', unique = True)
    g_auth_verify = db.Column(db.Boolean, default = False)
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.now(timezone.utc))

    def __init__(self, email, g_auth_verify = False, first_name = '', last_name = '', password = ''):
        self.id = self.set_id()
        self.first_name = first_name
        self.last_name = last_name
        self.password = self.set_password(password)
        self.email = email
        self.token = self.set_token(24)
        self.g_auth_verify = g_auth_verify

    def set_id(self):
        return str(uuid.uuid4())
    
    def set_token(self, length):
        return secrets.token_hex(length)
    
    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash

    def __repr__(self):
        return f'{self.email} has been successfully added.'


    
class Cars(db.Model):
    id = db.Column(db.String, primary_key = True, nullable = False)
    make = db.Column(db.String(150), nullable = False)
    car_model = db.Column(db.String(150), nullable = False)
    year = db.Column(db.String(150), nullable = False)
    stock_quantity = db.Column(db.Integer)
    user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable = False)

    def __init__(self, make, car_model, year, stock_quantity, user_token, id = ''):
        self.id = self.set_id()
        self.make = make
        self.car_model = car_model
        self.year = year
        self.stock_quantity = stock_quantity
        self.user_token = user_token

    def __repr__(self, make, model, year):
        return f'{year} {make} {model} has been added to the database.'
    
    def set_id(self):
        return (secrets.token_urlsafe())
    


class CarsSchema(ma.Schema):
    class Meta:
        fields = ['id', 'make', 'car_model', 'year', 'stock_quantity']
   

car_schema = CarsSchema()
cars_schema = CarsSchema(many = True)
