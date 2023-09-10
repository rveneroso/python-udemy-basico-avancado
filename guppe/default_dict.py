'''

Default Dict não apresenta o keyerror

Quando se cria um Default Dict, deve-se informar o valor default a ser usado quando uma chave sendo pesquisada não existir.
Quando isso ocorre, a entrada será criada com aquela chave e o valor associada será o valor default informado na criação do default dict.

Todas as demais funções que se aplicam à dicionários regulares, aplicam-se também ao Default Dict

'''
from collections import defaultdict
default = defaultdict(lambda :0)
default['curso'] = 'Programação em Python: Essencial'
print(default) # Imprime defaultdict(<function <lambda> at 0x7f7c31486340>, {'curso': 'Programação em Python: Essencial'})
print(default['Java']) # Não existe essa chave no dicionário. Porém, não ocorrerá o keyerror. Em vez disso, será criada a entrada 'Java' com o valor 0 associado a ela.
print(default) # Imprime defaultdict(<function <lambda> at 0x7f933c18b060>, {'curso': 'Programação em Python: Essencial', 'Java': 0})