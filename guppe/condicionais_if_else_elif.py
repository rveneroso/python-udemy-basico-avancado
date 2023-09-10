idade = 26
# Identação é algo muito importante em condicionais. O bloco abaixo causa erro ao ser executado.
# Isso porque as duas linhas abaixo do comando if não estão corretamente alinhadas. Tudo aquilo
# que precisar ser executado como resultado do comando if deve ter a mesma identação.
# if idade < 18:
#  print('Menor de idade')
#   print(idade)

 # Corrigindo o problema acima
if idade < 18:
     print('Menor de idade')
     print(idade)

# Em Python, todo novo bloco de código começa após dois pontos
if idade < 18:
    print('Menor de idade')
elif idade == 18:
    print('Tem 18 anos')
elif idade == 26:
    print('Tem 26 anos')
else:
    print('Maior de idade')