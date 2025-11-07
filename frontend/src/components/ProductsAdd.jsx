import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

export default function ProductAdd() {
  const [name, setName] = useState("");
  const [description, setDescription] = useState("");
  const [price, setPrice] = useState("");
  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();
    const newProduct = { name, description, price };

    // Отправляем новый товар на сервер
    fetch("http://127.0.0.1:8000/products/add", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(newProduct),
    })
      .then((res) => res.json())
      .then(() => {
        // После успешного добавления, перенаправляем пользователя на главную страницу
        navigate("/");
      })
      .catch(() => console.error("Ошибка добавления товара"));
  };

  return (
    <div className="add-product-container">
      <h1>Добавить товар</h1>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="name">Название</label>
          <input
            type="text"
            id="name"
            value={name}
            onChange={(e) => setName(e.target.value)}
            required
          />
        </div>

        <div className="form-group">
          <label htmlFor="description">Описание</label>
          <textarea
            id="description"
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            required
          />
        </div>

        <div className="form-group">
          <label htmlFor="price">Цена</label>
          <input
            type="number"
            id="price"
            value={price}
            onChange={(e) => setPrice(e.target.value)}
            required
          />
        </div>

        <button type="submit">Добавить товар</button>
      </form>
    </div>
  );
}
