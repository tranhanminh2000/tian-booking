from abc import ABC, abstractmethod
from typing import Any


class BaseCRUDRepository(ABC):

    @abstractmethod
    def get(self, id: str) -> Any:
        pass

    @abstractmethod
    def get_all(self) -> list[Any]:
        pass

    @abstractmethod
    def create(self, item: Any) -> Any:
        pass

    @abstractmethod
    def update(self, id: str, item: Any) -> Any:
        pass

    @abstractmethod
    def delete(self, id: str) -> None:
        pass
