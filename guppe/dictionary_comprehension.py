'''
Dictionary comprehension são muito semelhantes à List comprehension
O que muda basicamente é que é preciso informar o par chave:valor para o dicionário
'''
lista = [1, 2, 3, 4]
'''
A linha abaixo cria um dicionário onde a chave é o número convertido para String e o valor é o número
elevado ao quadrado.
'''
dict = {numero.__str__():numero ** 2 for numero in lista}
print(dict)

'''
É possível realizar a mesma operação acima com tuplas e sets
'''
tupla = (1, 2, 3, 4)
dict = {numero.__str__():numero ** 2 for numero in tupla}
print(dict)

set = (1, 2, 3, 4)
dict = {numero.__str__():numero ** 2 for numero in set}
print(dict)

chaves = 'abcde'
valores = [1, 2, 3, 4, 5]
print({chaves[i]:valores[i] for i in range(0,len(chaves))})

print({num: ('par' if num % 2 == 0 else 'impar') for num in valores})
