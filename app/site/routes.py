from flask import Blueprint, render_template
from helpers import token_required


site = Blueprint('site', __name__, template_folder = 'site_templates')

@site.route('/')
def home():
    return render_template('index.html')

@site.route('/profile')
@token_required
def profile():
    return render_template('profile.html')