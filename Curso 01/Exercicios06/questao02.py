# Solicitar ao usuário quatro números inteiros
numeros = tuple(map(int, input("Digite quatro números inteiros separados por espaço: ").split()))

# Quantas vezes o número 9 apareceu na tupla
vezes_nove = numeros.count(9)

# Posição do primeiro número 3
posicao_tres = numeros.index(3) if 3 in numeros else -1

# Números pares na tupla
numeros_pares = [num for num in numeros if num % 2 == 0]

# Exibindo os resultados
print(f"O número 9 apareceu {vezes_nove} vez(es) na tupla.")
if posicao_tres != -1:
    print(f"O primeiro número 3 foi digitado na posição {posicao_tres}.")
else:
    print("O número 3 não foi digitado.")
print(f"Números pares na tupla: {numeros_pares}")
