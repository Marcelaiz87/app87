from Cliente import Cliente
from Conta import Conta

print("=== Bem-vindo ao Banco Python ===")

# Cadastro do cliente
nome = input("Digite o nome do cliente: ")
telefone = input("Digite o telefone do cliente: ")
cliente = Cliente(nome, telefone)

# Criação da conta
numero = input("Digite o número da conta: ")
conta = Conta(numero, cliente)

print("\nConta criada com sucesso!")
print(conta)

# Menu de operações
while True:
    print("\n--- Operações Bancárias ---")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Consultar Saldo")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        valor = float(input("Digite o valor do depósito: "))
        conta.depositar(valor)
    elif opcao == "2":
        valor = float(input("Digite o valor do saque: "))
        conta.sacar(valor)
    elif opcao == "3":
        conta.consultar_saldo()
    elif opcao == "4":
        print("Saindo... Obrigado por usar o Banco Python!")
        break
    else:
        print("Opção inválida, tente novamente.")









