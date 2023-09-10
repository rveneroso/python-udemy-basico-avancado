"""
Teste de Memória com Generators


# Sequência de Fibonacci
1, 1, 2, 3, 5, 8, 13...

# Teste 1 Lista
for n in fib_lista(100000):
    print(n)

"""
import sys
sys.set_int_max_str_digits(1000000000)

# Função usando listas 449MB.
# Na minha máquina o consumo de memória do Python ficou entre 98 / 99 MB.
def fib_lista(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a + b
    return nums


# Função usando geradores
def fib_gen(max):
    a, b, contador = 0, 1, 0
    while contador < max:
        a, b = b, a + b
        yield a
        contador = contador + 1


# Teste 2 Geradores 3MB
# Na minha máquina o Python ocupou 0.1 MB
for n in fib_gen(100000):
    print(n)
