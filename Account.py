from typing import List
from abc import ABC, abstractmethod
from Authenticate import Authenticate
from Transaction import Transaction
from Tax import Tax
from Earning import Earning
from datetime import datetime
from Exceptions import InvalidValueDepositException, InvalidBalanceException, InvalidPasswordException, RequireLoginException

#ver de guardar um status de talvez logado 

#Classe de conta, abstrata
class Account(Authenticate, ABC):
    def __init__(self, number: str, client: str, balance: float, password: str):
        self._number = number
        self._client = client
        self._balance = balance
        self._password = password
        self._logged = False 
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

    @abstractmethod
    def withdraw(self, value: float):
        pass

    @abstractmethod   
    def deposit(self, value: float):
        pass 
    
    #fucao para fazer login
    def login(self, password: str):
        if password == self._password:
            self._logged = True
        else:
            raise InvalidPasswordException
    
    def require_login(self):
        if not self._logged:
            raise RequireLoginException("É necessário estar logado para realizar essa ação.")
    
    def logout(self) -> bool:
        self._logged = False
        return self._logged
    
    def total(self):
        pass #-> o que seria?
    
    def print_total(self):
        pass #-> o que seria? 
#---------------------------------------------------------------------------------

#Classe de conta corrente
#Conta corrente -> ela pode ficar com saldo negativo -> ja que tem um limite disponivel, entao é permitido saques onde seja menor que limite + saldo -> passar para docstrings
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
    def withdraw(self, value: float, password: str):
        withdraw = value + self._tax #taxa por saque é 10 reais
        available = self._balance + self._limit 
        
        if self.auntheticate(password):
            if withdraw <= available :
                self.balance -= withdraw
                print(f"Valor disponivel em conta: {self._balance}") #valor disponivel na conta
                transaction = Transaction("Saque - Conta Corrente", value, self) 
                transaction.get_receipt()
                self._transactions.append(transaction)
            else:
                raise InvalidBalanceException("Saldo insuficiente.") #levanta a excecao
        else:
            raise InvalidPasswordException("Senha inválida.")

    #deposito        
    def deposit(self, value:float, password: str):
        deposit = value
        
        if self.auntheticate(password):
            if deposit > 0 :
                self._balance += deposit
                transaction = Transaction("Depósito - Conta Corrente", value, self) 
                self._transactions.append(transaction)
                transaction.get_receipt()
            else:
                raise InvalidValueDepositException("Não é permitido depósitos negativos.") #levanta a excecao
        else:
            raise InvalidPasswordException("Senha inválida.")

    #valor da taxa    
    def get_tax_value(self) -> float:
        return f"Valor da taxa: {self._balance * 0.07}"
        
#---------------------------------------------------------------------------------

#Conta poupanca  -> contrato(interface) é a classe Earning(ganhando/rendendo)     
class Savings_account(Account, Earning):
    def __init__(self, number: str, titular: str, balance: float, password: str, earnings: float):
        super().__init__(number, titular, balance, password)
        self._earnings = earnings
        self._date = datetime.now().day

    def get_Earning(self):
        return self.balance * self._earnings

    #na conta poupanca, nao é permitido que a o saldo fique negativo
    def withdraw(self, value: float, password: str):
        if self.auntheticate(password):
            if value <= self._balance:
                self._balance -= value
                transaction = Transaction("Saque - Conta Poupança", value, self) 
                self._transactions.append(transaction)
                transaction.get_receipt()
            else:
                raise InvalidBalanceException("Saldo insuficiente.") #levanta a excecao
        else:
            raise InvalidPasswordException("Senha inválida.")

    def deposit(self, value:float, password: str):
        deposit = value
        if self.auntheticate(password):
            if value > 0: 
                self._balance += deposit
                transaction = Transaction("Depósito - Conta Poupança", value, self) 
                self._transactions.append(transaction)
                transaction.get_receipt()
            else:
                raise InvalidValueDepositException("Não é permitido depositos menores que zero.") #levanta a excecao
        else:
            raise InvalidPasswordException("Senha inválida.")

#---------------------------------------------------------------------------------
