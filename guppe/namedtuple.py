from collections import namedtuple

# Existem três diferentes formas de se criar uma namedtuple
# 1a. forma
cachorro = namedtuple('cachorro', 'idade raca nome')
print(cachorro)

# 2a. forma
dog = namedtuple('cachorro', 'idade, raca, nome')
print(dog)

# 3a. forma
hund = namedtuple('cachorro', ['idade', 'raca', 'nome'])
print(hund)

ray = cachorro(idade=2, raca='Chow-Chow', nome='Ray')
print(ray)

# Os campos do objeto cachorro podem ser acessados diretamente por seus nomes
print(ray.idade)
print(ray.raca)
print(ray.nome)