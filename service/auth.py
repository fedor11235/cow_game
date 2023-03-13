from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from flask import Blueprint, request, redirect, url_for, flash
from .models import User
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST'])
def login():
  email = request.form.get('email')
  password = request.form.get('password')
  remember = True if request.form.get('remember') else False

  user = User.query.filter_by(email=email).first()

  if not user or not check_password_hash(user.password, password):
    flash('Please check your login details and try again.')
    return redirect(url_for('main.index'))
  
  login_user(user, remember=remember)

  return redirect(url_for('main.index'))

@auth.route('/signup', methods=['POST'])
def signup():
  name = request.form.get('name')
  email = request.form.get('email')
  password = request.form.get('password')

  # if this returns a user, then the email already exists in database
  user = User.query.filter_by(email=email).first()

  # if a user is found, we want to redirect back to signup page so user can try again
  if user:
    flash('Email address already exists')
    return redirect(url_for('main.index'))
  
  # create a new user with the form data. Hash the password so the plaintext version isn't saved.
  new_user = User(email=email, password=generate_password_hash(password, method='sha256'), name=name )

  # add the new user to the database
  db.session.add(new_user)
  db.session.commit()

  return redirect(url_for('main.index'))

@auth.route('/logout')
@login_required
def logout():
  logout_user()
  return redirect(url_for('main.index'))