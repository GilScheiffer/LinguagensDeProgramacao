def eh_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numero = int(input("Digite um número inteiro para verificar se é primo: "))
resultado = eh_primo(numero)

if resultado:
    print(f"O número {numero} é primo.")
else:
    print(f"O número {numero} não é primo.")
