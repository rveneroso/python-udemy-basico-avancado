'''
Deques são muito semelhantes às listas mas com uma diferença: com deques é possível adiconar elementos no início da lista. Nas listas regulares, a inserção
de um novo elemento acontece sempre no fim da lista.
'''
from collections import deque

deq = deque('Geek')
print(deq)

# O método append funciona exatamente como com listas comuns.
deq.append('y')
print(deq) # Imprime deque(['G', 'e', 'e', 'k', 'y'])

deq.appendleft('k')
print(deq) # Imprime deque(['k', 'G', 'e', 'e', 'k', 'y'])

# O método pop() também funciona como com listas regulares.
deq.pop() # Removerá o último elemento da lista. No caso, 'y'
print(deq) # deque(['k', 'G', 'e', 'e', 'k'])

deq.popleft() # Irá remover o elemento que está no início da lista
print(deq) # Imprime deque(['G', 'e', 'e', 'k'])

