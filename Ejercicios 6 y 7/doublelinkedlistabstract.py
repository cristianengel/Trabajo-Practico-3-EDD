from abc import ABC, abstractmethod
from typing import Any, Iterator
class DoubleLinkedListAbstract(ABC):
#"""Representa una lista doblemente enlazada en la cada nodo tienen referencia a su antecesor y sucesor."""

    @abstractmethod
    def __len__(self) -> int:
        pass

    @abstractmethod
    def __getitem__(self, key: int) -> Any:
        pass

    @abstractmethod
    def __setitem__(self, key: int, value: Any) -> None:
        pass

    abstractmethod
    def __delitem__(self, key: int) -> None:
        pass

    @abstractmethod
    def __iter__(self) -> Iterator[Any]:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        pass
    @abstractmethod

    def append(self, elem: Any) -> None:
        pass
