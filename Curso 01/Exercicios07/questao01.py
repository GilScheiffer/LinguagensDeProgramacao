# Dicionário para armazenar os alunos e suas notas
alunos_notas = {}

# Cadastrar pelo menos 3 alunos
for i in range(3):
    nome = input("Digite o nome do aluno: ")
    nota = float(input(f"Digite a nota de {nome}: "))
    alunos_notas[nome] = nota

# Exibir a lista de alunos e suas respectivas notas
print("\nLista de alunos e suas notas:")
for nome, nota in alunos_notas.items():
    print(f"{nome}: {nota}")
