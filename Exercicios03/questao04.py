inicio = int(input("Digite o primeiro número do intervalo (A): "))
fim = int(input("Digite o segundo número do intervalo (B): "))

for i in range(inicio, fim + 1):
    if i % 2 != 0:
        print(i)
