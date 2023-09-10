'''
Raise é usado para lançarmos exceções.
Vale lembrar que, uma vez que raise é executado, o fluxo de execução é interrompido
'''
def divide_dois_numeros(numerador, denominador):
    if(type(numerador) is not int):
        raise TypeError('O numerador informado não é um número')
    if(type(denominador) is not int):
        raise TypeError('O denominador informado não é um número')
    if(denominador==0):
        raise ValueError('O denominador não pode ser zero')
    return (numerador / denominador)

a = divide_dois_numeros(1,2)
print(a)
# a = divide_dois_numeros('a',4)
# print(a)
# a = divide_dois_numeros(6,'b')
# print(a)
# a = divide_dois_numeros(5,0)
# print(a)
