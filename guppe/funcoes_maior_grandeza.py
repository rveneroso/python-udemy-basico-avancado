"""
Funções de Maior Grandeza - Higher Order Functions - HOF

O que isso significa?

- Quando uma linguagem de programação suporte HOF, indica que podemos ter funções
que retornam outras funções como resultado ou mesmo que podemos passar funções
como argumentos para outras funções, e até mesmo criar variáveis do tipo de funções
nos nossos programas.

OBS: Na seção de funções, nós utilizamos isso.

Em Python, as funções são Cidadões de Primeira Classe, First Class Citizen
"""

# Exemplo - Definindo as funções

def somar(a, b):
    return a + b


def diminuir(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b


def calcular(num1, num2, funcao):
    return funcao(num1, num2)


# Testando as funções

print(calcular(4, 3, somar))

print(calcular(4, 3, diminuir))

print(calcular(4, 3, multiplicar))

print(calcular(4, 3, dividir))


# Nested Functions - Funções Aninhadas

# Em Python podemos também ter funções dentro de funções, que são conhecidas por Nested Functions
# ou também Inner Functions (Funções Internas).

# Exemplo

from random import choice

def cumprimento(pessoa):
    def humor():
        return choice(('E ai ', 'Suma daqui ', 'Gosto muito de você '))
    '''
    IMPORTANTE: aqui o retorno da função cumprimento é o resultado da execução humor() concatenado com o nome da pessoa que foi passado como argumento
    '''
    return humor() + pessoa


# Testando
print(cumprimento('Angelina'))
print(cumprimento('Felicity'))


# Retornando funções de outras funções

from random import choice


def faz_me_rir():
    def rir():
        return choice(('hahahahahaha', 'kkkkkkkkkk', 'yayayayayayayaya'))
    '''
    IMPORTANTE: aqui o retorno da função faz_me_rir é a própria funçlão rir e não o resultado da execução da função rir.
    Isso é bem diferente pois permite que a função sendo retornada seja executada posteriormente através de uma variável que receba o 
    retorno da função faz_me_rir().
    '''
    return rir


# Testando

rindo = faz_me_rir()
'''
Como mencionado acima, a variável rindo recebeu o retorno da função faz_me_rir que é a função rir. Por isso, na linha abaixo, a execução de rindo()
é o mesmo que a execução de rir().
'''
print(rindo())

# Inner Functions (Funções Internas / Nested Functions) podem acessar o escopo de funções mais externas.
from random import choice

def faz_me_rir_novamente(pessoa):
    def dando_risada():
        risada = choice(('hahahahaha', 'lolololololo', 'kkkkkkkkkkk'))
        return f'{risada} {pessoa}'
    return dando_risada


# Testando

rindo = faz_me_rir_novamente('Fernanda')

print(rindo())
print(rindo())
print(rindo())



