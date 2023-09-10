"""
Decorators com diferentes assinaturas
"""
# Relembrando


def gritar(funcao):
    def aumentar(nome):
        """
        IMPORTANTE: no comando return abaixo o que será retornado é o resultado da execução de funcao(nome) convertido para letras maiúsculas.
        Se a função gritar for chamada pela função saudacao('Angelina'), então o comando return abaixo retornará OLÁ, EU SOU O/A ANGELINA
        """
        return funcao(nome).upper()
    return aumentar


@gritar
def saudacao(nome):
    return f'Olá, eu sou o/a {nome}'


@gritar
def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal}, acompanhado de {acompanhamento}, por favor.'

# Testando


print(saudacao('Angelina')) # Como mencionado acima, será impresso OLÁ, EU SOU O/A ANGELINA

'''
Na forma original da função gritar, a linha abaixo resultará em erro já que a função gritar somente aceita um parâmetro mas a função
ordenar passa dois argumentos.
'''
# print(ordenar('Picanha', 'Batata Frita'))

'''
Para resolver, utilizamos um padrão de projeto chamado Decorator Pattern
A assinatura de uma função é representada pelo seu retorno, nome e parâmetros de entrada.
Refatorando com a Decorator Pattern

'''
def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar


@gritar
def saudacao(nome):
    return f'Olá, eu sou o/a {nome}'


@gritar
def ordernar(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal} acompanhado de {acompanhamento}, por favor.'


print(saudacao('Felicity'))

print(ordernar('Picanha', 'Batata Frita'))


@gritar
def lol():
    return 'lol'


print(lol())


# OBS: Vale lembrar que podemos utilizar parâmetros nomeados

print(ordernar(acompanhamento='Batata Frita', principal='Picanha'))

# Decorator com argumentos

'''
Na definição da função abaixo está indicando que, qualquer função que venha a chamá-la deve passar o argumento valor.
'''
def verifica_primeiro_argumento(valor):
    def interna(funcao):
        '''
        A função interna outra recebe nenhum, um ou vários parâmetros.
        '''
        def outra(*args, **kwargs):
            '''
            Como uma função interna consegue ter acesso à variáveis declaradas em funções externas, aqui a variável valor (recebida por verifica_primeiro_argumento)
            pode ser acessada. Então a linha abaixo checa se foram passados argumentos a ela (à função outra) e, se sim, se o valor do primeiro argumento é aquele
            mesmo que foi informado no argumento passado à função verifica_primeiro_argumento. Caso não seja, uma mensagem será retornada.
            '''
            if args and args[0] != valor:
                return f'Valor incorreto! Primeiro argumento precisa ser {valor}'
            return funcao(*args, **kwargs)
        return outra
    return interna


'''
Decora a função comida_favorita com a função verifica_primeiro_argumento e define que o valor do primeiro argumento deve ser pizza.
'''
@verifica_primeiro_argumento('pizza')
def comida_favorita(*args):
    print(args)

'''
Decora a função soma_dez com a função verifica_primeiro_argumento e define que o valor do primeiro argumento deve ser 10.
'''
@verifica_primeiro_argumento(10)
def soma_dez(num1, num2):
    return num1 + num2


# Testando

print(soma_dez(10, 12))  # 22
print(soma_dez(1, 21))  # Retorna mensagem informando que o primeiro argumento deve ser o número 10

print(comida_favorita('pizza', 'churrasco'))
print(comida_favorita('sanduiche', 'pizza')) # Retorna mensagem informando que o primeiro argumento deve ser pizza
