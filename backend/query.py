import json
from pathlib import Path
from typing import List, Dict, Optional


class ProductManager:
    """Класс для управления товарами в JSON."""

    def __init__(self, file_path: str = "products.json"):
        self.path = Path(file_path)
        if not self.path.exists():
            self._init_file()

    def _init_file(self):
        """Создаёт файл, если его нет."""
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump([], f, ensure_ascii=False, indent=2)

    def _read(self) -> List[Dict]:
        """Чтение данных из JSON."""
        with open(self.path, "r", encoding="utf-8") as f:
            return json.load(f)

    def _write(self, data: List[Dict]) -> None:
        """Запись данных в JSON."""
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    # ------------------------
    # Основные CRUD-операции
    # ------------------------

    def get_all(self) -> List[Dict]:
        """Возвращает список всех товаров."""
        return self._read()

    def get_by_id(self, product_id: int) -> Optional[Dict]:
        """Находит товар по ID."""
        for product in self._read():
            if product.get("id") == product_id:
                return product
        return None

    def add_product(self, product_data: dict):
        """Добавляет новый товар."""
        products = self.get_all()

        # Генерация нового ID
        new_id = max((p.get("id", 0) for p in products), default=0) + 1

        # Создаём новый товар
        new_product = {"id": new_id, **product_data}

        # Добавляем и сохраняем
        products.append(new_product)
        self._write(products)

        return new_product

