from flask import Blueprint, render_template, redirect, url_for, request, flash

from flask_login import login_required, current_user

from . import db
from .models import Restaurant, Menu


views = Blueprint('views', __name__)


@views.route('/')
@views.route('/home')
def home():
    restaurants = Restaurant.query.all()
    return render_template('home.html', user=current_user, restaurants=restaurants)


@views.route('/create-restaurant', methods=['POST', 'GET'])
@login_required
def create_restaurant():
    if request.method == 'POST':
        restaurant = request.form.get('restaurant')
        first_food = request.form.get('first')
        second_food = request.form.get('second')
        third_food = request.form.get('third')
        if Restaurant.query.filter_by(restaurant_name=restaurant).first():
            flash('There is restaurant with this name', category='error')
        else:
            new_restaurant = Restaurant(restaurant_name=restaurant)
            db.session.add(new_restaurant)
            db.session.commit()
            restaurant_menu = Menu(restaurant_id=new_restaurant.id, first=first_food, second=second_food,
                                   third=third_food)
            db.session.add(restaurant_menu)
            db.session.commit()
            flash('The restaurant was successfully added!', category='success')
            return redirect(url_for('views.home'))
    return render_template('create_restaurant.html', user=current_user)


@views.route('/restaurant/<int:restaurant_id>')
def get_restaurant(restaurant_id):
    restaurant = Restaurant.query.get(restaurant_id)
    menu = Menu.query.filter_by(restaurant_id=restaurant_id).first()
    return render_template('restaurant.html', restaurant=restaurant, user=current_user, menu=menu)


@views.route('/menu-vote')
@login_required
def menu_vote():
    restaurants = Restaurant.query.all()
    return render_template('menu_vote.html', user=current_user, restaurants=restaurants)


@views.route('/restaurant/<int:restaurant_id>/menu-vote', methods=['GET', 'POST'])
@login_required
def restaurant_menu_vote(restaurant_id):
    restaurant = Restaurant.query.get(restaurant_id)
    menu = Menu.query.filter_by(restaurant_id=restaurant_id).first()
    if request.method == 'POST':
        first_food = request.form.get('food1')
        second_food = request.form.get('food2')
        drink = request.form.get('food3')
        menu.first = first_food
        menu.second = second_food
        menu.third = drink
        db.session.commit()
        flash('Your vote has been counted', category='success')
        return redirect(url_for('views.results'))
    return render_template('restaurant_menu_vote.html', user=current_user, restaurant=restaurant)


@views.route('/results')
def results():
    restaurants = Restaurant.query.all()
    return render_template('results.html', user=current_user, restaurants=restaurants)


@views.route('/delete-restaurant/<int:restaurant_id>')
@login_required
def delete_restaurant(restaurant_id):
    restaurant = Restaurant.query.get(restaurant_id)
    if not restaurant:
        flash('Restaurant does not exist.', category='error')
    else:
        db.session.delete(restaurant)
        db.session.commit()
        flash('Restaurant deleted.', category='success')
    return redirect(url_for('views.home'))
