from abc import abstractmethod
from ast import List, main
from typing import Any
from linked_stack_ext_abstract import LinkedStackExtAbstract
from linked_stack import LinkedStack

class LinkedStackExt(LinkedStack):
    """Representa un conjunto de métodos para extender la implementación original
    de LinkedStack.
    Args:
    ABC (_type_): _description_
    """

    @abstractmethod
    def multi_pop(self, num: int) -> List[Any]:
        """Realiza la cantidad de operaciones pop() indicada por num.
        Args:
        num (int): número de veces que se va a ejecutar pop().
        Raises:
        Exception: Arroja excepción si se invoca a pop() por cuando la estructura
        está vacía.
        Returns:
        List[Any]: lista formada por todos los topes que se quitaron de la pila.
        """
        lista_topes = list()
        for i in range(num):
            elem = super.pop()
            lista_topes.append(elem)
        
        return lista_topes



    @abstractmethod
    def replace_all(self, param1: Any, param2: Any) -> None:
        """Reemplaza todas las ocurrencias de param1 en la pila por param2.
        Args:
        param1 (Any): Valor a buscar/reemplazar.
        param2 (Any): Nuevo valor.
        """
        lista_elementos = list()
        for i in super.__len__():
            elem = super.pop()
            lista_elementos.append(elem)
        for i in lista_elementos:
            if lista_elementos[i] == param1:
                lista_elementos[i] = param2
        for i in reversed(lista_elementos):
            super.push(i)
        
            

    @abstractmethod
    def exchange(self) -> None:
        """Intercambia el elemento ubicado en el tope con el más antigüo o último.
        Raises:
        Exception: Arroja excepción si la estructura está vacía.
        """
        lista_elementos = list()
        for i in super.__len__():
            elem = super.pop()
            lista_elementos.append(elem)
        lista_elementos[0], lista_elementos[-1] = lista_elementos[-1], lista_elementos[0]
        for i in reversed(lista_elementos):
            super.push(i)

        

