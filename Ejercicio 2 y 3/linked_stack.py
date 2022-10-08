from typing import Any, Union
from list_node import ListNode

class LinkedStack:
    def __init__(self) -> None:
        self._head : Union[ListNode, None] = None
        self._size : int = 0

    def __len__(self) -> int:
        return self._size
    
    def __str__(self) -> str:
        
        if self.is_empty():
            return "LinkedStack()"
        resultado = ""

        actual = self._head

        while actual != None:
            resultado += str(actual.element) + ", "
            actual = actual.next 
        resultado = resultado[:len(resultado)-2]
        return f"LinkedStack({resultado})"
    
    def is_empty(self) -> bool:
        return self._size == 0
    
    def push(self, elem: Any) -> None:
        nuevo_tope = ListNode(elem, self._head)
        self._head = nuevo_tope
        self._size += 1
        
    def top(self) -> Any:
        if self.is_empty():
            raise Exception("Pila vacía. Operación no soportada")
        return self._head.element
        
    def pop(self) -> Any:
        if self.is_empty():
            raise Exception("Pila vacía. Operación no soportada")
        resultado = self._head.element
        self._head = self._head.next
        self._size -= 1
        return resultado