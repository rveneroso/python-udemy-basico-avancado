"""
Sistema de Arquivos - Manipulação
"""

import os
# Verificando se um arquivo ou diretório já existe
# Arquivo
print(os.path.exists('arquivo.txt'))  # False
print(os.path.exists('frutas.txt'))  # True

# Diretório
# Utilizanod paths relativos
print(os.path.exists('geek'))  # True
print(os.path.exists('geek/university'))  # True
print(os.path.exists('geek/university/../geek3.py'))  # False
print(os.path.exists('outro'))  # False

# Utilizando paths absolutos
print(os.path.exists('/home/geek/university'))  # False
print(os.path.exists('/home/geek/Imagens'))  # True
print(os.path.exists('/home/geek/Imagens/wallpaler2.png'))  # True

# Criando arquivos

# Forma 1
open('arquivo-teste.txt', 'w').close()

# Forma 2
open('arquivo-teste2.txt', 'a').close()

# Forma 3
with open('arquivo-teste3.txt', 'w') as arquivo:
    pass

# Apesar de ser possível criar arquivos com qualquer uma das formas apresentadas acima, a melhor maneira para se fazer isso é com a função
# mknod.
os.mknod('arquivo-teste4.txt')
os.mknod('/home/rveneroso/Downloads/university.txt')

'''
Observações:
1 - Para usuários de Mac OS, pode haver um erro de PermissionError
2 - Ao se criar um arquivo via mknod(), se o arquivo já existir teremos o erro FileExistsError
'''
# Criando diretórios - únicos (um a um)
# UtiliandopPath Relativo
os.mkdir('templates')

# Utilizando path Absoluto
os.mkdir('/home/geek/templates')

# A função mkdir() cria um diretório se este não existir. Caso exista, teremos FileExistsError

# Se não tivermos permissão para criar o diretório teremos um PermissionError
os.mkdir('/etc/templates')


# Criando múltiplos diretórios com um único comando
os.makedirs('templates/geek/university/outro')

# Se o diretório a ser criado já existe, um FileExistsError será levantado. Porém, o parâmetro exist_ok=True evita que o erro seja levantado.
os.makedirs('templates2/novo2/outro2', exist_ok=True)

# Diretórios
os.rename('geek2/novo2', 'geek2')

'''
Observações:

1 - Se o diretório não existir teremos um FileNotFoundError
2 -Se e diretório que queremos renomear não estiver vazio, teremos um OSError
'''

# Renomear arquivos e diretórios
# Arquivos
# Importante: ao renomear um arquivo é preciso informar o caminho completo do arquivo nos dois parâmetros.
os.rename('geek2/novo2/outro2/teste.txt', 'geek2/novo2/outro2/geek.txt')
os.rename('frutas.txt', 'cesta1.txt')

'''
ATENÇÃO! Tome cuidado com os comandos de deleção. Ao deletarmos um arquivo ou diretório, eles não vão para a lixeira. Eles somem.
'''
# Removendo arquivos
os.remove('geek.txt')

'''
Observações:

1 - Se você estiver no Windows e o arquivo que você for deletar estiver em uso, você terá um erro.
2 - Caso o arquivo não exista, teremos o FileNotFoundError
3 - Se for informado um diretório ao invés de um arquivo, teremos um IsADirectoryError
'''

# Removendo diretórios vazios
os.rmdir('templates')

'''
Observações:

1 - Se o diretório tiver qualquer conteúdo teremos um OSError
2 - Se o diretório não existir teremos um FileNotFoundError
'''

# Removendo uma árvore de arquivos
for arquivo in os.scandir('geek2'):
    if arquivo.is_file():
        os.remove(arquivo.path)


# Podemos remover uma árvore de diretórios vazios
# Se algum dos diretórios contiver arquivos ou outros diretórios, o processo para.
os.removedirs('geek2/mais')

# sudo apt-get install lsb-core

os.remove('cesta1.txt')  # Não vai para a lixeira. É deletado imediatamente

# ATENÇÃO: Ao remover arquivos e diretórios com Python eles não vão para a lixeira. Eles vão embora!

# Importando a biblioteca send2trash (Envia arquivos e diretórios para a lixeira)
from send2trash import send2trash

# Se o arquivo não existir, teremos OSError
send2trash('cesta2.txt')  # Vai pra lixeira. Pode ser restaurado.
send2trash('teste')

# Trabalhando com arquivos e diretórios temporários
import os
import tempfile

# Criando um diretório temporário
'''
Estamos criando um diretório temporário, abrindo o mesmo e dentro dele criando um arquivo para escrevermos um texto. No final, usamos um input() só para mantermos
os arquivos temporários 'vivos' dentro dos blocos with.
'''
with tempfile.TemporaryDirectory() as tmp:
    print(f'Criei o diretório temporário em {tmp}')
    with open(os.path.join(tmp, 'arquivo_temporario.txt'), 'w') as arquivo:
        arquivo.write('Geek Univesity\n')
    input()

'''
Possivelmente, o código acima não irá funcionar se você estiver utilizando o Windows. Por conta desse sistema trabalhar de forma diferente com arquivos
temporários.
'''

'''
Criando apenas um arquivo temporário (sem criar o diretório temporário).
IMPORTANTE: Em arquivos temporários só conseguimos escrever bits. Por isso, utilizamos b''
'''
with tempfile.TemporaryFile() as tmp:
    tmp.write(b'Geek University\n')
    tmp.seek(0)
    print(tmp.read())

# Criando um arquivo temporário sem o uso do bloco with
arquivo = tempfile.TemporaryFile()
arquivo.write(b'Geek University\n')
arquivo.seek(0)
print(arquivo.read())
arquivo.close()

# Trabalhando com arquivos e diretórios temporários

import os
import tempfile

arquivo = tempfile.NamedTemporaryFile()
arquivo.write(b'Geek University\n')

print(arquivo.name)
print(arquivo.read())
input()
arquivo.close()

# https://docs.python.org/3/library/os.html?highlight=os#module-os



