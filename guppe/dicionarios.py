'''
Dicionários são equivalentes a Maps do Java: são coleções do tipo chave-valor.

Dicionários são representados por {}

Dicionários NÃO SÃO IMUTÁVEIS

A chave é separada do valor por : (dois pontos).
Tanto a chave quanto o valor podem ser de qualquer tipo.

'''

# Existem duas formas de se criar um dicionário:
paises1 = {"br": "Brasil", "au": "Austrália", "de": "Alemanha"}
print(paises1)
print(type(paises1))

paises2 = dict(br="Brasil",au="Austrália",de="Alemanha")
print(paises2)
print(type(paises2))

# Dicionários não são indexados então a forma de acessar seus elementos é um pouco diferente.
# A forma abaixo é semelhante ao acesso em listas/tuplas.
print(paises1["au"])

# Se se tentar acessar um elemento para o qual não exista a chave, um erro será apresentado.
# print(paises1["ru"])


# A outra forma de se acessar um elemento é via função get()
print(paises1.get("br"))
'''
Diferentemente do que acontece com o acesso via chave, com get() se a chave sendo pesquisada não existir
não teremos o keyerror. O retorno será None. Por essa razão é aconselhado que se use sempre a função get()
O tipo None é sempre considerado FALSO.
'''
print(paises1.get("ru"))

'''
É possível também definir um valor default a ser assumido para os casos em que a chave sendo pesquisa não
for encontrada. No exemplo abaixo, a variável russia receberá o valor 'Puttin deve estar muito bravo' já
que o dicionário não possui uma entrada com chave = 'ru'
'''
russia = paises1.get("ru", "Puttin deve estar muito bravo")
print(russia)

# O operador in também pode ser utilizado com dicionários
print("br" in paises1)
print("ru" in paises1)
# A linha abaixo também retorna False pois a palavra "Austrália" ocorre no dicionário como valor e não como
# chave.
print("Austrália" in paises1)

# Uma das formas de se adicionar uma entrada a um dicionário é a seguinte:
paises1["nz"] = 'Nova Zelândia'
print(paises1)

# Segunda forma de se adicionar itens a um dicionário é criar uma variável com a mesma estrutura de cada
# elemento do dicionário e em seguida utilizar a função update no dicionário passando a variável criada
# anteriormente.
japao = {'jp':'Japão'}
paises1.update(japao)
print(paises1)

# O update também pode ser utilizado especificando-se diretamente o novo par chave-valor sem a necessidade de
# criação prévia de uma variável.
paises1.update({'pl':'Polônia'})
print(paises1)

# O update não serve apenas para adicionar um novo elemento a um dicionário. Ele permite que o valor de uma
# chave seja atualizado.
paises1.update({'ar':'Arjentina'})
print(paises1)
# Corrige o nome do país
paises1.update({'ar':'Argentina'})
print(paises1)

# Para remover elementos de um dicionário existem duas formas.
# Primeira: informando a chave a ser removida no método pop(). Se a chave passada ao método pop() não existir
# no dicionário, um KeyError será retornada.
# Ao removermos um item de um dicionário, o valor da chave removida é retornado.
paises1.pop('br')
print(paises1)
# paises1.pop('br')

# A segunda forma de se remover um item de um dicionário.
# Com del, também será gerado um KeyError caso a chave a ser removida não exista no dicionário.
del paises1['jp']
print(paises1)

# Métodos para manipulação de dados de dicionários
# Apagar o conteúdo de um dicionário
d = dict(a=1, b=2, c=3)
print(d)
d.clear()
print(d)

# Copiando um dicionário
# Deep copy
d = dict(a=1, b=2, c=3)
novo = d.copy()
novo.update({'d':8})
print(d)
print(novo)

# Shallow copy
d = dict(a=1, b=2, c=3)
novo = d
novo.update({'d':8})
print(d) # Por ser shallow copy, o dicionário d sofreu a mesma alteração aplicada ao dicionário novo
print(novo)

# Criando um dicionário utilizando a função fromKeys().
# IMPORTANTE: fromkeys() somente aceita 2 argumentos: o primeiro é a chave, o segundo é o valor
dc ={}.fromkeys('a',1)
print(dc)

# É possível passar uma lista de chaves no primeiro argumento de fromkeys. Dessa forma, serão criadas todas as chaves informadas, cada uma recebendo o valor
# único que for especificado no segundo argumento.
usuarios = {}.fromkeys(['nome','endereco','telefone','email'],'Indefinido')
# A linha acima resultará em um dicionário com a seguinte estrutura: {'nome': 'Indefinido', 'endereco': 'Indefinido', 'telefone': 'Indefinido', 'email': 'Indefinido'}
print(usuarios)

# Quando se usa uma String como chave de um dicionário, cada caracter da String será uma chave no dicionário tendo associada a si, o valor informado no segundo argumento.
letras = {}.fromkeys('teste', 'valor')
print(letras)
# O dicionário resultante será o seguinte: {'t': 'valor', 'e': 'valor', 's': 'valor'}
# Vale lembrar que dicionários não aceitam repetições nas chaves. Por isso, no exemplo acima, as letras 't' e 'e' ocorrem apenas uma vez.

# Podemos usar range para criar as chaves de um dicionário
dc_range = {}.fromkeys(range(1,6),'valor') # {1: 'valor', 2: 'valor', 3: 'valor', 4: 'valor', 5: 'valor'}
print(dc_range)