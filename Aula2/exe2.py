class ContaBancaria:
    def __init__(self, titular:str, saldo:float):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, deposito):
        self.saldo += deposito
        print(f'Houve deposito no valor de R$ {deposito}')
    
    def sacar(self, saque):
        self.saldo -= saque
        print(f'Houve saque no valor de R$ {saque}')

    def exibir_saldo(self):
        print(f'Seu saldo é de R$ {self.saldo:.2f}')


cliente1 = ContaBancaria('Victor', 1500.55)

cliente1.exibir_saldo()

cliente1.sacar(255.70)

cliente1.exibir_saldo()

cliente1.depositar(2410.50)

cliente1.exibir_saldo()

