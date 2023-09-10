'''
Funções lambda são funções que não tem nome, são funções anônimas
'''
# Definindo uma função simples de maneira tradicional
def funcao(x):
    return x * 3 + 1

print(funcao(4))
print(funcao(7))

# Criando uma lambda que executa o mesmo processamento da função acima.
lambda x: x * 3 + 1
'''
Da maneira como a função lambda foi criada acima, não há como utilizá-la. Ela não tem nome, portanto
não há como fazer uma chamada a ela.
Uma forma de se utilizar essa função seria como na linha abaixo.
'''
calc = lambda x: x * 3 + 1
print(calc(8)) # Imprime 25

# Expressões lambda podem receber mais de um parâmetro
nome_completo = lambda nome,sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()
print(nome_completo('renato','Veneroso'))

'''
A linha abaixo não imprime o resultado da execução da expressão lambda. Ela imprime informações
sobre o tipo do objeto que, no caso, é um lambda
'''
print(lambda: 'Declarei o lambda dentro do print') # Imprime <function <lambda> at 0x7fac32b762a0>
algo = lambda: 'Declarei o lambda dentro do print'
print(algo())

autores = ['Isaac Asimov', 'Ray Bradbury', 'Robert Heinlein', 'Arthur C. Clarke', 'Frank Herbert', 'Orson Scott Card',
           'Douglas Adams', 'H. G. Wells', 'Leigh Brackett']

print(autores)
'''
Na expressão lambda abaixo, cada valor da lista autores será passado à expressão lambda. A expressão
pode receber esse valor com qualquer nome. Na aula o professor chamou de 'sobrenome'. Eu mudei para 'etwas'
para ter certeza de que havia compreendido o que estava acontecendo.
'''
autores.sort(key=lambda etwas: etwas.split(' ')[-1].lower())
print(autores)

# Definindo a função quadrática
def geradora_funcao_quadratica(a, b, c):
    """Retorna a função f(x) = a*x**2 + b * x + c"""
    return lambda x: a * x ** 2 + b * x + c
'''
É importante observar o funcionamento da expressão lambda utilizada aqui.
A função geradora_funcao_quadratica propriamente dita, não recebe x como um de seus parâmetros.
Ela recebe apenas a, b e c.
Por essa razão a variável 'teste' criada abaixo funciona como uma chamada à função geradora_funcao_quadratica
passando os argumentos 2, 3 e -5.
Nas linhas subsequentes, onde temos 3 chamadas à 'variável' teste é que efetivamente passamos o valor de x
a ser utilizado na função lambda.
Assim, quando executamos print(teste(0)), chegarão à função geradora_funcao_quadratica os seguintes
valores:
    a = 2
    b = 3
    c = -5
    x = 0
Quando executamos print(teste(1)), os valores serão:
    a = 2
    b = 3
    c = -5
    x = 1
E quando executamos print(teste(2)), os valores serão:
    a = 2
    b = 3
    c = -5
    x = 2
A variável teste foi criada com os valores a=2, b=3 e c=-5 então não importa qual seja o valor de x,
os valores de a, b e c serão sempre os mesmos em diferentes chamadas. Somente o valor de x é que irá
variar. Assim, os resultados das 3 chamadas à 'variável' teste serão: -5, 0 e 9.
'''
teste = geradora_funcao_quadratica(2, 3, -5)
print(teste(0))
print(teste(1))
print(teste(2))
'''
Podemos perfeitamente chamar a função geradora_funcao_quadratica sem atribui-la à nenhuma variável.
A linha abaixo faz exatamente isso.
'''
print(geradora_funcao_quadratica(8, 2,7)(2))

