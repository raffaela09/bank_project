from functions_main import inputs_create_current_account, create_account, inputs_create_savings_account, inputs_login
from Account import CurrentAccount, SavingsAccount
from Exceptions import AccountAlreadyExistsException, InvalidPasswordException
def menu():
    accounts = {}

    while True:
        print("1 - Criar conta corrente.\n2 - Criar conta poupança.\n3 - Fazer login.\n4 - Sair.")
        option = int(input("Digite uma opção: "))
        if option == 1:
            number, client, balance, password, limit = inputs_create_current_account()
            new_account = CurrentAccount(number, client, balance, password, limit)
            try:
                create_account(accounts, number, new_account)
            except AccountAlreadyExistsException as e:
                print(e)

        elif option == 2:
            number_saving, titular, balance_saving, password_saving, earnings = inputs_create_savings_account()
            new_account_saving = SavingsAccount(number_saving, titular, balance_saving, password_saving, earnings)
            try:
                create_account(accounts, number_saving, new_account_saving)
            except AccountAlreadyExistsException as e:
                print(e)

        elif option == 3: 
            number_login, password_login = inputs_login()
            if number_login in accounts:
                try: 
                    account = accounts[number_login]
                    account.login(password_login)
                    print("Login efetuado! Bem vindo!")
                except InvalidPasswordException as e: 
                    print(e)
            else:
                print("Conta inexistente!") #verificar se precisa de exception
        elif option == 4:
            print("Até mais!!")
            break

if __name__ == "__main__":
    menu()