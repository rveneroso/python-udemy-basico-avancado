'''
Sorted pode ser utilizado com qualquer iterável. Já a funcão sort() só existe para listas.

Sorted, como o nome já indica, serve para ordenar os valores de um iterável.

A função sort() modifica a lista na qual é aplicada. Já sorted, gera um novo iterável ordenado sem modificar o objeto original.

OBSERVAÇÃO: sorted SEMPRE retorna uma lista com os elementos originais do iterável ordenados.
'''

numeros = [6, 1, 9, 3, 10, 11, 3, 4, 25]
print(f'List original: {numeros}')
print(f'Sorted aplicado sobre numeros {sorted(numeros)}')
print(f'Lista numeros após aplicação de sorted {numeros}')
numeros.sort()
print(f'Lista numeros após execução da função sort {numeros}')

print(f'Ordenando decrescente {sorted(numeros, reverse=True)}')

usuarios = [
    {"username": "samuel", "tweets": ["Eu adodo bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": [], "cor": "amarelo"},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": [], "cor": "preto", "musica": "rock"}
]

print(usuarios)

# Ordenando por username - Ordem Alfabética
# A função lambdba abaixo retorna o nome do usuário e esse nome é usado como chave para a ordenação do sorted.
print(sorted(usuarios, key=lambda usuario: usuario["username"]))

# Ordenando pelo número de tweets de cada usuário
print(sorted(usuarios, key=lambda usuario: len(usuario["tweets"])))

musicas = [
    {"titulo": "Thunderstruck", "tocou": 3},
    {"titulo": "Dead Skin Mask", "tocou": 2},
    {"titulo": "Back in Black", "tocou": 4},
    {"titulo": "Too old to rock'in'roll, too young to die", "tocou": 32}
]

# Ordena da menos tocada para a mais tocada
print(sorted(musicas, key=lambda musica: musica['tocou']))

# Ordena da mais tocada para a menos tocada
print(sorted(musicas, key=lambda musica: musica['tocou'], reverse=True))

