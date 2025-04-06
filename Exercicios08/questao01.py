try:
    # Solicitar dois números ao usuário
    numerador = float(input("Digite o primeiro número (numerador): "))
    denominador = float(input("Digite o segundo número (denominador): "))

    # Realizar a divisão
    resultado = numerador / denominador
    print(f"O resultado da divisão é: {resultado}")

except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")

except ValueError:
    print("Erro: Por favor, digite apenas números válidos.")
