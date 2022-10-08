from deque import Deque

cola = Deque()

print("\n----- se agregan 6 elementos a la cola -----")
cola.add_first(25)
cola.add_first(33)
cola.add_first(46)
cola.add_first(54)
cola.add_first(61)
cola.add_first(133)


print(f"\n----- método __str__: {cola.__str__()} -----")

print(f"\n----- tamaño de la cola: {cola.__len__()} -----")

print(f"\n----- primer elemento: {cola.first()} -----")

print(f"\n----- último elemento: {cola.last()} -----")

print("\n----- se agrega un elemento al final de la cola -----")
cola.add_last(77)

print(f"\n----- cola: {cola} -----")

print("\n----- se elimina el último elemento de la cola -----")
cola.delete_last()

print(f"\n----- cola: {cola} -----")

print(f"\n----- se elimina el primer elemento de la cola -----")
cola.delete_first()

print(f"\n----- cola: {cola} -----")