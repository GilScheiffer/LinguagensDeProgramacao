def calcular_media(lista):
    return sum(lista) / len(lista) if lista else 0

# Solicitar os números ao usuário
numeros = list(map(float, input("Digite os números separados por espaço: ").split()))

# Calcular a média
media = calcular_media(numeros)

print(f"A média dos números é: {media:.2f}")
