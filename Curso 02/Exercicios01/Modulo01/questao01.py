import math
import random

def main():
    try:
        numero = float(input("Digite um número para calcular a raiz quadrada: "))
        raiz = math.sqrt(numero)
        print(f"A raiz quadrada de {numero} é {raiz:.2f}")
    except ValueError:
        print("Erro: Digite um número válido.")

    aleatorio = random.randint(1, 100)
    print(f"Número aleatório gerado entre 1 e 100: {aleatorio}")

if __name__ == "__main__":
    main()
