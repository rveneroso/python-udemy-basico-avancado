"""
O bloco with

Passo para se trabalhar com arquivos

# 1 - Abrimos o arquivo
# 2 - Manipulamos o arquivo
# 3 - Fechamos o arquivo

O block with é utilizado para criar um contexto de trabalho onde os recursos
utilizados são fechados após o bloco with.

arquivo = open('texto.txt')

"""

# O block with - Forma Pythônica de manipular arquivos
with open('texto.txt') as arquivo:
    print(arquivo.readlines())
    print(arquivo.closed) # Como ainda estamos no contexto do bloco with, o arquivo ainda está aberto.

print(arquivo.closed) # Aqui o arquivo já está fechado.

