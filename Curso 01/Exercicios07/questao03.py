# Dicionário com algumas palavras em português e suas respectivas traduções em inglês
dicionario = {
    "casa": "house",
    "gato": "cat",
    "cachorro": "dog",
    "livro": "book",
    "carro": "car"
}

# Solicitar a palavra em português ao usuário
palavra_portugues = input("Digite uma palavra em português para saber sua tradução: ")

# Verificar se a palavra está no dicionário e exibir a tradução
if palavra_portugues in dicionario:
    print(f"A tradução de '{palavra_portugues}' para inglês é '{dicionario[palavra_portugues]}'.")
else:
    print("Desculpe, a tradução não foi encontrada.")
