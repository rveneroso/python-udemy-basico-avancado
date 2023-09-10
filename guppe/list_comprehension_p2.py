'''
Com List comprehension é possível adicionar elementos à nova lista de maneira condicional. Em outras
palavras: o elemento do iterável só será adicionado à lista final caso atenda a uma determinada condição.

'''
pares = [numero for numero in range(1,1001) if numero % 2 == 0]
print(pares)
impares = [numero for numero in range(1,1001) if numero % 2 != 0]
print(impares)
'''
É possível adicionar condicionais mais complexas. Aqui cabe observar que a condição saiu do
fim da expressão e veio para o início.
Na linha abaixo, números pares serão adicionados sem alterações à lista final. Já os números
ímpares serão divididos por 3 antes de serem adicionados à lista.
'''
res = [numero if numero % 2 == 0 else numero / 3 for numero in range(1,1001) ]
print(res)