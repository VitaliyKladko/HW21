from entity.base_storage import BaseStorage
from entity.exceptions import TooManyDifferentProductsError


class Shop(BaseStorage):
    def __init__(self, items: dict[str, int], capacity: int = 20):
        super().__init__(items, capacity)

    def add(self, name: str, amount: int) -> None:
        if self.get_unique_items_count() >= 5:
            # TODO: Ошибка 'Слишком много разных товаров'
            raise TooManyDifferentProductsError
        super().add(name, amount)
