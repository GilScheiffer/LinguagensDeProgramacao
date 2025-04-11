while True:
    try:
        numero = int(input("Digite um número inteiro: "))
        dobro = numero * 2
        print(f"O dobro de {numero} é {dobro}.")
        break  # Sai do loop se a conversão for bem-sucedida
    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite um número inteiro.")
