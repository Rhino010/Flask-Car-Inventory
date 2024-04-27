from flask import Flask, render_template, Blueprint, url_for, flash
from forms import UserLoginForm
from models import User, db, check_password_hash

@auth.route('/signup')
def signup():
    
    return 'signup.html'
    
@auth.route('/signin')
def signin():

    return 'signin.html'

