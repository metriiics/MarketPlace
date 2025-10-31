from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from api.endpoints import products
from query import ProductManager
import json
from pathlib import Path

app = FastAPI()

app.router.include_router(products.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
    
def get_manager():
    return ProductManager("products.json")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Market Place VVSU!"}