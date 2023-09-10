"""
Preservando metadatas com wraps

Metadados -> São dados intrísecos em arquivos.

wraps -> São funções que envolvem elementos com diversas finalizades.
"""

# Problema
def ver_log(funcao):
    def logar(*args, **kwargs):
        # Eu sou uma função (logar) dentro de outra
        print(f'Você está chamando {funcao.__name__}')
        print(f'Aqui a documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    ''' Soma dois números. '''
    return a + b


# print(soma(10, 30))
'''
Aqui ocorre o problema que se deseja apresentar e resolver nessa aula: as linhas abaixo deveriam mostrar o nome e a documentação da função soma.
Porém, como essa função está decorada com a função ver_log, o nome e a documentação impressas serão os da função ver_log e não da função soma 
como seria de se esperar.
'''
print(soma.__name__)  # soma
print(soma.__doc__)  # Soma dois números.


# Resolução do Problema

from functools import wraps

print('\nDesse ponto em diante as impressões são feitas pelo código já corrigido\n')
def ver_log(funcao):
    '''
    A solução para o problema apresentado acima é simples: basta anotar com @wraps a função interna na qual os atributos __name__ e __doc__ são
    utilizados.
    '''
    @wraps(funcao)
    def logar(*args, **kwargs):
        """Eu sou uma função (logar) dentro de outra"""
        print(f'Você está chamando {funcao.__name__}')
        print(f'Aqui a documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    """ Soma dois números. """
    return a + b


print(soma(10, 30))

print(soma.__name__)  # soma
print(soma.__doc__)  # Soma dois números.

print(help(soma))
