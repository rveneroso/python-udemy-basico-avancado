"""
Forçando tipos de dados com decoradores

zip

a = (1, 3, 5)
b = (2, 4, 6)

c = zip(a, b)

(1, 2), (3, 4), (5, 6)


"""


def forca_tipo(*tipos):
    def decorador(funcao):
        def converte(*args, **kwargs):
            novo_args = []
            for(valor, tipo) in zip(args, tipos):
                '''
                Recebe os valores e os tipos de dados esperados e os converte de acordo com o que ficou definido.
                Retorna os novos argumentos já convertidos de forma que a função que foi decorada possa realizar
                suas operações com os dados já convertidos.
                '''
                novo_args.append(tipo(valor))  # str('Geek'), int('3')
            return funcao(*novo_args, **kwargs)
        return converte
    return decorador


@forca_tipo(str, int)
def repete_msg(msg, vezes):
    for vez in range(vezes):
        print(msg)


repete_msg('Geek', '3')


@forca_tipo(float, float)
def dividir(a, b):
    print(a/b)


dividir('1', 5)

