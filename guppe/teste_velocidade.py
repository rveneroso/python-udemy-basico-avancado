"""
Teste de Velocidade com Expressões Geradoras

# Generators (Geradores)


def nums():
    for num in range(1, 10):
        yield num


ge1 = nums()

print(ge1)  # Generator

print(next(ge1))
print(next(ge1))


# Generator Expression

ge2 = (num for num in range(1, 10))

print(ge2)  # Generation Expression

print(next(ge2))
print(next(ge2))
"""

# Realizando o teste de velocidade
import time

# Generator Expression

gen_inicio = time.time()
print(sum(num for num in range(100000000)))  # 100  milhões
gen_tempo = time.time() - gen_inicio


# List Comprehension

list_inicio = time.time()
print(sum([num for num in range(100000000)]))  # 100 milhões
list_tempo = time.time() - list_inicio

# Na minha máquina Genetor Expression concluiu com 8.46 segundos e List Comprehension concluiu com 14.37 segundos. Essa diferença foi bem mais
# acentuada no meu ambiente do que nos testes feitos na aula.
print(f'Generator Expression levou {gen_tempo}')
print(f'List Comprehension levou {list_tempo}')

