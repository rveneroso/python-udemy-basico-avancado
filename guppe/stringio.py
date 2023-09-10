"""
StringIO

ATENÇÃO: Para ler ou escrever dados em arquivos do sistema operacional o software precisa ter permissão:
    - Permissão de Leitura -> Para ler o arquivo.
    - Permissão de Escrita -> Para escrever o arquivo.


StringIO -> Utilizado para ler e criar arquivos em memória.
"""

from io import StringIO

mensagem = 'Este é apenas uma string normal'

# Podemos criar um arquivo em memória já com uma string inserida ou mesmo vazio para inserirmos texto depois
arquivo = StringIO(mensagem)
'''
A abertura do arquvo com StringIO é equivalente à abertura do arquivo da seguinte maneira:
    arquivo = open('arquivo.txt', 'w')
'''

# Uma vez que o arquivo tenha sido criado com StringIO, todas as demais operações que se aplicam a arquivos regulares gravados no sistema operacional podem
# ser utilizadas.
print(arquivo.read())

# Escrevendo outros textos
arquivo.write(' Outro texto')

# Podemos inclusive movimentar o cursor
arquivo.seek(0)

print(arquivo.read())
