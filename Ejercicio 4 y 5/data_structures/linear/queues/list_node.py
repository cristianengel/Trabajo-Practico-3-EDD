from ctypes import Union
from typing import Any, List

class ListNode():
     
    def __init__(self, element : Any, next = None, prev = None) -> None:
        self.element = element
        self.next : Union[ListNode, None] = next
        self.prev : Union[ListNode, None] = prev