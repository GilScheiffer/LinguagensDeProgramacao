def multiplicador(fator):
    def multiplicar(numero):
        return numero * fator
    return multiplicar

# Programa principal
dobro = multiplicador(2)
triplo = multiplicador(3)

num = int(input("Digite um número: "))
print("Dobro:", dobro(num))
print("Triplo:", triplo(num))
