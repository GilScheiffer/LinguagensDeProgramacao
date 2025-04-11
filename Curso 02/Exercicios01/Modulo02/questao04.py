def contar_vogais(frase):
    vogais = "aeiou"
    contagem = {vogal: 0 for vogal in vogais}
    for letra in frase.lower():
        if letra in contagem:
            contagem[letra] += 1
    return contagem

def inverter_frase(frase):
    return frase[::-1]

def substituir_espacos(frase):
    return frase.replace(" ", "-")

frase = input("Digite uma frase: ")

contagem_vogais = contar_vogais(frase)
frase_invertida = inverter_frase(frase)
frase_substituida = substituir_espacos(frase)

print("Contagem de vogais:", contagem_vogais)
print("Frase ao contrário:", frase_invertida)
print("Frase com espaços substituídos:", frase_substituida)
