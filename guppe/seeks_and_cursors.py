"""
Seek e Cursors

seek() -> É utilizada para movimentar o cursor pelo arquivo.
"""
arquivo = open('texto.txt')
print(arquivo.read())

'''
Como foi mencionado na aula anterior, read() lê todo o conteúdo do arquivo de maneira que uma segunda execução de read() não traz nenhum conteúdo.
Porém, podemos usar a função seek() para levar o cursor a qualquer localização dentro do arquivo. 
Usando seek(0) faremos o cursor ir exatamente para o início do arquivo. Dessa forma, ao executarmos read() novamente, todo o conteúdo do arquivo será lido novamente.
# seek() -> A função seek() é utilizada para  movimentação do cursor pelo arquivo. Ela recebe um
# parâmetro que indica onde queremos colocar o cursor.
'''
arquivo.seek(0)
print(arquivo.read())
print('\n')

# Colocando o cursor em uma posição específica do arquivo. No meu caso, a posição 105 era o início de uma frase que eu quis usar como exemplo.
arquivo.seek(105)
print(arquivo.read())

'''
Para ler uma linha do arquivo de cada vez podemos usar a função readline().
readline() -> Função que lê o arquivo linha a linha (readline -> lê linha)
'''
arquivo.seek(0)
uma_linha = arquivo.readline()

print(type(uma_linha)) # Imprime <class 'str'>. É uma string
print(uma_linha) # Imprime o texto que está na primeira linha do arquivo.
# Criando uma lista das palavras presentes na linha lida acima.
print(uma_linha.split(' '))

'''
Podemos criar uma lista contendo todas as linhas presentes no arquivo com a função readlines()
'''
arquivo.seek(0)
linhas_arquivo = arquivo.readlines()
print(f'O arquivo lido possui {len(linhas_arquivo)} linhas')
print(linhas_arquivo)

'''
OBSERVAÇÃO: Quando abrimos um arquivo com a função open() é criada uma conexão entre o arquivo no disco do computador e o nosso programa. 
Essa conexão é chamada de streaming. Ao finalizar os trabalhos com o arquivo devemos fechar essa conexão. Para isso utilizamos a função close()

Passos para se trabalhar com um arquivo:

1 - Abrir o arquivo;

2 - Trabalhar o arquivo;

3 - Fechar o arquivo;

# 1 - Abrir o arquivo;
arquivo = open('texto.txt')

# 2 - Trabalhar o arquivo;
print(arquivo.read())

print(arquivo.closed)  # False Verifica se o arquivo está aberto ou fechado

# 3 - Fechar o arquivo;
arquivo.close()

'''
# Se o arquivo ainda estiver aberto, ele será fechado.
if not arquivo.closed:
    print('O arquivo está aberto e será fechado')
    arquivo.close()

# OBS: Se tentarmos manipular o arquivo após seu fechamento, teremos um ValueError
# A linha abaixo resulta em erro.
# arquivo.seek(0)

arquivo = open('texto.txt')
# Com a função read() podemos limitar a quantidade de caracteres a serem lidos no arquivo
print(arquivo.read(50))

