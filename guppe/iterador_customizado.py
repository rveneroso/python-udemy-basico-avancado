'''
Escrevendo um iterador customizado
'''

class Contador:
    def __init__(self, menor, maior):
        self.menor = menor
        self.maior = maior

    def __iter__(self):
        return self

    def __next__(self):
        if self.menor < self.maior:
            numero = self.menor
            self.menor = self.menor + 1
            return numero
        raise StopIteration

# Cria um novo objeto do tipo Contador com menor = 1, maior = 61
con = Contador(1,61)

# Cria um Iterator a partir da execução da função iter() passando como parâmetro o objeto con. Isso só funciona porque a classe Contador implementa
# o método __iter__
iterator = iter(con)

# Executa a primeira iteração sobre o Iterator criado acima executando a função next() passando como parâmetro o Iterator criado na etapa anterior.
print(next(iterator))

# Executa sucessivas iterações sobre o Iterator através de várias chamadas next()
print(next(iterator))
print(next(iterator))
print(next(iterator))

# Como a classe Contador implementa os métodos __iter__ e __next___, podemos aplicar um loop diretamente sobre um objeto dessa classe.
print('Iniciando for baseado na classe Contador')
for n in Contador(1, 61):
    print(n)

print('\nIniciando for baseado em range')
# O for abaixo dará o mesmo resultado do for executado com base na classe Contador. Isso mostra que a implementação dos métodos __iter__ e __next__
# foi feita corretamente.
for n in range(1, 61):
    print(n)
