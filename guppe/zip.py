'''

Zip

zip() -> Cria um iterável (Zip Object) que agrega elemento de cada um dos iteráveis passados como entrada em pares.
'''

# Exmplos

lista1 = [1, 2, 3]
lista2 = [4, 5, 6, 12]

zip1 = zip(lista1, lista2, 'abc')

print(zip1)
print(type(zip1))

# Sempre podemos gerar uma Lista, Tupla, ou Dicionário

print(list(zip1))

'''
IMPORTANTE: nas linhas abaixo foi necessário gerar o objeto zip1 antes de cada conversão porque objetos zip, assim como map e generator, têm seu conteúdo excluído
logo após o seu uso em uma conversão ou transformação.
'''

zip1 = zip(lista1, lista2, 'abc')
print(tuple(zip1))

zip1 = zip(lista1, lista2, 'abc')
print(set(zip1))

zip1 = zip(lista1, lista2)
print(dict(zip1))

'''
OBS: O zip() utiliza como parâmetro o menor tamanho em iterável. Isso significa que se estiver trabalhando com iteráveis de tamanhos diferentes, 
irá parar quando os elementos do menor iterável acabar.
'''

lista3 = [7, 8, 9, 10, 11]

zip1 = zip(lista3, lista2, lista1)
print(list(zip1))

# Numa única operação zip, é possível utilizar diferentes tipos de iteráveis. O exemplo abaixo utiliza uma tupla, uma lista e OS VALORES de um dicionário.
tupla = 1, 2, 3, 4, 5
lista = [6, 7, 8, 9, 10]
dicionario = {'a': 11, 'b': 12, 'c': 13, 'd': 14, 'e': 15}

zt = zip(tupla, lista, dicionario.values())
print(list(zt))

# Lista de tuplas
dados = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]

# IMPORTANTE: o * à frente da variável dados indica ao Python para realizar o desempacotamento dos dados presentes em dados (desculpe o trocadilho).
print(list(zip(*dados)))
"""
# Exemplos mais complexos
"""
'''
No exemplo abaixo temos o nome do aluno e suas notas em duas provas distintas. O objetivo é montar um dicionário cuja chave seja o nome do aluno e o valor será
a maior nota obtida pelo aluno entre as duas provas.
'''
prova1 = [80, 91, 78]
prova2 = [98, 89, 53]
alunos = ['maria', 'pedro', 'carla']

final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}

print(final) # Imprime {'maria': 98, 'pedro': 91, 'carla': 78}. Ou seja: a maior nota de maria foi 98, a de pedro 91 e a de carla foi 78.

# Podemos utilizar o map()
final = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))

print(dict(final))
