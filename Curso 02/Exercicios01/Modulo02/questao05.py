entrada = input("Digite uma lista de palavras separadas por espaço: ")
palavras = entrada.split()

palavras_ordenadas = sorted(palavras)
total_palavras = len(palavras)
palavras_maiusculas = [palavra.upper() for palavra in palavras]

print("Lista ordenada alfabeticamente:", palavras_ordenadas)
print("Número total de palavras:", total_palavras)
print("Palavras em maiúsculas:", palavras_maiusculas)
