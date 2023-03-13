import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()

def create_app():
  app = Flask(__name__)

  app.debug = True
  app.config['SECRET_KEY'] = SECRET_KEY
  app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
  app.config['SQLALCHEMY_ECHO'] = True

  db.init_app(app)

  login_manager = LoginManager()
  login_manager.login_view = 'auth.login'
  login_manager.init_app(app)

  from .models import User
  # @login_manager.user_loader
  # def load_user(user_id):
  #     # since the user_id is just the primary key of our user table, use it in the query for the user
  #     return User.query.get(int(user_id))
  @login_manager.user_loader
  def load_user(email):
      return User.query.get(email)

  # blueprint for auth routes in our app
  from .auth import auth as auth_blueprint
  app.register_blueprint(auth_blueprint)

  # blueprint for non-auth parts of app
  from .main import main as main_blueprint
  app.register_blueprint(main_blueprint)

  return app