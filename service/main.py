from flask import Blueprint, render_template
from flask_login import login_required, current_user
from . import db

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def set_user_score():
  return render_template('index.html')

# secure route example
@main.route('/profile')
@login_required
def profile():
  return render_template('profile.html', name=current_user.name)

# current_user - user from the database we can get all its fields