from flask import Flask, render_template, Blueprint, url_for, flash, request, redirect
from forms import UserLoginForm
from models import User, db, check_password_hash
from flask_login import login_user, logout_user, LoginManager, current_user, login_required


auth = Blueprint('auth', __name__, template_folder = 'auth_templates')

@auth.route('/signup', methods = ['GET','POST'])
def signup():
    form = UserLoginForm()

    try:
        if request.method == 'POST' and form.validate_on_submit():
            email = form.email.data
            password = form.password.data
            print(email, password)

            user = User(email = email, password = password)

            db.session.add(user)
            db.session.commit()

            flash(f'Nailed it! Your account has been created {email}', 'User-created')

            return redirect(url_for('site.home'))
    
    except Exception as e:
        print(e)
        raise Exception('Invalid form data: Please check your form.')
    
    return render_template('sign-up.html', form = form)


@auth.route('/signin', methods = ['GET', 'POST'])
def signin():
    form = UserLoginForm()

    try:
        if request.method == 'POST' and form.validate_on_submit():
            email = form.email.data
            password = form.password.data
            print (email, password)

            logged_user = User.query.filter(User.email == email).first()

            if logged_user and check_password_hash(logged_user.password, password):
                login_user(logged_user)
                flash('Login Successful')
                return redirect(url_for('site.profile'))
            
            else:
                flash('This account is not recognized. Check email and password and try again.')
                return redirect(url_for('auth.signin'))
            
    except:
        raise Exception('Invalid Form Data: Please check your form.')
    
    return render_template('sign-in.html', form = form)


@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('site.home'))
    