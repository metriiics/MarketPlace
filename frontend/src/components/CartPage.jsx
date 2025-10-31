import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";

export default function CartPage() {
  const [cart, setCart] = useState(() => {
    const saved = localStorage.getItem("cart");
    return saved ? JSON.parse(saved) : [];
  });

  const total = cart.reduce((sum, item) => sum + item.price, 0);

  const removeFromCart = (id) => {
    const updated = cart.filter((item) => item.id !== id);
    setCart(updated);
    localStorage.setItem("cart", JSON.stringify(updated));
  };

  const clearCart = () => {
    setCart([]);
    localStorage.removeItem("cart");
  };

  return (
    <div className="container">
      <div className="header-bar">
        <h1>🛒 Корзина</h1>
        <Link to="/" className="back-link">
          ← Назад в магазин
        </Link>
      </div>

      {cart.length === 0 ? (
        <p>Корзина пуста</p>
      ) : (
        <ul className="cart-list">
          {cart.map((item) => (
            <li key={item.id} className="cart-item">
              <span>
                {item.name} — {item.price} ₽
              </span>
              <button onClick={() => removeFromCart(item.id)}>✕</button>
            </li>
          ))}
        </ul>
      )}

      {cart.length > 0 && (
        <>
          <h3>Итого: {total} ₽</h3>
          <button className="checkout-btn" onClick={clearCart}>
            Оформить заказ
          </button>
        </>
      )}
    </div>
  );
}
