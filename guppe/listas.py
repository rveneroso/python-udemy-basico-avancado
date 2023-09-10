'''
Listas em Python são como arrays em outras linguagens. Porém, elas são dinâmicas e permitem
a inclusão de elementos de QUALQUER tipo de dado.

São dinâmicas porque não possuem tamanho fixo. Depois que uma lista é criada, pode-se ir inserindo
elementos nela sem se preocupar com o tamanho.

Também não há restrições quanto ao tipo de dado a ser inserido em uma lista.

Listas em Python são representadas por valores entre colchetes, separados entre si por vírgula.
'''

# Mesmo um par de abre e fecha colchetes é entendido como uma lista.
elemento = []
print(type(elemento)) # será impresso <class 'list'>

# A lista abaixo recebe elementos de diversos tipos de dados diferentes.
lista = [1, True, 'Isso é uma string', 4.0, 6j]
print(lista)

# É possível gerar uma lista com cada um dos caracteres que compôem uma string usando a função list
letras = list('Mercedes Benz')
print(letras)

# Pode-se verificar se um determinado valor está presente em uma lista com a cláusula in
numeros = list(range(11))
if 8 in numeros:
    print('Número 8 está presente na lista')
else:
    print('A lista de números não contém o 8')


# Uma lista pode ser ordenada através da função sort().
num = [2, 7, 27, 15, 8, 9, 4, 8, 27, 32, 64]
num.sort() # O resultado da função sort() automaticamente é aplicado à variável num.
print(num)

# A ordenação não se aplica apenas à listas de valores numéricos. String também podem ser ordenadas.
texto = 'Essa frase será usada como exemplo no programa de listas, mais especificamente, na ordenação'
palavras = list(texto.split())
palavras.sort()
print(palavras)

# Pode-se contar o número de ocorrências dentro de uma lista.
# Contando quantos números 27 existem na lista num
print(num.count(27)) # Imprime 2

# Para adicionar elementos à uma lista usamos a função append.
print(num)
num.append(38)
print(num)

'''
Com a função append só se pode adicionar um elemento por vez. Se tentarmos adicionar mais de um
elemento em uma única operação append, a execução terminará com erro.
A operação abaixo funciona mas ela não vai adicionar os números 58, 46 e 99 individualmente na lista
num. O que ela fará é adicionar a lista [58, 46, 99] ao fim da lista num.
'''
num2 = [58, 46, 99]
print(num)
num.append(num2)
print(num)

# A condição abaixo não irá retornar True porque o número 58 não existe como um elemento da lista num.
# Ele existe como um elemento da lista contida na lista num.
if 58 in num:
    print('Encontrei o número 58 na lista')
else:
    print('Não encontrei o número 58 na lista')

# Já a condição abaixo irá retornar True porque o número 58 está sendo procurado dentro do elemento
# de índice 12 da lista num e esse elemento é justamente a lista que contém o número 58.
if 58 in num[12]:
    print('Encontrei o número 58 na lista')
else:
    print('Não encontrei o número 58 na lista')
'''
Com a função extend, se uma lista1 for adicionada dentro de uma lista2, cada elemento de lista1
será adicionado individualmente dentro de lista2. O comportamento é diferente da função append.

IMPORTANTE: a função extend não aceita valor único como argumento. Ela só aceita um iterável.
Exemplos:
lista1.extend(46) -> Resulta em erro pois 46 é um valor único
lista1.extend([46]) -> Ok pois [46] é uma lista embora contenha apenas um elemento.
lista1.extend("a") -> Apesar de parecer que se trata de um único elemento, a operação é válida.
    Ao que parece, internamente o Python converte "a" para uma lista ['a']
lista1.extend("banana") -> Ok pois a string "banana" será convertida em uma lista com os caracteres
    que formam a palavra.
'''
lista_num1 = [1, 2, 3]
lista_num2 = [4, 5, 6]
print(lista_num1)
lista_num1.extend(lista_num2)
print(lista_num1)
lista_num1.extend([666])
print(lista_num1)
lista_num1.extend("a")
print(lista_num1)
lista_num1.extend("banana")
print(lista_num1)

'''
As funções append e extend sempre adicionam elementos ao final da lista. Porém, é possível inserir
elementos em uma posição específica com o uso da função insert.
É importante observar que a função insert não sobrescreve o valor existente na posição informada.
O que acontece é a inserção do novo valor na posição informada e os demais elementos são movidos
1 posição para a direita.
'''
l1 = [1, 2, 3, 4]
print(l1) # [1, 2, 3, 4]
l1.insert(3,666)
print(l1) # [1, 2, 3, 666, 4]

# O operador + quando aplicado em 2 listas tem o mesmo efeito da função extend()

# A função reverse inverte a ordem dos elementos de uma lista
print(f'Antes da inversão de seus elementos:\n {l1}')
l1.reverse()
print(f'Depois da inversão de seus elementos:\n {l1}')

# Recapitulando o que foi estudado em Strings, podemos também inverter a ordem dos elementos de uma lista
# com slice.
print(f'Depois da inversão de seus elementos com o uso de slice:')
l1 = l1[::-1]
print(l1)

# Para copiar uma lista
l2 = l1.copy()
print(f'A lista l2:\n{l2}')

# Identificando o tamanho de uma lista
print(len(l2))

# A função pop() remove o último item da lista. Além de remover o elemento, a função também
# retorna o elemento.
print(l2)
l2.pop()
print(l2)

# É possível também remover um item informando seu índice.
# IMPORTANTE: se não houver elemento no índice informado, uma mensagem de erro será retornada.
l2.pop(2)
print(f'l2 após a remoção do elemento na posição 2:\n{l2}')

# Para remover todos os elementos de uma lista
l2.clear()
print(f'l2 após a execução da função clear():\n{l2}')

# Ao se multiplicar uma lista por um número inteiro n, a lista resultante terá seus elementos
# replicados n vezes.
l_num = [1, 2, 3]
l_num = l_num * 3
print(l_num)

# Convertendo uma lista de elementos String em uma única String
palavras = ['Essa', 'é', 'minha', 'frase']
resultado = ' '.join(palavras) # Os elementos da lista serão unidos tendo um espaço entre si.
resultado_com_hifen = '-'.join(palavras) # Os elementos da lista serão unidos tendo um hífen entre si.
print(palavras)
print(resultado)
print(resultado_com_hifen)

# Iterando sobre listas com for
print('Iterando sobre listas com for\n')
for elemento in lista:
    print(elemento)

# É possível acessar os elementos de uma lista através de índices negativos. Nesse caso, é como se
# estivéssemos acessando a lista em ordem inversa.
l_num = [1, 2, 3]
print(l_num[-1])
print(l_num[-2])
print(l_num[-3])
# print(l_num[-4]) # Resulta em erro pois não existe posição 4 na lista

# Para se obter o índice em que um determinado elemento se encontra dentro da lista devemos usar a função
# index
print('Pesquisando elementos com a função index:\n')
lista_paises = ['Austrália', 'Itália', 'Rússia', 'Canadá', 'Irlanda']
print(lista_paises.index('Austrália'))
# Se o elemento pesquisado não existir na lista, ocorrerá erro.
# print(lista_paises.index('Bélgica')) # ValueError: 'Bélgica' is not in list
# Se o elemento sendo pesquisado ocorrer mais de uma vez na lista, somente será retornado o índice
# da primeira ocorrência encontrada.
print('Pesquisando o número 17 na lista\n')
numeros = [8, 17, 32, 99, 58, 17, 27]
print(numeros.index(17)) # Retorna o índice 1
# É possível informar à função index a posição a partir da qual iniciar a pesquisa.
# A linha abaixo indica que a pesquisa deve comeãr a partir da posição 2.
# Portanto, será impresso o índice da segunda ocorrência do número 17. Nesse caso, 5
print(numeros.index(17, 2))
# OBSERVAÇÃO: se o elemento pesquisado não for encontrado dentro da lista, qualquer que seja o método
# de pesquisa, o resultado será uma mensagem de erro.

# É possível ainda definir, além do índice inicial, o índice final para determinar em qual range a
# busca será feita.
# print(numeros.index(17, 2, 4)) # Resulta em erro.

# Para listas de elementos inteiros ou de ponto flutuante, pode-se aplicar as funções
# sum(), max() e min() que retornam, respectivamente, a soma, o maior valor e o menor valor
# presente na lista.
numeros = [1, 2, 3, 4, 5, 6]
print(f'A soma dos elementos da lista é {sum(numeros)}')
print(f'O maior valor encontrado na lista é {max(numeros)}')
print(f'O menor valor encontrado na lista é {min(numeros)}')
# Já a função len(), que retorna a quantidade dee elementos em uma lista, pode ser utilizada em listas
# contendo qualquer tipo de elementos.
print(f'O tamanho da lista é {len(numeros)}')

# Convertendo uma lista em tupla
tupla = tuple(numeros)
print(type(tupla))
print(tupla)

# O desempacotamento de listas consiste em transformar cada elemento de uma lista em uma variável
# independente.
# OBSERVAÇÃO: se for informado um número de variáveis menor do que a quantidade de elementos na lista
# um erro será gerado. Se houver mais variáveis do que elementos na lista, também ocorrerá um erro.
num = [1, 2, 3]
num1, num2, num3 = num;
print(f'num1 = {num1}')
print(f'num2 = {num2}')
print(f'num3 = {num3}')

# Existem duas formas de se copiar listas em Python.
# 1 - Deep Copy. É a forma que se aplica quando se utiliza a função copy(). O que o Python faz é criar
# um outro objeto contendo os mesmos elementos da lista original. Como se trata de objetos diferentes,
# modificações feitas em uma lista não afetam a outra.
#
# 2 - Shallow Copy. Trata-se de uma mera atribuição de um objeto a outro. As duas variáveis apontam
# para o mesmo objeto em memória. Portanto, qualquer alteração feita em um dos objetos irá se aplicar
# no outro objeto.


