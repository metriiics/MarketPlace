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

    def add(self, product: Dict) -> Dict:
        """Добавляет товар в JSON."""
        data = self._read()
        product["id"] = (max([p["id"] for p in data], default=0) + 1)
        data.append(product)
        self._write(data)
        return product

    def delete(self, product_id: int) -> bool:
        """Удаляет товар по ID."""
        data = self._read()
        new_data = [p for p in data if p["id"] != product_id]
        if len(data) == len(new_data):
            return False
        self._write(new_data)
        return True

    def update(self, product_id: int, updated_fields: Dict) -> Optional[Dict]:
        """Обновляет товар по ID."""
        data = self._read()
        for product in data:
            if product["id"] == product_id:
                product.update(updated_fields)
                self._write(data)
                return product
        return None
