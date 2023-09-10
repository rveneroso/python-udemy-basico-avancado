'''
Tuplas são imutáveis. Toda operação em uma tupla já existente gera uma nova tupla.

É semelhante à Strings no Java.

Tuplas são definidas pela presença de vírgulas e não pela presença de parênteses (vide exemplos abaixo).

Como tuplas são imutáveis, não existem métodos para a adição e remoção de elementos nelas.

Por quê utilizar tuplas em vez de listas?
1 - Tuplas são mais rápidas que listas. Para grandes volumes de dados, isso faz muita diferença.
2 - Tuplas são mais seguras já que são imutáveis.

'''

# Embora as tuplas sejam identificadas pelos parênteses, Python permite que elas sejam criadas sem os
# parênteses.
tupla1 = (1, 2, 3, 4, 5)
tupla2 = 5, 4, 3, 2, 1
print(f'tupla1: {tupla1}, tipo de tupla1 {type(tupla1)}')
print(f'tupla2: {tupla2}, tipo de tupla2 {type(tupla2)}')

# IMPORTANTE: uma variável criada com um valor simples entre parênteses NÃO É UMA TUPLA.
# É apenas um inteiro.
pseudo_tupla = (4)
print(f'pseudo_tupla {pseudo_tupla}, tipo de pseudo_tupla {type(pseudo_tupla)}')

# Porém, a variável abaixo É UMA TUPLA
tupla3 = (4,)
print(f'tupla3 {tupla3}, tipo de tupla3 {type(tupla3)}')

# Assim como acontece com listas, tuplas também podem ser geradas a partir de range
tupla_range = tuple(range(7,22))
print(tupla_range)

# Tuplas também podem ser desempacotadas e as regras de desempacotamento são as mesmas aplicadas em listas.
marca, modelo = ('Mercedes-Benz', 'C 180')
print(f'Marca: {marca}, modelo: {modelo}')

# Funções para a obtenção da soma, valor máximo, valor mínimo e tamanho também podem ser aplicadas às
# tuplas, DESDE QUE TODOS OS ELEMENTOS DA TUPLA SEJAM INTEIROS OU REAIS.
print('Dados de tupla4')
tupla4 = 1, 2, 3, 4, 5
print(sum(tupla4))
print(max(tupla4))
print(min(tupla4))
print(len(tupla4))

print('\nDados de tupla_real')
tupla_real = 2.3, 18.75, 9.07, 12.0, 4.88
print(sum(tupla_real))
print(max(tupla_real))
print(min(tupla_real))
print(len(tupla_real))

# Embora tuplas sejam imutáveis, é possível alterá-las. Assim como Strings em Java, um novo objeto
# será criado para conter as alterações realizadas.
# As linhas abaixo mostram que o id da tupla tp1 mudou depois que ela foi concatenada com tp2.
# O id da tupla tp2 permaneceu o mesmo.
tp1 = 1, 2, 3
tp2 = 4, 5, 6
print(f'Antes da concatenação - tp1: {tp1}, id de tp1 {id(tp1)} ')
print(f'Antes da concatenação - tp2: {tp2}, id de tp2 {id(tp2)} ')
tp1 = tp1+ tp2
print(f'Depois da concatenação - tp1: {tp1}, id de tp1 {id(tp1)} ')
print(f'Depois da concatenação - tp2: {tp2}, id de tp2 {id(tp2)} ')

# Os recursos de pesquisa (in), iteração (for) e demais que são válidos para listas, aplicam-se também
# às tuplas. Não vou escrever exemplos aqui.

# Contando a ocorrência de um deerminado elemento em uma tupla
tpc = ('a', 'b', 'c', 'd', 'e', 'b', 'a')
print(tpc.count('a'))
print(tpc.count('b'))
print(tpc.count('e'))

tp_a = ('Rossi', 'Doohan', 'Simoncelli')
# Com tuplas não temos o efeito shallow copy que aocntece com listas. A linha abaixo atribui o mesmo id
# à ambas as tuplas.
tp_b = tp_a
print(f'Conteúdo de tp_a: {tp_a}; Id de tp_a: {id(tp_a)}')
print(f'Conteúdo de tp_b: {tp_b}; Id de tp_b: {id(tp_b)}')
print(f'\nAgora iremos alterar o conteúdo de tp_b e verificar os conteúdos e ids de ambas as tuplas')
tp_c = 'Stoner',
# Como tuplas são imutáveis, ao adicionar tp_c à tp_b, um novo objeto é criado e tp_b recebe um novo id.
# Esse id passa a ser diferente do id de tp_a. Portanto, tp_a permanece com o id e conteúdo originais.
tp_b = tp_b + tp_c
print(f'Conteúdo de tp_a: {tp_a}; Id de tp_a: {id(tp_a)}')
print(f'Conteúdo de tp_b: {tp_b}; Id de tp_b: {id(tp_b)}')