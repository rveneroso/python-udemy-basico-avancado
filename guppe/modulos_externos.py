'''
Módulos Externos

A instalação de módulos externos no Python deve ser feita via pip - Python Installer Package

Os pacotes oficiais externos disponíveis para Python encontram-se no site https:pypi.org

colorama é um pacote que permite a impressão de texto em cores variadas
'''

# import pydf
from colorama import init, Fore

init()

print(Fore.MAGENTA + 'Geek University')
print(Fore.BLUE + 'Geek University')
'''
Não fiz a execução desse código pois não instalei o pacote pydf.
pdf = pydf.generate_pdf('<h1>Geek University</h1><br/><br/><strong>Programa&ccedil;&atilde;o em Python: Essencial</strong>')

with open('test_doc.pdf', 'wb') as f:
    f.write(pdf)
'''

