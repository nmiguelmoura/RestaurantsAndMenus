from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
Base = declarative_base()


class User(Base):

    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    email = Column(String(250))
    picture = Column(String(250))


class Restaurant(Base):

    __tablename__ = "restaurant"

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship(User)

    @property
    def serialize(self):
        return {
            "name": self.name,
            "id": self.id
        }


class Menu(Base):

    __tablename__ = "menu"

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    course = Column(String(30), nullable=False)
    description = Column(String(250), nullable=False)
    price = Column(String(10), nullable=False)
    restaurant_id = Column(Integer, ForeignKey("restaurant.id"))
    restaurant = relationship(Restaurant)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship(User)

    @property
    def serialize(self):
        return {
            "name": self.name,
            "course": self.course,
            "description": self.description,
            "price": self.price,
            "restaurant": self.restaurant.name
        }


engine = create_engine('sqlite:///restaurant.db')
Base.metadata.create_all(engine)
