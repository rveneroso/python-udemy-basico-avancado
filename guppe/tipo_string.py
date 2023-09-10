# Em Python caracteres de mudança de linha podem ser inseridos no meio de strings.
nome = 'Angeline \nJolie'
print(nome)

# No caso da quebra de linha ser inserida manualmente, quando a string está declarada entre aspas simples,
# é preciso colocá-la entre parênteses para que o compilador aceite.
nome2 = ('Ivan'
         'Piro')
print(nome2)

# Isso não é necessário caso a string seja definida entre triplas aspas simples ou duplas.
nome3 = '''Karl
Bartos'''
print(nome3)

nome4 = """Ralf
Hutter"""
print(nome4)

# Para quebrar uma string em uma lista de elementos.
frase = 'A vingança nunca é plena, mata a alma e a envenena'
print(frase.split())

# Assim como em Java, é possível definir o delimitador a ser utilizado no split.
frase = 'A-vingança-nunca-é-plena,-mata-a-alma-e-a-envenena'
resultado = frase.split('-')
print(resultado)
print(type(resultado))

# O que o Python faz ao criar uma string é criar um array onde cada posição é um caracter da string
# Por isso, é possível acessar posições específidas da string informando as posições do vetor
# que se deseja acessar. Assim como o substring de Java, o segundo índice nesse tipo de pesquisa
# não entra no resultado.
marca = 'Mercedes Benz'
print(marca[0:5]) # Imprime Merce

# Caso o segundo índice seja omitido será retornada a string até o seu fim.
print(marca[9:]) # Imprime Benz

# Para imprimir uma string invertida
print(marca[:: -1])

# Em Python, o comando replace por padrão já substitui TODAS as ocorrências de um caracter por outro.
print(marca.replace('e','i')) # Imprime Mircidis Binz