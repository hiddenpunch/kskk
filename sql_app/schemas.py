import enum
from typing import Union

from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: Union[str, None] = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        orm_mode = True


class Dish(enum.Enum):
    KR = "KR"
    CN = "CN"
    JP = "JP"
    WS = "WS"
    MX = "MX"


class Restaurant(BaseModel):
    id: str
    latitude: float = 37.4797211
    longitude: float = 126.9529953
    photos: list[str] = [
        "https://ldb-phinf.pstatic.net/20230209_14/1675938486650ecwib_JPEG/new됶缭篿_뿜밎_뀺듺_ver20230209_면목.jpg"]
    tags: list[Dish] = [Dish.KR]

    class Config:
        orm_mode = True


class RestaurantCreate(BaseModel):
    latitude: float = 37.4797211
    longitude: float = 126.9529953
    photos: list[str] = [
        "https://ldb-phinf.pstatic.net/20230209_14/1675938486650ecwib_JPEG/new됶缭篿_뿜밎_뀺듺_ver20230209_면목.jpg"]
    tags: list[Dish] = [Dish.KR]


class RestaurantExtend(BaseModel):
    id: str
    name: str
    x: float
    y: float
    fullRoadAddress: str
    description: str
    images: list[str]
    categories: list[str]
    bizhourInfo: str
    menuImages: list[str]
    previewImages: list[str]

    class Config:
        orm_mode = True

class RestaurantExtendCreate(BaseModel):
    name: str = "식당"
    x: float = 126.9529953
    y: float = 37.4797211
    fullRoadAddress: str = "301"
    description: str = "301"
    images: list[str] = []
    categories: list[str] = []
    bizhourInfo: str = ""
    menuImages: list[str] = []
    previewImages: list[str] = []