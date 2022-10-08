from typing import Any
from linked_stack_ext_abstract import LinkedStackExtAbstract
from linked_stack import LinkedStack

class LinkedStackExt(LinkedStack):
    def multi_pop(self, num: int):
        lista_topes = list()
        for i in range(num):
            elem = self.pop()
            lista_topes.append(elem)
        
        return lista_topes

    
    def replace_all(self, param1: Any, param2: Any) -> None:
        lista_elementos = list()
        for i in range(self.__len__()):
            elem = self.pop()
            lista_elementos.append(elem)
        for i in range(len(lista_elementos)):
            if lista_elementos[i] == param1:
                lista_elementos[i] = param2
        for i in reversed(lista_elementos):
            self.push(i)
        
    
    def exchange(self) -> None:
        lista_elementos = list()
        for i in range(self.__len__()):
            elem = self.pop()
            lista_elementos.append(elem)
        lista_elementos[0], lista_elementos[-1] = lista_elementos[-1], lista_elementos[0]
        for i in reversed(lista_elementos):
            self.push(i)

        

