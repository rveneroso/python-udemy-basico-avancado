'''
Não se deve confundir a função reversed() com a função reverse() das listas.

reverse() só existe para listas.

reversed() funcionado com qualquer iterável. Sua função é inverter o iterável.

A função reversed() retorna um iterável chamado List Reverse Iterator

reversed() cria um novo iterável a partir do original sem alterar o iterável original.
'''

nome = 'Geek University'
nome_invertido = list(reversed(nome))
print(nome_invertido)

lista = [1, 2, 3, 4, 5]

res = reversed(lista)

print(res)
print(type(res))

# Podemos converter o elemento retornado para uma Lista, Tupla ou Conjunto

# Lista
print(list(reversed(lista)))

# Tupla
print(tuple(reversed(lista)))

# OBS: Em conjuntos, não definimos a ordem dos elementos
# Conjunto (Set)
print(set(reversed(lista)))

# Podemos iterar sobre o reversed
for letra in reversed('Geek University'):
    print(letra, end='')

print('\n')