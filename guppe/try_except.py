def divide_dois_numeros(numerador, denominador):
    return (numerador / denominador)

numerador = ''
while numerador != 'sair':
    numerador = input("Informe o numerador ou digite 'sair' para encerrar: ")
    if numerador =='sair':
        break
    denominador = input('Informe o denominador: ')
    try:
        numerador = int(numerador)
        denominador = int(denominador)
        print(f'O resultado da divisão de {numerador} por {denominador} é {divide_dois_numeros(numerador, denominador)}')
    except ValueError as verr:
        print(f'Um dos valores informados não é numérico: {verr} . Tente novamente!')
        continue
    except ZeroDivisionError:
        print('O denominador informado não pode ser zero.')
    except Exception as err:
        print(f'A divisão entre os números não pode ser realizada pelo seguinte motivo: {err}')

