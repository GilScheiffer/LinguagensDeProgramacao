import os
import time
import datetime
import calendar

# Exibe o diretório atual
print("Diretório atual:", os.getcwd())

# Exibe a data e hora atuais
agora = datetime.datetime.now()
print("Data e hora atuais:", agora)

# Exibe o calendário do mês atual
ano = agora.year
mes = agora.month
print(f"\nCalendário de {mes}/{ano}:")
print(calendar.month(ano, mes))

# Pausa de 3 segundos
print("Pausando por 3 segundos...")
time.sleep(3)
print("Programa retomado.")
