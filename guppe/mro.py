"""
POO - MRO - Method Resolution Order

Method Resolution Order (Resolução de Ordem de Métodos), é a ordem
de execução dos métodos (quem será executado primeiro).

Em Python, a gente pode conferir a ordem de execução dos métodos (MRO) de 3 formas:
    - Via propriedade da classe __mro__
    - Via método mro()
    - Via help
"""

'''
Saída do comando Pinguim.__mro__

>>> Pinguim.__mro__
(<class 'mro.Pinguim'>, <class 'mro.Aquatico'>, <class 'mro.Terrestre'>, <class 'mro.Animal'>, <class 'object'>)

Aqui podemos ver a sequência de execução dos métodos: aqueles definidos na pŕopria classe, os da classe Aquatico, os da 
classe Terrestre, os da classe Animal e, por fim, os da classe object.

Saída do comando Pinguim.mro()

>>> Pinguim.mro()
[<class 'mro.Pinguim'>, <class 'mro.Aquatico'>, <class 'mro.Terrestre'>, <class 'mro.Animal'>, <class 'object'>]

Saída parcial do comando help(Pinguim)

class Pinguim(Aquatico, Terrestre)
 |  Pinguim(nome)
 |  
 |  Method resolution order:
 |      Pinguim
 |      Aquatico
 |      Terrestre
 |      Animal
 |      builtins.object
 |  
 |  Methods defined here:
 |  
 |  __init__(self, nome)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Methods inherited from Aquatico:
 |  
 |  nadar(self)
 |  
 |  ----------------------------------------------------------------------
:


'''


class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        return f'Eu sou {self.__nome}'


class Aquatico(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self._Animal__nome} está nadando.'


class Terrestre(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{self._Animal__nome} está andando.'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} da terra!'


class Pinguim(Aquatico, Terrestre):

    def __init__(self, nome):
        super().__init__(nome)


# Testando

tux = Pinguim('Tux')
print(tux.cumprimentar())

"""
Pinguim(Aquatico, Terrestre)
Eu sou Tux do mar!

Pinguim(Terrestre, Aquatico)
Eu sou Tux da terra!
"""
