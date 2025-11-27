from Exceptions import AccountAlreadyExistsException

def inputs_create_current_account():
    number = input("Número da conta: ")
    client = input("Cliente: ")
    balance = float(input("Saldo: "))
    password = input("Senha: ")
    limit = float(input("Limite: "))
    return number, client, balance, password, limit

def create_account(accounts, number, account):
    if number in accounts:
        raise AccountAlreadyExistsException("Número de conta já existente.")
    accounts[number] = account
    print("Conta criada com sucesso!")
    return account

def inputs_create_savings_account():
    number = input("Número da conta: ")
    titular = input("Titular da conta: ")
    balance = float(input("Saldo: "))
    password = input("Senha: ")
    earnings = float(input("Rendimento: "))
    return number, titular, balance, password, earnings

def inputs_login():
    number = input("Número da conta: ")
    password = input("Senha: ")
    return number, password