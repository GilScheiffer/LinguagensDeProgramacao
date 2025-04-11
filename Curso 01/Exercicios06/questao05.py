# Tupla com os 10 primeiros colocados do campeonato
times = ("Flamengo", "Palmeiras", "São Paulo", "Atlético-MG", "Grêmio", "Fluminense", "Internacional", "Santos", "Corinthians", "Vasco")

# Exibindo os três primeiros colocados
print("Três primeiros colocados:", times[:3])

# Exibindo os últimos três colocados
print("Últimos três colocados:", times[-3:])

# Exibindo os times em ordem alfabética
print("Times em ordem alfabética:", sorted(times))

# Solicitar o nome de um time e exibir sua posição
time_especifico = input("Digite o nome de um time para saber sua posição: ")
if time_especifico in times:
    posicao = times.index(time_especifico) + 1
    print(f"O time {time_especifico} está na posição {posicao}.")
else:
    print("Time não encontrado na classificação.")
