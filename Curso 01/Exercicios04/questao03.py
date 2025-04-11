lista = list(map(int, input("Digite uma lista de números inteiros separados por espaço: ").split()))

# Remover duplicatas mantendo a ordem
lista_sem_duplicatas = []
for num in lista:
    if num not in lista_sem_duplicatas:
        lista_sem_duplicatas.append(num)

print(f"Lista sem duplicatas: {lista_sem_duplicatas}")
