'''
*args é a forma de se passar mais de um argumentos a uma função sem declará-los explicitamente.
Com *args, podem ser passados quantos argumentos se queira.
'''
def soma_varios_numeros(*args):
    # IMPORTANTE: na definição da função escrevemos *args mas ao referenciarmos a variável usamos apenas args
    soma = 0
    # A variável args é uma tupla. Abaixo temos a soma no método lusitano feito por mim.
    # for numero in args:
    #     soma = soma + numero
    # return soma
    # Abaixo o método inteligente feito pelo professor.
    return sum(args)

print(soma_varios_numeros(1, 2, 3, 4, 5))

# O parâmetro args não precisa ser o único parâmetro de uma função. Ele pode ser combinado com outros
# parâmetros e esses, por sua vez, podem ser obrigatórios ou opcionais.

# Python oferece ainda um recurso valioso para se trabalhar com *args.
# Por ser do tipo tuple, se passarmos qualquer outra coleção para a função que tem *args como
# parâmetro, teríamos um typeerror.
# A linha abaixo define uma lista
numeros = [ 1, 2, 3, 4, 6, 7]

# Ao chamar a função soma_varios_numeros passando a lista 'numeros', temos um typeerror
# print(soma_varios_numeros(numeros)) # TypeError: unsupported operand type(s) for +: 'int' and 'list'

# Porém, se passarmos a variável números para a função precedido de um asterisco, indicamos ao Python
# que a função está recebendo uma coleção qualquer e que ele deve fazer a conversão automaticamente e
# de forma implícita.
print(soma_varios_numeros(*numeros)) # Teremos o resultado esperado: 23

# Essa solução atende também a variáveis do tipo set
outros_numeros = {9, 8, 7, 6, 5}
print(soma_varios_numeros(*outros_numeros)) # Teremos o resultado esperado: 35