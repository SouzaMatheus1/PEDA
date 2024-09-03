class Conta:
    def __init__(self, nome, num_conta, sald, sal_mensal, lim_saque):
        self.nome = nome
        self.num_conta = num_conta
        self.saldo = sald
        self.sal_mensal = sal_mensal
        self.lim_saque = lim_saque
        self.verificaSaque(lim_saque)

    def verificaSaque(self, lim_saque):
        if self.sal_mensal < lim_saque:
            self.lim_saque = self.sal_mensal - (self.sal_mensal * 0.05)
        
    def deposito(self, deposito):
        self.saldo = deposito

    def saque(self, valor_saque):
        if valor_saque > self.saldo and valor_saque > self.lim_saque:
            return False
        return True
    
    def saldo(self):
        return self.saldo
    
    def dados(self):
        return f"""
Nome = R${self.nome}
Nº da conta = R${self.num_conta}
Saldo = R${self.saldo}
Sálario mensal = R${self.sal_mensal}
Limite de saque = R${self.lim_saque}
                                    """

    def __str__(self) -> str:
        return f'conta n = {self.num_conta}'
        
if __name__ == "__main__":
    c1 = Conta('mat', 81, 100, 2000, 1000)

    print(c1.dados())