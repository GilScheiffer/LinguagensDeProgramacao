n = int(input("Digite um número N para exibir os N primeiros termos da sequência de Fibonacci: "))

a, b = 0, 1

print("Sequência de Fibonacci:")
for i in range(n):
    print(a)
    a, b = b, a + b
