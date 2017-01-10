# -*- coding: utf-8 -*-
from flask import session as login_session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, Menu, User

class DB_interaction:
    engine = create_engine('sqlite:///restaurant.db')
    Base.metadata.bind=engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    def count_restaurants(self):
        return self.session.query(Restaurant)\
            .count()

    def query_restaurants(self):
        restaurants = self.session.query(Restaurant)\
            .order_by(Restaurant.name.asc())\
            .all()
        num = self.count_restaurants()
        return restaurants, num

    def add_restaurant(self, name):
        try:
            new_restaurant = Restaurant(name=name, user_id=login_session['user_id'])
            self.session.add(new_restaurant)
            self.session.commit()
        except:
            print u"An unknown error has occurred. Please try again."

    def query_restaurant_by_id(self, id):
        try:
            return self.session.query(Restaurant)\
                .filter_by(id=id)\
                .one()
        except:
            print u"Error. No id found."

    def update_restaurant_by_id(self, id, new_name):
        restaurant = self.query_restaurant_by_id(id)

        if restaurant:
            try:
                restaurant.name = new_name
                self.session.add(restaurant)
                self.session.commit()
            except:
                print u"An error has occured while trying to edit the restaurant name"

    def delete_restaurant(self, id):
        restaurant = self.query_restaurant_by_id(id)

        if restaurant:
            try:
                print u"Restaurant %s has been deleted" % restaurant.name
                self.session.delete(restaurant)
                self.session.commit()
            except:
                print u"An error has occured while trying to edit the restaurant name"

    def query_menus(self, rest_id):
        try:
            return self.session.query(Menu)\
                .filter_by(restaurant_id=rest_id)\
                .order_by(Menu.name.asc())\
                .all()
        except:
            print u"Error. Menu for restaurant with id %s were not found." % rest_id

    def add_menu(self, name, course, description, price, rest_id):
        try:
            new_menu = Menu(name=name, course=course, description=description, price=price, restaurant_id=rest_id, user_id=login_session['user_id'])
            self.session.add(new_menu)
            self.session.commit()
            return new_menu.id
        except:
            print u"An unknown error has occurred. Please try again."

    def query_menu_by_id(self, menu_id):
        try:
            return self.session.query(Menu)\
                .filter_by(id=menu_id)\
                .one()
        except:
            print u"The menu with id %s could not be found." % id

    def update_menu(self, menu_id, new_name, new_course, new_description, new_price):
        menu = self.query_menu_by_id(menu_id)

        if menu:
            try:
                menu.name = new_name
                menu.course = new_course
                menu.description = new_description
                menu.price = new_price
                self.session.add(menu)
                self.session.commit()
                return menu.id
            except:
                print u"An unknown error has occurred. Please try again."

    def delete_menu(self, menu_id):
        menu = self.query_menu_by_id(menu_id)

        if menu:
            try:
                print u"Menu %s has been deleted" % menu.name
                self.session.delete(menu)
                self.session.commit()
            except:
                print u"An unknown error has occurred. Please try again."

    def get_user_info(self, user_id):
        user = self.session.query(User).filter_by(id=user_id).one()
        return user

    def get_user_id(self, email):
        try:
            user = self.session.query(User).filter_by(email=email).one()
            return user.id
        except:
            return None

    def create_user(self, login_session):
        existing_user = self.get_user_id(login_session['email'])
        if existing_user:
            print u'Current user already registered!'
            return existing_user

        new_user = User(name=login_session['username'], email=login_session['email'], picture=login_session['picture'])
        self.session.add(new_user)
        self.session.commit()
        return self.get_user_id(login_session['email'])