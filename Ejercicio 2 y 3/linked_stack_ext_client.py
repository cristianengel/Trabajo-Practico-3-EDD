from linked_stack_ext import LinkedStackExt
from linked_stack import LinkedStack
from list_node import ListNode
from util import h1, h2

def linked_stack_ext_client() -> None:
    h1("LinkedStackExt")
    
    stack_prueba = LinkedStackExt()
    
    for i in range(1, 11):
        stack_prueba.push(i)
        print("stack.push({}): {} - len(stack): {}".format(i, stack_prueba, len(stack_prueba)))
    
    h2("LinkedStackExt llena")
    print(stack_prueba)
    
    h2("Prueba Multipop:")
    print("Lista con los topes quitados")
    print(stack_prueba.multi_pop(5))
    
    h2("Prueba Metodo Replace_All")
    print("Pila prueba")
    stack_prueba.push(3)
    print(stack_prueba)

    stack_prueba.replace_all(3, 6)
    print("Pila luego del metodo") 
    print(stack_prueba)
    
    h2("Prueba metodo exchange")
    stack_prueba.exchange()
    print(stack_prueba)
                

if __name__ == "__main__" and __package__ is None:
    linked_stack_ext_client()