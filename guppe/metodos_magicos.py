"""
POO - Métodos Mágicos

Métodos Mágicos, são todos os métodos que utilizam dunder.

# dunder init -> __init__()
def __init__(self, titulo, autor, paginas):
    self.titulo = titulo
    self.autor = autor
    self.paginas = paginas

Dunder > Double Underscore

# dunder repr -> Representação do objeto
def __repr__(self):
    return f'{self.titulo} escrito por {self.autor}'
"""


class Livro:

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    '''
    Os métodos __repr__ e __str__ são semelhantes. Se for feita a impressão do objeto com print(objeto), Porém, __repr__ tem precedência sobre __str__. Se __repr__ existir em uma classe, ele será utilizado para
    representar uma instância daquela classe. Caso não exista mas o método __str__ exista, então __str__ será usado.
    Esses dois métodos são semelhantes ao toString() do Java.
    '''
    def __repr__(self):
        return f'{self.titulo} escrito por {self.autor}'

    def __str__(self):
        return self.titulo

    '''
    Sobreescrevendo o método __len__ que fornece informações sobre o tamanho do objeto.
    '''
    def __len__(self):
        return self.paginas

    '''
    Sobreescrevendo o comportamento do método __del__
    '''
    def __del__(self):
        print('Um objeto do tipo Livro foi deletado da memória')

    def __add__(self, outro):
        return f'{self} - {outro}'

    def __mul__(self, outro):
        if isinstance(outro, int):
            msg = ''
            for n in range(outro):
                msg += ' ' + str(self)
            return msg
        return 'Não posso multiplicar'


livro1 = Livro('Python Rocks!', 'Geek University', 400)
livro2 = Livro('Inteligência Artificial com Python', 'Geek University', 350)

print(livro1)

print(livro2)

print(len(livro1))
print(len(livro2))

print(livro1 + livro2)

print(livro1 * 5)
