from entity.base_storage import BaseStorage


class Store(BaseStorage):
    """
    Класс склад
    """
    def __init__(self, items: dict[str, int], capacity: int = 100):
        super().__init__(items, capacity)
