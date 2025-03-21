# Solicitar a palavra ao usuário
palavra = input("Digite uma palavra: ")

# Dicionário para armazenar a contagem de cada caractere
contagem = {}

# Contar a ocorrência de cada caractere na palavra
for caractere in palavra:
    if caractere in contagem:
        contagem[caractere] += 1
    else:
        contagem[caractere] = 1

# Exibir o dicionário com a contagem de caracteres
print("\nContagem de caracteres:")
print(contagem)
