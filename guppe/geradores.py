"""
Geradores

- Geradores (Generators) são Iterators (Iteradores);

OBS: O contraŕio não é verdadeiro. Ou seja, nem todo iterator é um generator.

Outras informações:
- Generators podem ser criados com funções geradoras;
- Funções geradoras utilizam a palavra reservada yield;
- Generators podem ser criados com Expressões Geradoras;

Diferenças entre Funções e Generator Functions (Funções Geradoras)

-----------------------------------------------------------------------------------
| Funções                                 | Generator Functions                   |
-----------------------------------------------------------------------------------
| utilizam return                         | utilizam yield                        |
-----------------------------------------------------------------------------------
| retorna uma vez                         | podem utilizar yield múltiplas vezes  |
-----------------------------------------------------------------------------------
| quando executada, retorna um valor      | quanto executada, retorna um generator|
-----------------------------------------------------------------------------------
"""

'''
Exemplo Função Geradora (Generator Function)
Observação: uma Generator Function não é um Generator. Ela produz um generator.
'''
def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        '''
        yield funciona como return das funções convencionais. A diferença é que o return encerra a execução da função. O yield retorna um valor mas continua
        aguardando uma próxima chamada válida de next().
        '''
        yield contador
        contador = contador + 1



gen = conta_ate(5)

print(type(gen)) # Imprime <class 'generator'> já que a função conta_ate produz um Generator.

for num in gen:
    print(num)

'''
As chamadas next() abaixo estão comentadas porque, se executadas (qualquer uma delas), causam um StopIteration visto que o comando for acima esgotou todas as chamadas
next() válidas no objeto gen.
'''
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# print(next(gen))
#
# print(next(gen))  # 1

print('Geek')




for num in gen:
    print(num)



gen = list(conta_ate(10))

print(gen)
