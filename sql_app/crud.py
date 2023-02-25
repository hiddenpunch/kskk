from sqlalchemy.orm import Session

from . import models, schemas
from .schemas import RestaurantCreate, RestaurantExtendCreate


def get_restaurants(db: Session, skip: int = 0, limit: int = 2):
    return db.query(models.Restaurant).offset(skip).limit(limit).all()

def create_restaurant(db: Session, restaurant: RestaurantCreate):
    db_restaurant = models.Restaurant(
        latitude = restaurant.latitude,
        longitude = restaurant.longitude,
        photos = restaurant.photos,
        tags = restaurant.tags
    )
    db.add(db_restaurant)
    db.commit()
    db.refresh(db_restaurant)
    return db_restaurant

def get_restaurants_extend(db: Session, skip: int = 0, limit: int = 2):
    return db.query(models.RestaurantExtend).offset(skip).limit(limit).all()

def create_restaurant_extend(db: Session, restaurant: RestaurantExtendCreate):
    db_restaurant_extend = models.RestaurantExtend(
        name = restaurant.name,
        x = restaurant.x,
        y = restaurant.y,
        fullRoadAddress = restaurant.fullRoadAddress,
        description = restaurant.description,
        images = restaurant.images,
        categories = restaurant.categories,
        bizhourInfo = restaurant.bizhourInfo,
        menuImages = restaurant.menuImages,
        previewImages = restaurant.previewImages
    )
    db.add(db_restaurant_extend)
    db.commit()
    db.refresh(db_restaurant_extend)
    return db_restaurant_extend

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item