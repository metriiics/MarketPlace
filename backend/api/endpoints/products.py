from fastapi import APIRouter, HTTPException, Depends
from dependencies import get_manager
from query import ProductManager

router = APIRouter()

@router.get("/products")
def get_products(manager: ProductManager = Depends(get_manager)):
    """
    Возвращает список всех товаров из JSON-файла.
    """
    return manager.get_all()

@router.get("/products/{product_id}")
def get_product(product_id: int, manager: ProductManager = Depends(get_manager)):
    """
    Возвращает один товар по его ID.
    """
    product = manager.get_by_id(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product