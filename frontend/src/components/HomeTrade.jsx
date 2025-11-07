import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";

export default function HomeTrade() {
  const [products, setProducts] = useState([]);
  const [cart, setCart] = useState(() => {
    const saved = localStorage.getItem("cart");
    return saved ? JSON.parse(saved) : [];
  });

  // Загружаем товары
  useEffect(() => {
    fetch("http://127.0.0.1:8000/products")
      .then((res) => res.json())
      .then((data) => {
        if (Array.isArray(data)) setProducts(data);
      })
      .catch(() => console.error("Ошибка загрузки товаров"));
  }, []);

  // Сохраняем корзину
  useEffect(() => {
    localStorage.setItem("cart", JSON.stringify(cart));
  }, [cart]);

  const addToCart = (product) => {
    setCart([...cart, product]);
  };

  const hasItems = cart.length > 0;

  return (
    <div className="container">
      <div className="header-bar">
        <h1>🛍️ Мини-магазин</h1>
        <Link
          to="/checkout"
          className={`cart-link ${hasItems ? "active" : ""}`}
        >
          🛒 Корзина ({cart.length})
        </Link>
        <Link to="/products/add" className="add-product-link">
          ➕ Добавить товар
        </Link>
      </div>

      <div className="product-list">
        {products.map((p) => (
          <div key={p.id} className="product-card">
            <div className="product-info">
              <h3>{p.name}</h3>
              <p className="desc">{p.description}</p>
              <p className="price">{p.price} ₽</p>
            </div>
            <button onClick={() => addToCart(p)}>Добавить</button>
          </div>
        ))}
      </div>
    </div>
  );
}
