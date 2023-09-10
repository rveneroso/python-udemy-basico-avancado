import os
'''
Cria o diretório temp. Na primeira execução, o diretório será criado sem problemas pois não existia.
Porém, uma segunda execução do programa resulta no erro FileExistsError: [Errno 17] File exists: 'temp'.
Após essas duas execuções, alterei o comando adicionando o parâmetros exist_ok=True e isso fez com que novas execuções do programa, mesmo com o diretório já 
existindo, fossem executadas sem problemas.

Observação: com exist_ok=True, se o diretório a ser criado já existir, seu conteúdo será preservado. Antes de incluir o parâmetro exist_ok=True, criei um
arquivo dentro do diretório temp. Então, rodei o programa novamente, não ocorreu o FileExistsError e o arquivo previamente criado foi preservado.
Acredito que isso tenha acontecido porque tudo indica que o parâmetro exist_ok=True simplesmente ignora o FileExistsError. Ele não recria o diretório. Daí
o conteúdo do diretório ter sido preservado.
'''
os.makedirs('temp', exist_ok=True)