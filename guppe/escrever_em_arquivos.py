"""
Ao abrir um arquivo para leitura, não podemos realizar a escrita nele. Apenas ler.
Da mesma forma, se abrirmor um arquivo para escrita, não podemos lê-lo, somente escrever nele.

OBS: Ao abrir um arquivo para escrita, o arquivo é criado no sistema operacional.

Para escrevermos dados em um arquivo, após abrir o arquivo utilizamos a função write().
Esta função recebe uma string como parâmetro, caso contrário teremos um TypeError

Abrindo um arquivo para escrita com o modo 'w', se o arquivo não existir será criado,
caso ele já exista, o anterior será apagado e um novo será criado. Dessa forma, todo
o conteúdo no arquivo anterior é perdido.

# Exemplo de escrita - modo 'w' - write (escrita)
"""

# Forma tradicional de escrita em arquivo (Não Pythônica)
arquivo = open('mais.txt', 'w') # O modo w indica que iremos gravar no arquivo.

# Obrigatoriamente, o argumento da função write deve ser uma string
arquivo.write('Um texto qualquer.\n')
arquivo.write('Mais um texto.')

arquivo.close()

# Forma Pythônica
with open('novo.txt', 'w') as arquivo:
    arquivo.write('Novos dados.\n')
    arquivo.write('Outros podemos colocar quantas linhas quisermos.\n')
    arquivo.write('Mais Esta é a última linha.')

# Esse é o bloco da ignorância. Foi criado apenas para gerar um arquivo gigantesco como teste.
with open('arquivo_da_ignorancia.txt','w') as arquivo_da_ignorancia:
    for linha in range(0,800000):
        arquivo_da_ignorancia.write(f'Eu sou a linha de número {linha} no arquivo!\n')
    arquivo.close()

with open('geek.txt', 'w') as arquivo:
    arquivo.write('Geek ' * 1000)

with open('frutas.txt', 'w') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou digite sair: ')
        if fruta != 'sair':
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break



