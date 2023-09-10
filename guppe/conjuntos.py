'''
Em Python conjuntos são chamados de Sets

- Conjuntos não possuem valores duplicados
- Conjuntos não possuem valores ordenados
- Elementos não são acessados via índices. Ou seja: conjuntos não são indexados.

Conjuntos são úteis nos cenários em que a ordenação não importa e também não há a preocupação com chaves duplicadas.

Os conjuntos em Python são referenciados por {}. Como os dicionários também são referenciados por {}, deve-se observar que um dicionário tem chave/valor
ao passo que um conjunto tem apenas valor.

É possível criar sets a partir de listas e tuplas.

Sets seguem o padrão de Deep Copy e Shallow Copy das demais coleções.

'''

# IMPORTANTE: sets não garantem a ordem dos elementos nem mesmo no momento da criação. Em uma das execuções do código abaixo, ao imprimir o set gerado,
# o resultado foi: {'Terra', 'Saturno', 'Urano', 'Netuno', 'Vênus', 'Marte', 'Júpiter', 'Mercúrio'}
planetas = {'Mercúrio', 'Vênus', 'Terra', 'Marte', 'Júpiter', 'Saturno', 'Urano', 'Netuno'}
print(planetas)
print(type(planetas))

# Outra forma de se criar um set.
# IMPORTANTE: como sets não admitem repetições, os itens informados mais de uma vez no set abaixo serão automaticamente descartados.
numbers = set({1, 2, 3, 4, 5, 5, 6, 7, 7, 7, 8, 9, 10, 3})
print(numbers)
print(type(numbers))

# O operador in pode ser usado também em conjuntos
if 'Júpiter' in planetas:
    print('Encontrei Júpiter. Vou me mudar para lá.')

# Sets aceitam diferentes tipos de dados em seus elementos
misc = {1, 'Mercedes', 81000.0, True, 7j}
print(misc)

for planeta in planetas:
    print(planeta)

# Para adicionar um elemento a um set
planetas.add('Plutão')
print(planetas)

# Removendo elementos de um set
# IMPORTANTE: a tentativa de remoção de um item inexistente no conjunto resulta em um keyerror
# Nenhum valor é retornado.
planetas.remove('Plutão')
print(planetas)

# Outra maneira de remover um item de um set. Aqui também, nenhum item é retornado como resultado da execução da função discard
planetas.discard('Plutão')
planetas.discard('Kíron')
# IMPORTANTE: com discard não serã lançado nenhum keyerror caso o elemento passado como argumento não exista no set.

# Assim como acontedce com as demais coleções, clear() apaga todo o conteúdo de um set.
planetas_backup = planetas.copy()
print(planetas_backup)
planetas_backup.clear()
print(planetas_backup)

cj1 = {'Honda', 'Suzuki', 'Kawasaki', 'KTM', 'Yamaha', 'Aprilia', 'Ducati'}
cj2 = {'Triumph', 'Norton', 'Ducati', 'Gas Gas', 'KTM'}
# União de sets (conjuntos) pode ser feita de duas formas diferentes.
cj3 = cj1.union(cj2)
print(cj3)

cj3 = cj1 | cj2
print(cj3)

# Interseção de sets (conjuntos) pode ser feita de duas formas diferentes.
cj3 = cj1.intersection(cj2)
print(cj3)

cj3 = cj1 & cj2
print(cj3)

# Diferenças entre conjuntos
motos1 = cj1.difference(cj2) # Motos que estão apenas em cj1
print(motos1)
motos2 = cj2.difference(cj1) # Motos que estão apenas em cj2
print(motos2)

# As funções sum(), min(), max() aplicam-se também a conjuntos desde que os elementos sejam inteiros ou reais.