from pydantic import BaseModel, Field
from typing import List

class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float

class ProductCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100, description="Название товара")
    description: str = Field(..., min_length=1, max_length=500, description="Описание товара")
    price: float = Field(..., gt=0, description="Цена товара (в рублях)")