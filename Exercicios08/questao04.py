numeros = [10, 20, 30, 40, 50]

try:
    indice = int(input("Digite um índice (0 a 4) para acessar um valor da lista: "))
    print(f"O valor no índice {indice} é: {numeros[indice]}")
except IndexError:
    print("Erro: Índice fora do intervalo da lista. Tente um número entre 0 e 4.")
except ValueError:
    print("Erro: Por favor, digite um número inteiro válido.")
