from . import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)

    def __str__(self):
        return f'{self.user_name}, {self.email}'


class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    restaurant_name = db.Column(db.String(50), nullable=False)
    menu = db.relationship('Menu', backref='restaurant', passive_deletes=True)

    def __str__(self):
        return f'{self.restaurant_name}, {self.menu}'


class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id', ondelete='CASCADE'), nullable=False)
    first = db.Column(db.String(50), nullable=False, default='borsch')
    second = db.Column(db.String(50), nullable=False, default='caesar')
    third = db.Column(db.String(50), nullable=False, default='water')

    def __str__(self):
        return f'{self.first}, {self.second}, {self.third}'
