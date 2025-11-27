from functions_main import inputs_create_current_account, create_account 
from Account import CurrentAccount
from Exceptions import AccountAlreadyExistsException
def menu():
    accounts = {}

    while True:
        print("1 - Criar conta corrente.\n2 - Criar conta poupança.\n3 - Fazer login.\n 4 - Sair.")
        option = int(input("Digite uma opção: "))
        if option == 1:
            number, client, balance, password, limit = inputs_create_current_account()
            new_account = CurrentAccount(number, client, balance, password, limit)
            try:
                create_account(accounts, number, new_account)
            except AccountAlreadyExistsException as e:
                print(e)
        elif option == 2:
            pass
if __name__ == "__main__":
    menu()