try:
    # Solicitar o nome do arquivo ao usuário
    nome_arquivo = input("Digite o nome do arquivo a ser lido: ")

    # Tentar abrir e ler o conteúdo do arquivo
    with open(nome_arquivo, 'r') as arquivo:
        conteudo = arquivo.read()
        print("\nConteúdo do arquivo:")
        print(conteudo)

except FileNotFoundError:
    print("Erro: Arquivo não encontrado. Verifique o nome e tente novamente.")

except Exception as e:
    print(f"Ocorreu um erro ao tentar ler o arquivo: {e}")
