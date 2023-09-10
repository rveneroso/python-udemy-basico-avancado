nome = 'Geek University'
lista = [1, 2, 3, 4, 5]
numeros = range(1,15)

# Esse for se utiliza de uma conversão implícita da string em um array de caracteres
for letra in nome:
    print(letra)

# Esse for percorre o conteúdo da variável lista. Interessante observar que a sintaxe do comando
# for é a mesma do exemplo anterior.
for numero in lista:
    print(numero)

# OBSERVAÇÃO: no range, o segundo parâmetro não é inclusivo. Ou seja: ele não faz parte da faixa a ser
# considerada
for numero in numeros:
    print(numero) # O número 15 não será impresso.

# Quando se acessa parte de um objeto com a sintaxe variavel[inicio:fim], não há nenhum problema em se indicar
# em 'fim' um valor que vai além do tamanho verdadeiro de variavel.
#
# marca = 'Mercedes Benz'
# print(marca[5:120])
# vai imprimir
#   des Benz
#
# Porém, se se tentar acessar diretamente uma posição que não exista efetivamente no objeto, um erro
# acontecerá.
# print(marca[14])
#
# resultará em erro:
# print(marca[14])
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: string index out of range

marca = 'Mercedes Benz'

#enumerate cria uma lista de tuplas onde cada tupla é composta pelo índice e pelo valor associado àquele
# índice.
for indice, letra in enumerate(marca):
    print(f'Índice: {indice}')
    print(f'Letra: {letra}')

# Caso se queira ver as tuplas geradas pelo enumerate, pode-se utilizar o código abaixo.
for valor in enumerate(marca):
    print(valor)

# Alterando o comportamento padrão de mudança de linha em um comando print
for _,letra in enumerate(marca):
    print(letra,end="")
