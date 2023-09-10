# Nessa função, o parâmetro pontencia assume o valor 2 caso não seja informado. Isso faz com que
# esse parâmetro passe a ser opcional.

'''
IMPORTANTE: os parâmetros que recebem valores default devem estar sempre no fim da lista de parâmetros da
função.

1 - Declaração válida: def exponencial(numero, potencia=2)
2 - Declaração inválida: def exponencial(potencia=2, numero)
'''
def exponencial(numero, potencia=2):
    return numero ** potencia

print(exponencial(2,3)) # Resulta em 8
print(exponencial(5,5)) # Resulta em 3125
print(exponencial(8)) # Resulta em 64

def mostra_informacao(nome='Geek',instrutor=False):
    if nome=='Geek' and instrutor:
        return 'Olá instrutor. Seja bem vindo'
    elif nome=='Geek':
         return 'Eu pensei que você fosse instrutor'
    return f'Olá {nome}'

print(mostra_informacao())
# Na chamada abaixo o valor True não poderia ser passado diretamente. Ele tem que ser precedido pelo
# nome do parâmetro para que a função saiba a qual parâmetro atribuir o valor True.
print(mostra_informacao(instrutor=True))
# Como o valor True foi informado sem a referência ao nome do parâmetro, a saída da linha abaixo
# será Olá True
print(mostra_informacao(True))
print(mostra_informacao('Ozzy'))

# Python permite a execução de uma função da seguinte maneira:
def diz_oi():
    print('Oi')

variavel = diz_oi
variavel()

def soma(num1, num2):
    return num1 + num2
# Aqui o nome da função a ser executada por default será soma.
def mat(num1, num2, funcao=soma):
    return funcao(num1,num2)

def subtracao(num1, num2):
    return num1 - num2

print(mat(2,3))
# Faz uma chamada à mat informando que a função a ser executada é a subtracao.
print(mat(2,2, subtracao))

total = 0
def soma_total():
    # A linha abaixo resulta em erro pois o Python não sabe que estamos referenciando a variável global total.
    # Com isso, ele espera que a variável local total tenha sido inicializada, coisa que não foi feita.
    # total = total + 1

    # Para resolver o problema basta declarar que queremos utilizar a variável global total
    global total
    total = total + 1
    return total

print(soma_total())
print(soma_total())
print(soma_total())
print(soma_total())

def fora():
    contador = 0
    def dentro():
        '''
        O modificador nonlocal abaixo informa que a variável a ser usada não é declarada localmente.
        Fiz um teste comentando a variável declarada dentro da função fora() e criei a variável
        contador com escopo local. Não funcionou. O Python reclamou que não havia nenhuma variável
        para a qual se poderia aplicar o modificador nonlocal.
        Então, pelo o que entendi, o nonlocal serve para indicar que a variável referenciada não é
        declarada dentro do escopo atual, existe em algum escopo visível, mas não é uma variável global.
        '''
        nonlocal contador
        contador = contador + 1
        return contador
    return dentro()

print(f'Resultado da execução da função fora() {fora()}')
