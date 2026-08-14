class ContaCorrente:
    def __init__(self, saldo=0):
        self.saldo = saldo

# Nao fiz uma funcao separada para verificar viabilidade pois adicionei somente o atributo de saldo, nada de limite ou coisa do tipo
    def sacar(self, valor):
        if self.saldo < valor:
            print("Nao foi possivel sacar, saldo insuficiente")
            return
        self.saldo -= valor

    def depositar(self, valor):
        if valor <= 0:
            print("Insira um valor maior que 0 para fazer um deposito")
            return
        self.saldo += valor

    def transferir(self, valor, conta_destino):
        if isinstance(conta_destino, ContaCorrente):
            self.sacar(valor)
            conta_destino.depositar(valor)

    def verificar_saldo(self):
        print(f"Saldo atual: {self.saldo}")


conta_origem = ContaCorrente(100)
conta_destino = ContaCorrente(50)

conta_origem.transferir(50, conta_destino)

conta_origem.verificar_saldo() # Abaixou para 50
conta_destino.verificar_saldo() # Aumentou para 100
