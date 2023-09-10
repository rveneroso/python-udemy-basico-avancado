'''
Dicionários em Python são também chamados de mapas
'''

receita = {'jan': 500, 'fev': 300, 'mar':450}
print(receita)

# Interagindo sobre o dicionário e imprimindo a chave
for chave in receita:
    print(chave)

# Interagindo sobre o dicionário e imprimindo o valor
for chave in receita:
    print(receita[chave])

# Imprimindo todas as chaves presentes no dicionário
chaves = receita.keys()
print(f'Chaves {chaves} é do tipo {type(chaves)}')

# O jeito correto para se interagir sobre as chaves de um dicionário
for chave in receita.keys():
    print(chave)

# Imprimindo todas os valores presentes no dicionário
valores = receita.values()
print(f'Valores {valores} é do tipo {type(valores)}')

# O jeito correto para se interagir sobre os valores de um dicionário
for valor in receita.values():
    print(valor)

# Desempacotamento de dicionários
for chave, valor in receita.items():
    print(f'Chave: {chave} = {valor}')

# Desde que os valores de um dicionário sejam inteiros ou reais, as funções de soma, valor mínimo, valor máximo podem ser aplicadas
print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita.values()))

cidades = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26), ('Tokio', 27), ('Nova York', 28),
           ('Londes', 22)]

c_para_f = lambda dado: (dado[0], (9/5) * dado[1] + 32)
