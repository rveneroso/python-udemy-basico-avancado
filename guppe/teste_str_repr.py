class CompactDisc:

    def __init__(self, titulo, artista):
        self.titulo = titulo
        self.artista = artista

    def  __repr__(self):
        return f'Sou uma representação do CD {self.titulo} composto por {self.artista}'

    def __str__(self):
        return f'Sou o toString() do CD {self.titulo} composto por {self.artista}'

cd = CompactDisc('Rambo First Blood','Jerry Goldsmith')

# Com o comando abaixa será usado o método __str__ para imprimir informações sobre o objeto.
print(cd)

# Para imprimir somente a representação do objeto é necessário fazer a chamada explícita ao método__repr__
print(repr(cd))