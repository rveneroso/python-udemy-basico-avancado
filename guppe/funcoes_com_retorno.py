'''
Na aula em que esse arquivo Python foi escrito não foi falado nada que eu ainda não soubesse sobre funções.

'''

from random import random
def funcao_unica():
    return 2, 3, 4, 5

def lanca_moeda():
    if random() > 0.5:
        return 'Cara'
    return 'Coroa'

minha_variavel = funcao_unica();
print(f'O tipo de retorno da função funcao_unica é {type(minha_variavel)}') # Imprime O tipo de retorno da função funcao_unica é <class 'tuple'>

for i in range(1,101):
    print(lanca_moeda())
