class InvalidValueDepositException(Exception):
    "Excecao para nao permitir deposito com numeros invalidos"
    pass

class InvalidBalanceException(Exception):
    "Excecao para nao permitir saque com valores invalidos"
    pass