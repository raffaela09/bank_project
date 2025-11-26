from datetime import datetime

class Transaction:
    def __init__(self, type: str, value: float, account: 'Account'):
        self._type = type
        self._value = value
        self._account = account
        self._date = datetime.now()

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def account(self):
        return self._account

    @account.setter
    def account(self, value):
        self._account = value

    @property
    def date(self):
        return self._date

    def get_receipt(self):
        print("===================================")
        print("         RECIBO BANCÁRIO")
        print("===================================")
        print(f"Date: {self.date}")
        print(f"Tipo de operação: {self.type}")
        print(f"Conta: {self._account.number} ")
        print(f"Cliente: {self._account.client}")
        print(f"Valor: R${self.value}")
        print(f"Saldo atual: R${self._account.balance}")
        print(f"Obrigado por usar o nosso banco!")
        print("===================================")
        
        #terminar recibo
        