from http.client import HTTPException
from typing import Set, Union, List

from sqlalchemy.orm import Session

from sql_app import schemas, crud
from sql_app.crud import get_user, create_user, get_restaurants

from fastapi import FastAPI, Depends

from sql_app.main import get_db
from sql_app.schemas import RestaurantCreate, Dish, RestaurantExtendCreate

app = FastAPI()

@app.get("/")
async def root(page: int = 0, size: int = 2):
    db = next(get_db())
    return get_restaurants(db, page*size, size)

    # return restaurants[page*size:(page+1)*size]


@app.get("/hello/{name}")
async def say_hello(name: str):
    db = get_db()
    get_user(db, 1)
    return {"message": f"Hello {name}"}

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

@app.post("/restaurants/")
def create_user(restaurant: RestaurantCreate, db: Session = Depends(get_db)):
    print(Dish.KR.value)
    return crud.create_restaurant(
        db,
        RestaurantCreate(
            longitude=restaurant.longitude,
            latitude=restaurant.latitude,
            photos=restaurant.photos,
            tags=restaurant.tags
        )
    )

@app.get("/restaurants/extend/")
def get_restaurants_extend(page: int = 0, size: int = 2, db: Session = Depends(get_db)):
    return crud.get_restaurants_extend(db, page*size, size)
@app.post("/restaurants/extend/")
def create_restaurant_extend(restaurant: RestaurantExtendCreate, db: Session = Depends(get_db)):
    return crud.create_restaurant_extend(
        db,
        restaurant
    )