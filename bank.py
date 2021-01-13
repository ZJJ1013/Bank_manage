import datetime


def verify(func):
    def wrapper(self, *args, **kwargs):
        amount = str(args[0])
        index = amount.index(".")
        if len(amount) - index - 1 > 2:
            print("Wrong input")
        else:
            func(self, *args, **kwargs)

    return wrapper


class Bank(object):
    account_log = []

    def __init__(self, name):
        self.name = name

    @verify
    def deposit(self, amount):
        user.balance += amount
        self.write_log('Deposit', amount)

    @verify
    def withdraw(self, amount):
        if amount > user.balance:
            print('Wrong input')
        else:
            user.balance -= amount
        self.write_log('Withdraw', amount)

    def write_log(self, type, amount):
        now = datetime.datetime.now()
        create_time = now.strftime("%Y-%m-%d %H:%M-%S")
        data = [self.name, user.username, create_time, type, amount, f'{user.balance:.2f}']
        bank.account_log.append(data)

class TD(Bank):
    def __init__(self,name):
        self.name = name
class CIC(Bank):
    def __init__(self,name):
        self.name = name



class User(object):
    def __init__(self, username, balance):
        self.username = username
        self.balance = balance

    def print_log(self):
        print(bank.account_log)


bank = Bank('BMO')
user = User('Harry', 1000)

bank = TD('TD Bank')
user = User('Harry',1000)
def show_menue():
    menu = '''
0: Exit
1: Deposit
2: Withdraw
3: Stats'''
    print(menu)


while True:
    show_menue()
    num = int(input('Please Enter a Number: '))
    if num == 0:
        print('Exit')
        break
    elif num == 1:
        print('Deposit')
        amount = float(input('Enter amount'))
        bank.deposit(amount)
        print(f'The balance is: {user.balance:.2f}')

    elif num == 2:
        print('Withdraw')
        amount = float(input('Enter amount'))
        bank.withdraw(amount)
        print(f'The balance is: {user.balance:.2f}')
    elif num == 3:
        print('Status')
        user.print_log()
    else:
        print('Error')
