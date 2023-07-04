import datetime

menu: str = """
    =========== BANCO TAL ===========
    [d] Depósito
    [s] Saque
    [e] Extrato
    [q] Sair
    =================================
"""
log: str = ""
saldo: float = 0.0
num_saques: int = 0
MAX_SAQUES_DIA: int = 3
MAX_VALOR_SAQUE: float = 500.0


def depositar() -> None:
    global saldo, log

    valor_deposito: float = float(input("Digite o valor do depósito: "))
    saldo += valor_deposito
    log += "\n{} - Depósito realizado. Quantia: R${:.2f}".format(datetime.datetime.now(), valor_deposito)
    print("\nDepósito realizado com sucesso. ")


def sacar() -> None:
    global saldo, log, num_saques, MAX_SAQUES_DIA

    if num_saques >= MAX_SAQUES_DIA:
        log += f"\n{datetime.datetime.now()} - Tentativa bloqueada de saque: Limite diário de saques atingido."
        print("\nTentativa bloqueada de saque: Limite diário de saques atingido.")
        return

    valor_saque: float = float(input("Digite o valor do saque: "))
    while valor_saque > 500 or valor_saque > saldo:
        valor_saque = float(input("Digite um valor válido para saque: "))

    saldo -= valor_saque
    num_saques += 1

    log += "\n{} - Saque realizado. Quantia: R${:.2f}".format(datetime.datetime.now(), valor_saque)

    print("\nSaque realizado com sucesso. ")


def mostrar_extrato() -> None:
    global log, saldo

    extrato = "Extrato Bancário\n" + log + "\n\nSaldo atual: R${:.2f}".format(saldo)
    print(extrato)

    input("\nPressione qualquer tecla para continuar...")


while True:
    opcao: str = input(menu)

    match opcao:
        case "d":
            depositar()
        case "s":
            if saldo > 0:
                sacar()
            else:
                print("\nNão há saldo para ser sacado. ")
        case "e":
            mostrar_extrato()
        case "q":
            break
        case _:
            print("\nOpção não existente. ")
