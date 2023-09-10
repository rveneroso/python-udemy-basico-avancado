'''
Não confundir Map sendo tratado aqui com os chamados Mapas apresentados anteriormente (que na verdade são
dicionários).

'''
import math

def area(r):
    """ Calcula a área de uma circunferência de raio 'r'"""
    return math.pi * (r ** 2)

print(area(2))
print(area(5.7))

raios = [2.27, 3.08, 14.75, 2, 0.78]
# Gerando uma lista de áreas da maneira tradicional
areas = []
for raio in raios:
    areas.append(area(raio))
print(areas)

''' 
Utilizando map
Map é uma função que recebe dois parâmetros: O primeiro a função, o segundo um iterável. 
Retorna um Map Object.
Na linha abaixo será criado um objeto map gerado a partir de sucessivas chamadas à função area,
sendo uma chamada para cada valor presente na lista raios.
'''
areas = map(area, raios)

print(areas) # Imprime <map object at 0x7f95e6533d90>
print(type(areas)) # Imprime <class 'map'>
'''
Converte o objeto areas (map) para list e imprime seu conteúdo.
IMPORTANTE: apesar do nome map, o objeto areas não contém chave:valor. Contém somente o resultado
do cálculo da área para cada um dos raios presentes na lista raios.
'''
print(list(areas))

'''
É possível eliminar a definição da função area e convertê-la para uma expressão lambda chamada diretamente
dentro do bloco de código onde se deseja obter os resultados.
'''
print(list(map(lambda r: math.pi * (r ** 2), raios)))
'''
IMPORTANTE: uma vez que o conteúdo de um map seja utilizado, seja em uma iteração ou na conversão
para outro objeto qualquer, seu conteúdo é apagado.
'''

# Usando lambda para converter temperaturas de celsius para farenheit. As temperaturas a serem convertidas
# estão em uma lista e cada uma é associada a uma cidade.
cidades = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26), ('Tokio', 27), ('Nova York', 28),
           ('Londres', 22)]
print(cidades)
c_para_f = lambda dado: (dado[0], (9/5) * dado[1] + 32)
print(list(map(c_para_f, cidades)))