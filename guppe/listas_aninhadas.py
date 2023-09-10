'''
Listas aninhadas são arrays ou matrizes em Python
'''

'''
Abaixo temos uma matriz 3 X 3 - 3 colunas por 3 linhas onde:
- linha 0 -> [1, 2, 3]
- linha 1 -> [4, 5, 6]
- linha 2 -> [7, 8, 9]
- linha 0, coluna 0 -> 1
- linha 0, coluna 1 -> 2
- linha 0, coluna 2 -> 3
- linha 1, coluna 0 -> 4
- linha 1, coluna 1 -> 5
- linha 1, coluna 2 -> 6
- linha 2, coluna 0 -> 7
- linha 2, coluna 1 -> 8
- linha 2, coluna 2 -> 9
'''
lista = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
linha = 0
for linhas in lista:
    coluna = 0
    for colunas in linhas:
        # print(f'Na linha {linha}, coluna {coluna} temos o elemento {lista[linha][coluna]}')
        coluna += 1
    linha += 1

'''
Realizando a iteração acima (somente a iteração, sem a impressão das posições) usando List comprehension

IMPORTANTE: observar a necessidade de se separar os resultados de cada for com colchetes
'''
[[print(valor) for valor in lista_individual] for lista_individual in lista]
