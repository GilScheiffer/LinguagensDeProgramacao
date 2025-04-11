# Tupla com os nomes e notas dos alunos
alunos_notas = ('Ana', 8.5, 'Carlos', 7.0, 'Beatriz', 9.2, 'Daniel', 6.8, 'Eduarda', 8.0)

# Exibindo apenas os nomes dos alunos
nomes = alunos_notas[::2]
print("Nomes dos alunos:", nomes)

# Exibindo apenas as notas dos alunos
notas = alunos_notas[1::2]
print("Notas dos alunos:", notas)
