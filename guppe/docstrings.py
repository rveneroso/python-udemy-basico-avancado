'''
Docstrings de uma função é criado através das triplas aspas duplas conforme feito abaixo para a função
diz_oi().

O docstrings de uma função pode ser acessado via prompt do Python pelo comando help(nome_da_funcao)
ou ainda através de seu atributo __doc__ (são 2 underlines).
'''
def diz_oi():
    """ Uma função simples que retorna 'Oi!' """
    return 'Oi!'

def exponencial(numero, potencia=2):
    """
    Retorna o resultado de 'número' elevado à 'potência'. Caso não seja informada, 'potencia' terá o valor
    default 2.
    :param numero: Número que será elevado à potência informada.
    :param potencia: Potência à qual 'número' será elevado. Se não informado, será 2.
    :return: Resultado de 'número' elevado à 'potência'
    """
    return numero ** potencia