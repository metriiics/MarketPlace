from fastapi import APIRouter, HTTPException, Depends
from dependencies import get_manager
from api.models.products import Product, ProductCreate
from query import ProductManager
from typing import List

router = APIRouter()

@router.get("/products", response_model=List[Product])
def get_products(manager: ProductManager = Depends(get_manager)):
    """
    Возвращает список всех товаров.
    """
    products = manager.get_all()
    return products


@router.get("/products/{product_id}", response_model=Product)
def get_product(product_id: int, manager: ProductManager = Depends(get_manager)):
    """
    Возвращает товар по ID.
    """
    product = manager.get_by_id(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.post("/products/add", response_model=Product, status_code=201)
def create_product(product: ProductCreate, manager: ProductManager = Depends(get_manager)):
    """
    Добавляет новый товар.
    """
    try:
        new_product = manager.add_product(product.dict())
        return new_product
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error while adding product: {e}")