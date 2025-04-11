try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 / num2
except ZeroDivisionError:
    print("Erro: divisão por zero não é permitida.")
except ValueError:
    print("Erro: você deve digitar apenas números.")
else:
    print("Resultado da divisão:", resultado)
