from datetime import datetime

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, cpf, data_nascimento, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento

class Conta:
    AGENCIA = "0001"

    def __init__(self, cliente, numero):
        self.saldo = 0.0
        self.numero = numero
        self.agencia = self.AGENCIA
        self.cliente = cliente
        self.historico = Historico()

    def saldo(self):
        return self.saldo

    def nova_conta(self, cliente, numero):
        return Conta(cliente, numero)

    def sacar(self, valor):
        if valor > 0 and self.saldo >= valor:
            self.saldo -= valor
            self.historico.adicionar_transacao(Saque(valor))
            return True
        return False

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.historico.adicionar_transacao(Deposito(valor))
            return True
        return False

class ContaCorrente(Conta):
    def __init__(self, cliente, numero, limite, limite_saques):
        super().__init__(cliente, numero)
        self.limite = limite
        self.limite_saques = limite_saques

class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

class Transacao:
    def registrar(self, conta):
        raise NotImplementedError("Subclass must implement abstract method")

class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor
        self.data = datetime.now()

    def registrar(self, conta):
        if conta.sacar(self.valor):
            print(f"Saque de R$ {self.valor:.2f} realizado com sucesso!")
        else:
            print("Falha no saque: saldo insuficiente.")

class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor
        self.data = datetime.now()

    def registrar(self, conta):
        conta.depositar(self.valor)
        print(f"Depósito de R$ {self.valor:.2f} realizado com sucesso!")

def main():
    cliente1 = PessoaFisica(nome="João Silva", cpf="12345678900", data_nascimento="01/01/1990", endereco="Rua A, 100")
    conta1 = ContaCorrente(cliente=cliente1, numero=1, limite=1000, limite_saques=3)

    cliente1.adicionar_conta(conta1)

    deposito = Deposito(200.0)
    cliente1.realizar_transacao(conta1, deposito)

    saque = Saque(50.0)
    cliente1.realizar_transacao(conta1, saque)

    saque = Saque(300.0)
    cliente1.realizar_transacao(conta1, saque)

if __name__ == "__main__":
    main()
