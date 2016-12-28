# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from database_setup import Base, Restaurant

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
        new_restaurant = Restaurant(name=name)
        self.session.add(new_restaurant)
        self.session.commit()

    def query_restaurant_by_id(self, id):
        try:
            return self.session.query(Restaurant)\
                .filter_by(id=id)\
                .one()
        except:
            print "Error. No id found."

    def update_restaurant_by_id(self, id, new_name):
        restaurant = self.query_restaurant_by_id(id)

        if restaurant:
            try:
                restaurant.name = new_name
                self.session.add(restaurant)
                self.session.commit()
            except:
                print "An error has occured while trying to edit the restaurant name"

    def delete_restaurant(self, id):
        restaurant = self.query_restaurant_by_id(id)

        if restaurant:
            try:
                print "Restaurant %s has been deleted" % restaurant.name
                self.session.delete(restaurant)
                self.session.commit()
            except:
                print "An error has occured while trying to edit the restaurant name"


