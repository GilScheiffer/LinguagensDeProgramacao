#caminho do arquivo no meu pc
caminho = r'C:\Users\grepi\Desktop\LinguagensDeProgramacao\Curso 02\Exercicios01\Modulo04\dados.txt'
try:
    with open(caminho, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
        print(f"Total de linhas: {len(linhas)}")
        print("\nConteúdo do arquivo:")
        for linha in linhas:
            print(linha.strip())
except FileNotFoundError:
    print("O arquivo 'dados.txt' não foi encontrado.")
except Exception as e:
    print("Ocorreu um erro ao ler o arquivo:", e)
