nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 7:
    print(f"Sua média é {media:.2f}. Você foi APROVADO!")
elif 5 <= media < 7:
    print(f"Sua média é {media:.2f}. Você está em RECUPERAÇÃO.")
else:
    print(f"Sua média é {media:.2f}. Você foi REPROVADO.")
