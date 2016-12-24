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

