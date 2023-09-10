"""
POO - O método super()

O método super() se refere á super classe.


"""


class Animal:

    def __init__(self, nome, especie):
        self.__nome = nome
        self.__especie = especie

    def faz_som(self, som):
        print(f'O {self.__nome} fala {som}')


class Gato(Animal):

    def __init__(self, nome, especie, raca):
        # Animal.__init__(self, nome, especie)
        '''
        Quando se utiliza super() não há a necessidade de passar a ele o objeto self. Se utilizarmos o nome da super classe, então é necessário passar
        ao __init__ o objeto self.
        '''
        super().__init__(nome, especie)
        '''
        Com o super() não ficamos restritos a acessar o método __init__. Qualquer método da super classe pode ser chamado, conforme mostra o exemplo abaixo.
        '''
        super().faz_som('auauauaua')
        self.__raca = raca


felix = Gato('Felix', 'Felino', 'Angorá')

felix.faz_som('miau')

