# Se eu quiser somente a parte inteira de uma divisão devo usar o operador //
print(5 // 2)

# Inteiros no Python estão limitados apenas pela memória do computador. Portanto, a linha abaixo
# cria uma variável perfeitamente válida
numero_muito_grande = 2**8793
print(f'numero_muito_grande vale {numero_muito_grande}')

# Python permite separar centenas em um número com underline. Isso facilita a legibilidade para humanos
# e ainda preserva o valor como válido.
numero_um_muito_grande = 1_000_000_000
numero_dois_muito_grande = 8_000_000_000_000
soma_muito_grande = numero_um_muito_grande +  numero_dois_muito_grande
print(f'soma_muito_grande vale {soma_muito_grande}')

# Python permite atribuir valores diferentes a diferentes variáveis em uma única linha
valor1, valor2 = 27, 32
print(valor1)
print(valor2)