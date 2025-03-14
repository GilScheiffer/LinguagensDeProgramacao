lista = list(map(int, input("Digite uma lista de números inteiros separados por espaço: ").split()))
numero = int(input("Digite o número que deseja contar na lista: "))

ocorrencias = lista.count(numero)

print(f"O número {numero} aparece {ocorrencias} vez(es) na lista.")
