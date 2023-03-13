from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
  __tablename__ = 'users'
  email = db.Column(db.String(100), unique=True, primary_key=True)
  password = db.Column(db.String(100))
  name = db.Column(db.String(1000))
  level = db.Column(db.Integer, default=0)
  score = db.Column(db.Integer, default=0)

  def get_id(self):
        return (self.email)