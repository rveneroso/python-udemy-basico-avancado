'''

Em Python, o dicionário padrão não garante a ordem de inserção de seus elementos. Pode até acontecer da ordem de inserção ser mantida mas não há garantias
com relação a isso.

Ordered Dict veio para solucionar essa questão.
'''

from collections import OrderedDict

dict = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4,})
for chave, valor in dict.items():
    print(f'Chave={chave}:{valor}')

dict.update({'h':8})
dict.update({'f':6})
dict.update({'g':7})
for chave, valor in dict.items():
    print(f'Chave={chave}:{valor}')

# Importante: uma comparação entre dicionários comuns irá retornar True desde que os elementos de um dicionário estejam presentes no outro
dict1 = {'a':1, 'b': 2}
dict2 = {'b':2, 'a': 1}
# A condição abaixo retornará True porque, como a ordem não importa, basta que todos os elementos de um dicionário estejam presentes no outro.
if(dict1 == dict2):
    print('Os dicionários são iguais')

# Com dicionários ordenados a ordem importa.
dict3 = OrderedDict({'a':1, 'b': 2})
dict4 = OrderedDict({'b':2, 'a': 1})
# A condição abaixo retornará False
if(dict3 == dict4):
    print('Os dicionários são iguais')
else:
    print('Os dicionários não são iguais')
