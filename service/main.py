from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from .models import User
from . import db
# from flask_sqlalchemy import desc

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def index():

  usersBd = User.query.order_by(db.desc(User.score)).limit(10)
  # users = User.query.order_by(User.score).all()

  usersSorted = []
  for user in usersBd:
    userAdded = {
      'name': user.name,
      'score': user.score
    }
    usersSorted.append(userAdded)

  if(current_user.is_authenticated):
    return render_template('index.html', users=usersSorted, name=current_user.name, score=current_user.score)
  else:
    return render_template('index.html', users=usersSorted)
  # return render_template('index.html', users=usersSorted, name=current_user.name, score=current_user.score)
  # return redirect(url_for('main.index'))

# @main.route('/cows', methods=['GET'])
# def cows():
#   return render_template('index.html')

# secure route example
@main.route('/profile')
@login_required
def profile():
  return render_template('profile.html', name=current_user.name)

# current_user - user from the database we can get all its fields
