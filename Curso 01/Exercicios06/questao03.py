# Tupla com as cores do arco-íris
cores = ("Vermelho", "Laranja", "Amarelo", "Verde", "Azul", "Anil", "Violeta")

# Solicitar um número de 1 a 7 ao usuário
numero = int(input("Digite um número de 1 a 7 para saber a cor correspondente: "))

# Exibir a cor correspondente, se o número estiver no intervalo correto
if 1 <= numero <= 7:
    print(f"A cor correspondente ao número {numero} é {cores[numero - 1]}.")
else:
    print("Número inválido! Digite um número de 1 a 7.")
