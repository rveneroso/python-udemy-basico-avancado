'''
List comprehension é uma maneira de se gerar listas a partir do processamento de elementos existentes
em qualquer iterável.

'''
# List comprehension utiliza a sintaxe [dado for elemento in iteravel]
def multiplica_por_dez(numero):
    return numero * 10

numeros = [1, 2, 3, 4, 5, 6]
vezes_dez = [numero * 10 for numero in numeros]
print(vezes_dez)

vezes_dez2 = [multiplica_por_dez(numero) for numero in numeros]
print(vezes_dez2)

