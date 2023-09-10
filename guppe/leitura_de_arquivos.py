# A forma mais simples de se abrir um arquivo somente leitura em Python é a que se segue.
arquivo = open('texto.txt')

print(arquivo) # <_io.TextIOWrapper name='texto.txt' mode='r' encoding='UTF-8'>
print(type(arquivo)) # <class '_io.TextIOWrapper'>

# Para ler o conteúdo de um arquivo já aberto
print(arquivo.read())
print('Essa linha não faz parte do arquivo lido.')
'''
IMPORTANTE: O Python utiliza um recurso para trabalhar com arquivos chamado cursor. Esse cursor, funciona como o cursor quando estamos escrevendo.
Isso quer que dizer que, após a leitura completa do conteúdo de um arquivo, seja com a função read() ou através de outro recurso, ao se realizar uma segunda leitura,
nada será retornado pois a leitura anterior foi até o fim do arquivo.
'''
print('Linha anterior à segunda chamada da função read()')
print(arquivo.read())
print('Linha posterior à segunda chamada da função read()')

