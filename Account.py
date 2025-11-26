from typing import List
from abc import ABC, abstractmethod
from Authenticate import Authenticate
from Transaction import Transaction
from Tax import Tax
from Earning import Earning
from datetime import datetime


#Classe de conta, abstrata
class Account(Authenticate, ABC):
    def __init__(self, number: str, client: str, balance: float, password: str):
        self._number = number
        self._client = client
        self._balance = balance
        self._password = password
        self._transactions: List['Transaction'] = []

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        self._number = value

    @property
    def client(self):
        return self._client

    @client.setter
    def client(self, value):
        self._client = value

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value
        
    def authentication(self, password: str):
        pass 
    @abstractmethod
    def withdraw(self, value: float):
        pass
    @abstractmethod   
    def deposit(self, value: float):
        pass 
    
    def auntheticate(self, password: str) -> bool:
        return self._password == password
    
    def total(Self):
        pass
    
    def print_total(self):
        pass 
#---------------------------------------------------------------------------------

#Classe de conta corrente
class Current_account(Account, Tax):
    def __init__(self, number: str, client: str, balance: float, password: str,  limit: float):
        super().__init__(number, client, balance, password)
        self._limit = limit
        self._tax = 10.0
        self._transactions : List['Transaction'] = []

    @property
    def limit(self):
        return self._limit

    @limit.setter
    def limit(self, value):
        self._limit = value

    @property
    def tax(self):
        return self._tax

    @tax.setter
    def tax(self, value):
        self._tax = value

    #saque    
    def withdraw(self, value):
        withdraw = value + self._tax #taxa por saque é 10 reais
        available = self._balance + self._limit 
        
        if withdraw <= available:
            self.balance -= withdraw
            print(f"the remaining value on the account is: {self._balance}") #valor disponivel na conta
            transaction = Transaction("current", value, self) #ajusta o valor após o saque
            self._transactions.append(transaction)
        else:
           raise #erro de que nao é possivel sacar -> Personalizado

    #deposito        
    def deposit(self, value):
        deposit = value
        self._balance += deposit
        #excecao pra numero negativo? -> nao permitir depositar um numero negativo, ou permitir fazer deposito a partir de determinado valor (1 real etc) -> personalizar

    #valor da taxa    
    def get_tax_value(self):
        return self._balance * 0.07 
        
#---------------------------------------------------------------------------------


#Conta poupanca  -> contrato(interface) é a classe Earning(ganhando/rendendo)     
class Savings_account(Account, Earning):
    def __init__(self, number: str, titular: str, balance: float, password: str, earnings: float):
        super().__init__(number, titular, balance, password)
        self._earnings = earnings
        self._date = datetime.now().day

    #falta implementar saque e deposito -> ja que é heranca de account 
    def get_Earning(self):
        print (self.balance * self._earnings)

    def withdraw(self, value):
        if value <= self._balance:
            self._balance -= value
        else:
            print("saldo insuficiente") #excecao personlizada de saldo insuficiente aqqui <-----

    def deposit(self, value):
        if value > 0: 
            deposit = value
            self._balance += deposit
        else:
            print("Não é permitido fazer deposito com numeros negativos") #excecao personalizada para nao permitir numeros negativo - faz sentido?
        #vale uma excecao pra nao permitir 
#---------------------------------------------------------------------------------


conta = Current_account(12343, "rafa", 500, 1234, 1000)
# print()
conta.withdraw(200)
conta.withdraw(200)

poup = Savings_account("112f", "rafa", 500, 1234, 0.2)
poup.get_Earning()