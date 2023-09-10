'''
Como o nome indica, filter é utilizado para filtrar dados de coleções
'''

paises = ['', 'Austrália', 'Rússia', '', 'Brasil', 'Ucrânia', '', '', 'Alemanha', 'Áustria','']
# Remove da lista os países que não foram informados
res = list(filter(None, paises))
print(res)

# Realizando o mesmo filtro, agora com lambda
res = list(filter(lambda paises: len(paises)>0, paises))
print(res)
# A solução que utiliza None é mais Pythônica

'''
A diferenca entre map() e filter() é:

map() -> Recebe dois parâmetros, uma função e um iterável e retorna um objeto mapeando a função para 
cada elemento do iterável.

filter() -> Recebe dois parâmetros, uma função e um iterável e retorna um objeto filtrando apenas 
os elementos de acordo com a função.
'''
usuarios = [
    {"username": "samuel", "tweets": ["Eu adodo bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": []}
]
# Filtrar os usuários que estão inativos no Twitter. Usuários inativos são aqueles que não postaram
# nenhum tweet
inativos = list(filter(lambda usuario: len(usuario['tweets']) == 0, usuarios))
print(inativos)

# Uma forma ainda mais simples de se fazer o mesmo filtro.
# Importante lembrar que [], quando tratado como um boolean, retorna False.
print(bool([])) # Imprime False
# Assim, um usuário em que 'tweets' esteja vazio, irá retorna False. Com o operador not mudando esse valor,
# temos True e aí o usuário em questão entra no filro.
inativos = list(filter(lambda usuario: not usuario['tweets'], usuarios))
print(inativos)

# Combinando filter() e map()
nomes = ['Vanessa', 'Ana', 'Maria']

'''
Devemos criar uma lista contendo 'Sua instrutora é' + nome, desde que cada nome tenha menos de 5 caracteres
Vale lembrar que map aceita dois parâmetros: a função a ser executada e os dados.
A função é um lambda que simplesmente adiciona o nome a um texto. Já os dados serão retornados de acordo
com o filter. Como só nos interessam nomes com menos de 5 caracteres, o único nome retornado será Ana.
'''
lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))

print(lista)