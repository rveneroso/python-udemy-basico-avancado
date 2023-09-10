# def cumprimentar(nome: str) -> str:
#     return f'Olá, {nome}'
#
#
# print(cumprimentar('Geek'))


def cabecalho(texto: str, alinhamento: bool = True) -> str:
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f" {texto.title()} ".center(50, '#')


print(cabecalho('geek university'))

print(cabecalho('geek university', alinhamento=False))

'''
IMPORTANTE: apesar de Python oferecer o recurso de type hinting, nada impede que os tipos de variáveis sejam violados
no programa. Na linha abaixo o valor 'geek' é passado à função cabecalho no argumento que espera um boolean. Apesar disso,
a função foi executada normalmente e recebeu o argumento alinhamento como se fosse true visto que uma String preenchida
é considerada como True quando utilizada como um boolean.
'''
print(cabecalho('Passei geek no parâmetro alinhamento', alinhamento='geek'))

print(cabecalho('Passei None no parâmetro alinhamento', alinhamento=None))
