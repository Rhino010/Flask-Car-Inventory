from flask import Blueprint, jsonify, render_template, request
from models import User, db

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/getdata')
def getdata():
    return {'hello':'world'}

