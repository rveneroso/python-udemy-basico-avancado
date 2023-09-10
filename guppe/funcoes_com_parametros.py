def quadrado(numero):
    return numero ** 2;

def imprime_nome_completo(nome, sobrenome):
    print(f'Seu nome completo é {nome} {sobrenome}')


# Utilizando argumentos nomeados.
if __name__ == '__main__':
    imprime_nome_completo(sobrenome='Veneroso', nome='Renato')
    print(f'O quadrado de 6 é {quadrado(6)}')

'''
A função abaixo foi criada pelo professor. Em sua forma original, não havia a linha 
    if __name__ == '__main__':
    
Essa linha foi adiciona pelo seguinte motivo: o Python atribui automaticamente o valor __main__ à variável __name___. É isso que permite que um programa Python
seja executado sem a necessidade de se implementar um método main como acontece nas linguagens C e Java.
No caso da função abaixo, ela possui dois comandos print que são automaticamente executados quando outro módulo Python faz um import desse módulo ou apenas da função.
Dessa forma, a linha 
    if __name__ == '__main__':
faz com que as impressões dentro da função somente sejam executadas caso o módulo sendo executado seja o proóprio funcoes_com_parametros

'''
def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total


if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5, 6, 7]
    print(soma_impares(lista))

    tupla = (1, 2, 3, 4, 5, 6, 7)
    print(soma_impares(tupla))
else:
    print(f'O valor __name__ nesse momento é {__name__}')