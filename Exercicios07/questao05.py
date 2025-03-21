# Dicionário com códigos de produtos como chaves e tuplas (nome, preço) como valores
catalogo = {
    "001": ("Arroz", 25.50),
    "002": ("Feijão", 8.30),
    "003": ("Macarrão", 3.75),
    "004": ("Açúcar", 2.10),
    "005": ("Óleo", 5.45)
}

# Solicitar o código do produto ao usuário
codigo_produto = input("Digite o código do produto para buscar seu nome e preço: ")

# Verificar se o código do produto está no catálogo e exibir as informações
if codigo_produto in catalogo:
    produto, preco = catalogo[codigo_produto]
    print(f"O produto {produto} tem o preço de R${preco:.2f}.")
else:
    print("Produto não encontrado no catálogo.")
