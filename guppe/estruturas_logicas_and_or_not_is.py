usuario_ativo = True

# O operodor is eventualmente pode se mostrar desnecessário. Os dois blocos abaixo dão o mesmo resultado,
# o que significa que a forma mais simples (segundo if) deve ser preferencialmente utilizada.
if usuario_ativo is True:
    print('Usuário está ativo')

if usuario_ativo:
    print('Usuário está ativo')

# Em testes envolvendo valores falsos o operador is torna-se um pouco menos redundante, mas ainda assim
# pode ser substituído por uma operação com o operador not conforme mostrado abaixo.
usuario_logado = False
if usuario_logado is False:
    print('Usuário não está logado')

if not(usuario_logado):
    print('Usuário não está logado')