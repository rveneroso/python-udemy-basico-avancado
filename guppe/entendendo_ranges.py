# O valor inicial do range, por não ter sido informado, será 0.
# Então serão impressos os números de 0 a 10 (o segundo parâmetro não é inclusivo)
for numero in range(11):
    print(numero, end="")
print("\n")

# Se for informado um valor inicial, a iteração terá início nesse valor.
# Irá imprimir os números de 5 a 10.
for numero in range(5, 11):
    print(numero, end="")
print("\n")

# Caso se deseje especificar o step na iteração, ele deve ser informado como terceiro parâmetro.
# Serão impressos os números de 1 a 9
for numero in range(1,10,2):
    print(numero, end="")
print("\n")

# Imprimindo os números de 10 a 2 (ordem decrescente)
for numero in range(10,1,-2):
    print(numero, end="")