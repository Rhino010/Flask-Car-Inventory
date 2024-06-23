from flask import Flask
from config import Config
from .api.routes import api
from .site.routes import site
from .authentication.routes import auth

from flask_migrate import Migrate
from flask_cors import CORS

from json import JSONEncoder
from app.models import db as root_db, login_manager, ma


app = Flask(__name__)
CORS(app)

app.register_blueprint(site)
app.register_blueprint(auth)
app.register_blueprint(api)

app.json_encoder = JSONEncoder
app.config.from_object(Config)
root_db.init_app(app)
login_manager.init_app(app)
ma.init_app(app)
migrate = Migrate(app, root_db)

# # This will automatically logout the user when the app is shut down
# def logout_all_users(exception = None):
#     try:
#         # Will set user tokens to invalid upon logging out, essentially automatically logging out upon shut down.
#         invalid_token = 'Invalid Token!'
#         users = User.query.all()

#         for user in users:
#             user.token = invalid_token
        
#         root_db.session.commit()
    
#         print('All users have been successfully logged out.')

#     except Exception as e:
#         print(f'Logout unsuccessful for {e}.')

#         root_db.session.rollback()

#     finally:
#         root_db.session.remove()

# @app.teardown_appcontext
# def teardown(exception):
#     logout_all_users(exception)

