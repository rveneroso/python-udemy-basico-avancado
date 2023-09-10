'''
Sintaticamente Generator Expressions assemelham-se muito à tuplas.

Generator Expressions são sempre mais performáticos que as demais estruturas comprehension. Eles não armazenam em memória as estruturas que geram, até que elas
precisem ser utilizadas fora do bloco em que foram geradas. E mesmo assim, tão logo os dados sejam utilizados, eles são apagados.
'''

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']
# List Comprehension.
# Observar que a expressão está entre colchetes
res = [nome[0] == 'C' for nome in nomes]
print(type(res))
print(res)

# Generator
# Observar que a expressão está entre parênteses. Essa sintaxe induz a pensar que se trata de uma tupla mas é um Generator.
res = (nome[0] == 'C' for nome in nomes)
print(type(res))
print(res)

'''
Nas linhas que se seguem foram feitas medições da quantidade de memória utilizada por cada uma das estruturas List, Set e Dict Comprehension.
'''
from sys import getsizeof

# Gerando uma lista de números com List Comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])

# Gerando uma lista de números com Set Comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})

# Gerando uma lista de números com Dictionary Comprehension
dic_comp = getsizeof({x: x * 10 for x in range(1000)})

# Gerando uma lista de números com Generator
gen = getsizeof(x * 10 for x in range(1000))

'''
No meu ambiente foram obtidos os seguintes números:
List Comprehension: 8856 bytes
Set Comprehension: 32984 bytes
Dictionary Comprehension: 36952 bytes
Generator Expression: 208 bytes

Como se vê, Generator Expression ocupam uma quantidade absurdamente menor que as demais estruturas. Entre as demais, nota-se claramente que List Comprehension
é muito mais performático que Set e Dictionary.
'''
print('Para fazer a mesma tarefa gastamos em memória: ')
print(f'List Comprehension: {list_comp} bytes')
print(f'Set Comprehension: {set_comp} bytes')
print(f'Dictionary Comprehension: {dic_comp} bytes')
print(f'Generator Expression: {gen} bytes')

# Iterando sobre um Generator Expression
gen = (x * 10 for x in range(1000))
print(gen)
print(type(gen))

for num in gen:
    print(num)

