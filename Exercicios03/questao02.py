soma = 0

while True:
    numero = float(input("Digite um número (ou um número negativo para encerrar): "))
    if numero < 0:
        break
    soma += numero

print(f"A soma dos números positivos é: {soma:.2f}")
