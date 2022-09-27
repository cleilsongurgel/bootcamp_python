# Importando bibliotecas
from datetime import datetime as dt


# função principal do programa
def op_bank():
    menu = """
        [D] => Depositar
        [S] => Sacar
        [E] => Extrato
        [Q] => Sair

    """
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    cont = 0

    while True:
        # Menu
        op = input(menu)



        if op == 'd' or op == "D":
            print("#### Opção Deposito ####")
            valor = float(input("Informe o valor a ser depositado: "))
            if valor > 0:
                saldo += valor
                registro = dt.now()
                extrato += f"{registro} + Valor depositado: R$ {valor:.2f} \n"

            else:
                print("Não é possível depositar o valor.")
                print("Digite um valor válido.")

        if op == 's' or op == "S":
            print("#### Opção Saque ####")
            saque = float(input("Informe o valor que você deseja sacar: "))

            # Regras de negócio

            # Limitando a quantidade de saques em 3
            cond1 = numero_saques >= LIMITE_SAQUES

            # O saque não pode ultrapassar o valor limite
            cond2 = saque > limite

            # O saque tem que ser menor ou igual ao saldo
            cond3 = saque >= saldo

            # O saque tem que ser um valor positivo
            cond4 = (cond1 == False and cond2 == False and cond3 == False)

            if cond1:
                print("Limite de saques excedido!!! ")
                print("Dirija-se até uma agencia... ")
            elif cond2:
                print("Valor acima do permitido!!! ")
            elif cond3:
                print("Saldo insuficiente. Verifique seu saldo !!!")
            elif cond4:
                saldo -= saque
                numero_saques += 1
                extrato += f"{registro} - Valor retirado: R$ {saque:.2f} \n"


        if op == 'e' or op == "E":
            print("#### Opção Extrato ####")
            if extrato == "":
                print("Não foram realizadas movimentações nessa conta")
            else:
                print("Extrato de movimentações: ")
                print(extrato)

                print("Seu saldo é de R$ {:.2f} ".format(saldo))

        if op == 'q' or op == "Q":
            print("Saindo da aplicação...")
            print("Obrigado por utilizar nossos serviços :D")
            break




# Iniciando o programa
if __name__ == '__main__':
    print("#### Banco v1 ####\n")
    print(op_bank())
    print("#### Banco v1 ####\n")


