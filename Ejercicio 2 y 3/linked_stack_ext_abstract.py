from abc import ABC, abstractmethod
from typing import Any, List
class LinkedStackExtAbstract(ABC):
   
    @abstractmethod
    def multi_pop(self, num: int) -> List[Any]:
        pass

    @abstractmethod
    def replace_all(self, param1: Any, param2: Any) -> None:
        pass

    @abstractmethod
    def exchange(self) -> None:
        pass