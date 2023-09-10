"""
Doctests

Doctests são testes que colocamos na docstring das funções/métodos Python.
"""

# Doctests têm uma grande desvantagem: eles precisam ser escritos como se o desenvolvedor estivesse digitando diretamente
# no prompt da console do Python. Por isso, no exemplo abaixo a linha soma(1, 2) está precedida por >>>
def soma(a, b):
    """
    soma os números a e b

    >>> soma(1, 2)
    3

    >>> soma(4, 6)
    10
    """
    return a + b
    
print(soma(3,4))

"""
Para rodar um test do doctest:

python -m doctest -v nome_do_mobulo.py

As linhas abaixo mostram a saída da execução do comando acima.

Trying:
    soma(1, 2)
Expecting:
    3
ok
1 items had no tests:
    doctests
1 items passed all tests:
   1 tests in doctests.soma
1 tests in 2 items.
1 passed and 0 failed.
Test passed.
"""
# Outro Exemplo, Aplicando o TDD

def duplicar(valores):

    """
    Duplica os valores em uma lista

    >>> duplicar([1, 2, 3, 4])
    [2, 4, 6, 8]

    >>> duplicar([])
    []

    >>> duplicar(['a', 'b', 'c'])
    ['aa', 'bb', 'cc']

    >>> duplicar([True, None])
    Traceback (most recent call last):
       ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'

    # Sem a implementação da linha abaixo, todos os testes irão falhar. Esse é exatamente o conceito de TDD: os
    # testes são escritos antes da implementação.
    # Com a implementação da linha abaixo, todos os testes passam.
    """
    return [2 * elemento for elemento in valores]

"""
IMPORTANTE: ao realizar testes baseados em retornos de String dentro de doctests, é preciso ficar atento ao uso de aspas
duplas e simples. Doctests são escritos dentro de aspas triplas e por isso, ao se escrever resultados esperados, é preciso
colocar os resultados entre aspas simples,
"""
def fala_oi():
    """
    Fala oi

    >>> fala_oi()
    'oi'

    """
    return "oi"