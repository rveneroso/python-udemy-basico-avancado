def divide_dois_numeros(numerador, denominador):
    return (numerador / denominador)

# Exemplo que não utiliza loop apenas para fins didáticos
# numerador = input("Informe o numerador: ")
# denominador = input('Informe o denominador: ')
#
# try:
#     numerador = int(numerador)
#     denominador = int(denominador)
# except ValueError:
#     print('Somente são aceitos números')
# else:
#     try:
#         res = numerador / denominador
#     except ZeroDivisionError:
#         print('O denominador informado não pode ser zero.')
#     else:
#         print(f'O resultado da divisão de {numerador} por {denominador} é {divide_dois_numeros(numerador, denominador)}')
# finally:
#     print('Esse linha será impressa independente das condições anteriores')

#
# O mesmo código acima porém refatorado
def div(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Valor não numérico'
    except ZeroDivisionError:
        return 'Não é possível fazer divisão por zero'

def div2(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Não foi possível realizar a divisão: {err}.'

num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')
print(div2(num1, num2))