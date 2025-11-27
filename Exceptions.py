class InvalidValueDepositException(Exception):
    "Excecao para nao permitir deposito com numeros invalidos"
    pass

class InvalidBalanceException(Exception):
    "Excecao para nao permitir saque com valores invalidos"
    pass

class InvalidPasswordException(Exception):
    "Excecao para autenticacao, caso a senha esteja incorreta."
    pass

class RequireLoginException(Exception):
    "Excecao para acoes que precisam de login"
    pass

class AccountAlreadyExistsException(Exception):
    "Excecao para conta ja existente."
    pass