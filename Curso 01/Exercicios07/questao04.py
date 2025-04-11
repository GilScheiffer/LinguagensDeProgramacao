# Solicitar ao usuário uma frase
frase = input("Digite uma frase: ")

# Converter a frase em uma lista de palavras
palavras = frase.split()

# Dicionário para armazenar a contagem de cada palavra
contagem_palavras = {}

# Contar a ocorrência de cada palavra na frase
for palavra in palavras:
    if palavra in contagem_palavras:
        contagem_palavras[palavra] += 1
    else:
        contagem_palavras[palavra] = 1

# Exibir o dicionário com a contagem de palavras
print("\nContagem de palavras na frase:")
print(contagem_palavras)
