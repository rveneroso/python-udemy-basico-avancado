'''
Python é uma linguagem de tipagem dinâmica, ou seja, ao se declarar uma variável não declaramos o seu
tipo. Esse tipo será inferido do valor que foi atribuído à variável.
'''

var_escopo_global = 18

if var_escopo_global > 23:
    var_escopo_local = 6
    var_escopo_global += 2

print(var_escopo_global)
# A linha abaixo resulta em erro pois, uma vez que o bloco do comando if não foi executado, a variável
# var_escopo_local não foi criada.
print(var_escopo_local)