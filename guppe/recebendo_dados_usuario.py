"""
Recebendo dados do usuário.

Em Python, tudo o que entra via input é String
"""
# print("Qual o seu nome?")
# nome = input()

# Fazendo a entrada de dados em uma única linha
nome = input('Qual o seu nome? ')

# Para imprimir apenas um parâmetro, funciona a sintaxe abaixo.
print('Seja bem vindo(a) ', nome)

# A sintaxe abaixo também funciona para a impressão de um único parâmetro.
# Sintaxe da versão 2.x do Python
print('Seja bem vindo(a) %s' % nome)

# Utilizando a sintaxe da versão 3 e acima
print('Seja bem vindo(a) {0}'.format(nome))

# Sintaxe mais atual
print(f'Seja bem vindo(a) {nome}')

# print("Qual sua idade? ")
# idade = input()
# idade = input('Qual sua idade?')

# É possível fazer cast de String para o tipo desejado já no input
idade = int(input('Qual sua idade?'))

# Para imprimir 2 ou mais parâmetros, funciona a sintaxe abaixo.
# Sintaxe da versão 2.x do Python
print('%s tem %s anos' % (nome,idade))

# Sintaxe mais atual
print(f'{nome} tem {idade} anos')

# Utilizando a sintaxe da versão 3 e acima
print('{0} tem {1} anos'.format(nome, idade))

# Calculando a idade com cast
print(f'A pessoa {nome} nasceu em {2023-int(idade)}')