"""
Argumentos Somente Posicionais
"""

# valor = '67.3'
# print(float(valor))

# def cumprimenta_v1(nome):
#     return f'Olá {nome}'
#
# print(cumprimenta_v1('Geek'))
# print(cumprimenta_v1(nome='Geek'))


# def cumprimenta_v2(nome, /):
#     return f'Olá {nome}'
#
# print(cumprimenta_v2('Geek'))
# print(cumprimenta_v2(nome='Geek'))

# def cumprimenta_v3(nome, /, mensagem='Olá'):
#     return f'{mensagem} {nome}'
#
# print(cumprimenta_v3('Geek'))
# print(cumprimenta_v3('University', mensagem='Hello'))
# print(cumprimenta_v3('Felicity', 'Bem-vinda'))

# def cumprimenta_v4(nome, mensagem='Olá', /):
#     return f'{mensagem} {nome}'
#
# print(cumprimenta_v4('Geek'))
# print(cumprimenta_v4('Felicity', 'Bem-vinda'))
# print(cumprimenta_v4('University', mensagem='Hello'))

# def cumprimenta_v5(*, nome):
#     return f'Olá {nome}'
#
# print(cumprimenta_v5(nome='Geek'))
# print(cumprimenta_v5('Geek'))

'''
Quando criamos funções com argumentos somente posicionais, não é possível utilizar o recurso
de se atribuir o nome da variável diretamente na passagem do argumento à função.
Por exemplo: a função abaixo

    def cumprimenta_v4(nome, mensagem='Olá', /):
    
não irá permitir uma chamada a ela da seguinte forma:

    print(cumprimenta_v4(nome='João', mensagem='Vai garoto!!')
    
Somente é possível chamar a função passando diretamente os parâmetros sem nomeá-los:

    print(cumprimenta_v4('João', 'Vai garoto!!')

Quando colocamos a / após toda a lista de parâmetros dizemos ao Python que TODOS os parâmetros
da função são apenas posicionais.

Se quisermos que apenas alguns parâmetros sejam posicionais, basta colocar a / após cada um dos parâmetros.
A função abaixo

    def cumprimenta_v3(nome, /, mensagem='Olá'):
    
informa ao Python que o parâmetro nome é somente posisional mas o parâmetro mensagem não é. Por isso
todas as chamadas abaixo são válidas:

    print(cumprimenta_v3('Geek'))
    print(cumprimenta_v3('University', mensagem='Hello'))
    print(cumprimenta_v3('Felicity', 'Bem-vinda'))

'''

'''
Python permite também o oposto dos argumentos somente posicionais. É possível criar funções onde 
obrigatoriamente os parâmetros devem ser nomeados.

Por exemplo: a função

    def cumprimenta_v5(*, nome):
    
indica que o parâmetro nome deve ser obrigatoriamente informado ao se chamar a função cumprimenta_v5.

Por isso a chamada abaixo é válida

    print(cumprimenta_v5(nome='Geek'))

ao passo que a chamada abaixo NÃO É válida

    print(cumprimenta_v5('Geek'))

'''

'''
A função abaixo utiliza uma combinação das 3 formas diferentes de declaração de parâmetros: 
    * somente posicionais: parâmetro nome
    * opcionais: parâmetro mensagem1
    * nomeados e obrigatórios: parâmetro mensagem2
    
    
    
'''
def cumprimentar_v6(nome, /, mensagem1='Olá', *, mensagem2):
    return f'{mensagem1} {nome} {mensagem2}'

print(cumprimentar_v6('Geek', mensagem1='Hello', mensagem2='tenha um bom dia'))
print(cumprimentar_v6('Geek', mensagem2='tenha um bom dia'))
print(cumprimentar_v6('Geek', 'Oi', mensagem2='Vamos?'))

