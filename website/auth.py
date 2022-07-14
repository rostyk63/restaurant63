from flask import Blueprint, render_template, redirect, url_for, request, flash

from . import db
from .models import User

from flask_login import login_user, current_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        user_name = request.form.get('user_name')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        email_exists = User.query.filter_by(email=email).first()
        if email_exists:
            flash('Account with this email is already created.', category='error')
        elif password1 != password2:
            flash('Passwords dont match.', category='error')
        else:
            new_user = User(user_name=user_name, email=email,
                            password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('User created successfully!', category='success')
            return redirect(url_for('views.home'))

    return render_template('sign_up.html', user=current_user)


@auth.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Password is incorrect.', category='error')
        else:
            flash('User with this email does not exists.', category='error')

    return render_template('login.html', user=current_user)


@auth.route('/logout', methods=['POST', 'GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
