'''
**kwargs é semelhante a *args. A principal diferença entre os dois é que **kwargs recebe os valores em
forma de dicionário enquanto que *args recebe os valores em forma de tupla.
'''

def imprime_cores_favoritas(**kwargs):
    for nome, cor in kwargs.items():
        print(f'A cor favorita de {nome.title()} é {cor}')

imprime_cores_favoritas(nicolas='verde',renato='azul',simone='amarelo')

# Assim como ocorre com *args, **kwargs não precisa ser o único parâmetro de uma função.

'''
IMPORTANTE: *args e **kwargs não são parâmetros obrigatórios
'''
imprime_cores_favoritas()

'''
IMPORTANTE: nas funções Python podem ser definidos todos os tipos de argumento listados abaixo mas eles
precisam ser declarados NESTA ORDEM:
1 - Parâmetros obrigatórios;
2 - *args
3 - Parâmetros não obrigatórios (default)
4 - **kwargs

Assim como acontece com *args, argumentos passados a funções que recebem **kwarges como parâmetros,
podem ser precedidas de ** para que o Python faça o desempacotamento de maneira implícita.
'''
