from Cliente import Cliente

class Conta:
    def __init__(self, numero, cliente, saldo=0.0):
        self.numero = numero
        self.cliente = cliente
        self.__saldo = saldo  # saldo privado

    # Depositar (regra de negócio)
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")
        else:
            print("Valor inválido para depósito!")

    # Sacar (regra de negócio)
    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso!")
        else:
            print("Saldo insuficiente ou valor inválido!")

    # Consultar saldo
    def consultar_saldo(self):
        print(f"Saldo atual: R${self.__saldo:.2f}")

    # Representação da conta
    def __str__(self):
        return f"Conta {self.numero} - {self.cliente.nome} | Saldo: R${self.__saldo:.2f}"
