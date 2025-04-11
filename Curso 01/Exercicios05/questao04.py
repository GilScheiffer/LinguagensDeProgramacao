def contar_vogais(palavra):
    vogais = "aeiouAEIOU"
    return sum(1 for letra in palavra if letra in vogais)

# Solicitar a palavra ao usuário
palavra = input("Digite uma palavra para contar as vogais: ")

# Contar as vogais
quantidade_vogais = contar_vogais(palavra)

print(f"A palavra '{palavra}' contém {quantidade_vogais} vogal(is).")
