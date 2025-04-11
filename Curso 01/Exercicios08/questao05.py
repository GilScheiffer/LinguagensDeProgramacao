class SaldoInsuficienteError(Exception):
    """Exceção personalizada para saldo insuficiente."""
    pass

def sacar(saldo, valor_saque):
    if valor_saque > saldo:
        raise SaldoInsuficienteError("Erro: Saldo insuficiente para realizar o saque.")
    return saldo - valor_saque

def main():
    saldo = 1000.00

    try:
        valor = float(input("Digite o valor que deseja sacar: R$ "))
        saldo = sacar(saldo, valor)
        print(f"Saque realizado com sucesso! Saldo restante: R$ {saldo:.2f}")
    except ValueError:
        print("Erro: Valor inválido. Digite um número.")
    except SaldoInsuficienteError as e:
        print(e)

if __name__ == "__main__":
    main()
