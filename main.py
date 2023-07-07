from datetime import datetime


def depositar(valor_inicial, extrato):
    valor_deposito: float = float(input("Digite o valor do depósito: "))
    valor_inicial += valor_deposito
    extrato += "\n{} - Depósito realizado. Quantia: R${:.2f}".format(datetime.now(), valor_deposito)
    print("\nDepósito realizado com sucesso. ")

    return valor_inicial, extrato


def sacar(*, valor_inicial, extrato, limite, numero_saques):
    valor_saque: float = float(input("Digite o valor do saque: "))
    while valor_saque > limite or valor_saque > valor_inicial:
        valor_saque = float(input("Digite um valor válido para saque: "))

    valor_inicial -= valor_saque
    numero_saques += 1

    extrato += "\n{} - Saque realizado. Quantia: R${:.2f}".format(datetime.now(), valor_saque)
    print("\nSaque realizado com sucesso. ")

    return valor_inicial, extrato, numero_saques


def mostrar_extrato(valor_inicial, /, *, extrato):
    extrato_final = "Extrato Bancário\n" + extrato + "\n\nSaldo atual: R${:.2f}".format(valor_inicial)
    return extrato_final


def verifica_uso_cpf(cpf, clientes):
    for cliente in clientes:
        if cliente["cpf"] == cpf:
            return True
    return False


def criar_cliente(clientes):
    cpf: str = input("Digite seu CPF: ")

    cpf_usado: bool = verifica_uso_cpf(cpf, clientes)
    if cpf_usado:
        print("CPF já foi utilizado. ")
        return

    nome: str = input("Digite seu nome: ")
    data_nasc: str = input("Digite sua data de nascimento (aaaa-mm-dd): ")

    clientes.append({"nome": nome, "cpf": cpf, "data_nasc": data_nasc})
    print("Cliente cadastrado com sucesso. ")


def criar_conta(agencia, numero_conta, clientes, contas):
    cpf: str = input("Informe o CPF da conta: ")

    cpf_usado: bool = verifica_uso_cpf(cpf, clientes)
    if not cpf_usado:
        print("CPF não foi cadastrado no sistema. ")
        return numero_conta

    contas.append({"agencia": agencia, "numero_conta": numero_conta, "cpf": cpf})
    print("Conta cadastrada com sucesso. ")

    return numero_conta + 1


def listar_contas(contas):
    for conta in contas:
        conta_str: str = f"\nAGÊNCIA: {conta['agencia']}\nNÚMERO DA CONTA: {conta['numero_conta']}\nCPF TITULAR: {conta['cpf']}\n---------------------"
        print(conta_str)


def main():
    menu: str = """
        =========== BANCO TAL ===========
        [d]   Depósito
        [s]   Saque
        [e]   Extrato
        [ccl] Criar cliente
        [cco] Criar conta
        [lco] Listar contas
        [q]   Sair
        =================================
    """
    MAX_SAQUES_DIA: int = 3
    MAX_VALOR_SAQUE: float = 500.0
    AGENCIA: str = "0001"
    log: str = ""
    saldo: float = 0.0
    num_saques: int = 0
    num_nova_conta: int = 0
    clientes = []
    contas = []

    while True:
        opcao: str = input(menu)

        match opcao:
            case "d":
                saldo, log = depositar(saldo, log)

            case "s":
                if num_saques >= MAX_SAQUES_DIA:
                    log += f"\n{datetime.now()} - Tentativa bloqueada de saque: Limite diário de saques atingido."
                    print("\nTentativa bloqueada de saque: Limite diário de saques atingido.")
                elif saldo <= 0:
                    print("\nNão há saldo para ser sacado. ")
                else:
                    saldo, log, num_saques = sacar(valor_inicial=saldo, extrato=log, limite=MAX_VALOR_SAQUE,
                                                   numero_saques=num_saques)

            case "e":
                print(mostrar_extrato(saldo, extrato=log))

            case "ccl":
                criar_cliente(clientes)

            case "cco":
                num_nova_conta = criar_conta(AGENCIA, num_nova_conta, clientes, contas)

            case "lco":
                listar_contas(contas)

            case "q":
                break

            case _:
                print("\nOpção não existente. ")


main()
