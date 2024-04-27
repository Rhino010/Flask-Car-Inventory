from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import uuid
import secrets
frome datetime import datetime
from weurkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin
import flask_marshmallow import Marshmallow

login_manager = LoginManager()
ma = Marshmallow()
db = SQLAlchemy()

class User(db.model, UserMixin):
    ID = db.Column(db.String, primary_key = True)
    first_name = db.Column(db.String(150), nullable = True, default = '')
    last_name = db.Column(db.String(150), nullable = True, default = '')
    email = db.Column(db.String(150), nullable = False)
    password = db.Column(db.String, nullable = True, default = '')
    token = db.Column(db.String, default = '', unique = True)
    date_created = db.Column(db.Datetime, nullable = False, default = datetime.now(datetime.UTC))
    