from numbers import Real

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Double
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import relationship

from .database import Base

from sqlalchemy.types import TypeDecorator, Integer

from .schemas import Dish


class EnumType(TypeDecorator):
    impl = String

    def __init__(self, enum_class):
        super().__init__()
        self.enum_class = enum_class

    def process_bind_param(self, value, dialect):
        if value is not None:
            return value.value

    def process_result_value(self, value, dialect):
        if value is not None:
            return self.enum_class(value)

class RestaurantExtend(Base):
    __tablename__ = "restaurants_extend"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    x = Column(Double)
    y = Column(Double)
    fullRoadAddress = Column(String)
    description = Column(String)
    images = Column(ARRAY(String))
    categories = Column(ARRAY(String))
    bizhourInfo = Column(String)
    menuImages = Column(ARRAY(String))
    previewImages = Column(ARRAY(String))

class Restaurant(Base):
    __tablename__ = "restaurants"

    id = Column(Integer, primary_key=True, index=True)
    latitude = Column(Double)
    longitude = Column(Double)
    photos = Column(ARRAY(String))
    tags = Column(ARRAY(EnumType(Dish)))


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")
