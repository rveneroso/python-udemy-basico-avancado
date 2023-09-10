"""
Decoradores (Decorators)

O que são decorators?

- Decorators são funções;
- Decorators envolvem outras funções e aprimoram seus comportamentos;
- Decorators também são exemplos de Higher Order Functions;
- Decorators tem uma sintaxe própria, usando "@" (Syntact Sugar / Açúcar Sintático)



|----------------------------------------|
|      Function Decorator                |
------------------------------------------


---------------------------------------------
| |---------------------------------------| |
| |        Função decorada                | |
| |---------------------------------------- |
| ------------------------------------------
"""

# Decorators como funções (Sintaxe não recomendada / Sem Açúcar Sintático)

'''
IMPORTANTE: Decorator Function é a função que recebe como parâmetro uma outra função e altera o comportamento da função recebida.
            Decorator é basicamente a anotação do tipo @seja_educado_mesmo
'''
def seja_educado(funcao):
    def sendo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um ótimo dia!')
        '''
        IMPORTANTE: observar que o que está sendo retornado na linha de baixo é a função interna sendo() e não o resultado da execução da função
        interna sendo().
        '''
    return sendo


def saudacao():
    print('Seja bem-vindo(a) à Geek University')


# Testando 1

# saudacao()

'''
A linha abaixo chama a função decorator seja_educado() e passa como argumento a função saudacao. Passa a função em si e não a execução da função.
O resultado é capturado na variável teste que, como recebe uma função, deve ser executada posteriormente.
'''
teste = seja_educado(saudacao)

# Executa a variável teste pois ela contém uma função.
teste()


# Testando 2


def raiva():
    print('EU TE ODEIO!')


raiva_educada = seja_educado(raiva)

raiva_educada()

# Decorators com Syntax Sugar (Açúcar Sintático)

def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um excelente dia!')
    return sendo_mesmo

'''
A função abaixo está codificada da maneira correta em se tratando de decorators.
Pelo fato de ter sido anotada com @seja_educado_mesmo, quando a função apresentando for executada, ela será automaticamente passada como
argumento para a função seja_educado_mesmo. Não há a necessidade de fazer uma chamada explícita à função seja_educado_mesmo passando a
função apresentando como argumento. Isso é feito de maneira implícita devido à anotação @seja_educado_mesmo.
O comportamento será o mesmo daquele de funções decorators com chamadas explícitas.
'''
@seja_educado_mesmo
def apresentando():
    print('Meu nome é Pedro')


# Testando

apresentando()


@seja_educado_mesmo
def dormir():
    print('Quero dormir...')


dormir()


"""
|-------------------------------------------------------
|  Home    |  Serviços   | Produtos   | Administrativo |
--------------------------------------------------------

http://www.suaempresa.com.br/home

http://www.suaempresa.com.br/servicos

http://www.suaempresa.com.br/produtos

http://www.suaempresa.com.br/admin
"""

'''
# OBS: Não é código funcional (Que funcione) é apenas exemplo

def checa_login():
    if not request.usuario:
        redirect('http://www.suaempresa.com.br/login')


def home(request):
    return 'Pode acessar home'

@checa_login
def servicos(request):
    return 'Pode acessar serviços'


def produtos(request):
    return 'Pode acessar produtos'


@checa_login
def admin(request):
    return 'Pode acessar admin'

# OBS: Não confunda Decorator com Decorator Function
'''

