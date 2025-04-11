def contar_pares(n):
    for i in range(0, n + 1, 2):
        yield i

# Programa principal
limite = int(input("Digite um número: "))
print("Números pares até", limite, ":")
for par in contar_pares(limite):
    print(par)
