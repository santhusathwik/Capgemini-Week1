def check_balance(amount):
    print(f'Balance is {amount}')

def withdraw(amount):
    money=int(input("Enter money to be withdrawn"))
    if money>amount:
        print('Required funds are not available')
    else:
        amount=amount-money
        print('Money withdrawn')
    print(f'Balance is {amount}')
    return amount

def deposit(amount):
    money=int(input("Enter money to be deposited"))
    amount=amount+money
    print('Money deposited')
    print(f'Balance is {amount}')
    return amount

def exit():
    print("Thank You")
    return None

def atm(amount):
    print("\n1-Check Balance\n2-Withdraw\n3-Deposit\n4-Exit\n")
    choice=int(input("Enter the option"))
    if choice==1:
        check_balance(amount)
    elif choice==2:
        amount=withdraw(amount)
    elif choice==3:
        amount=deposit(amount)
    elif choice==4:
        return exit()
    else:
        print("Please enter correct option")
    return atm(amount)

amount1=int(input("Enter base amount"))
atm(amount1)