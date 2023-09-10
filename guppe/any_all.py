'''
all() -> retorna True se todos os elementos presentes no iterável forem True ou se o iterável estiver vazio
any() -> retorna True se um dos elementos presentes no iterável forem True. Se o iterável estiver vazio,
    retorna False
'''
numeros = [0, 1, 2, 3, 4, 5]
print(all(numeros)) # Imprime False porque o 0 retorna False
numeros2 = [1, 2, 3, 4, 5]
print(all(numeros2)) # Imprime True pois o 0 foi removido da lista.
vazia = []
print(all(vazia)) # Imprime True pois a lista está vazia

nomes = ['Carlos', 'Charles', 'Camila', 'César', 'Cibelle']
# Imprime True porque todos os nomes da lista começam com C
print(all([nome[0] == 'C' for nome in nomes]))

nomes = ['Carlos', 'Charles', 'Camila', 'César', 'Cibelle', 'Vanessa']
# Imprime True porque pelo menos um dos nomes da lista começam com C
print(any([nome[0] == 'C' for nome in nomes]))
print(any(vazia))