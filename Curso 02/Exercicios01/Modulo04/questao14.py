import pickle

# Lista de números inteiros
numeros = [10, 20, 30, 40, 50]

# Gravar os números no arquivo binário
with open('dados.bin', 'wb') as arquivo_bin:
    pickle.dump(numeros, arquivo_bin)

# Ler e exibir os números do arquivo binário
with open('dados.bin', 'rb') as arquivo_bin:
    numeros_lidos = pickle.load(arquivo_bin)
    print("Números lidos do arquivo binário:", numeros_lidos)
