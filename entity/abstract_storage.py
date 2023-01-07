from abc import ABC, abstractmethod


class AbstractStorage(ABC):
    """
    Описываем абстрактный класс с помощью ABC
    Абстрактный класс - это по сути шаблон, по которому мы создаем объекты-наследники
    """
    # @abstractmethod - декоратор для определения абстрактного метода или, если мы не предоставляем определение методу,
    # он автоматически становится абстрактным методом
    @abstractmethod
    def add(self, name: str, amount: int) -> None:
        pass

    @abstractmethod
    def remove(self, name: str, amount: int) -> None:
        pass

    @abstractmethod
    def get_free_space(self) -> int:
        pass

    @abstractmethod
    def get_items(self) -> dict[str, int]:
        pass

    @abstractmethod
    def get_unique_items_count(self) -> int:
        pass
