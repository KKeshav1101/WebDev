class InsufficientBalanceError(Exception):
        e="Insufficient funds"
class Account:

    def __init__(self,initial_amount=0.00):
        self.balance = initial_amount

    def withdrawal(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            amount=0
        self.balance=self.balance-amount
        try:
            if(self.balance<0):
                raise InsufficientBalanceError()
        except InsufficientBalanceError:
            print(InsufficientBalanceError.e)
            self.balance=self.balance+amount
        print("Balance =",self.balance)

    def deposit(self,amount):
        try:
            amount = float(amount)
        except ValueError:
            amount = 0
        self.balance=self.balance+amount
        print("Balance =",self.balance)

account=Account(500.00)
while True:
    print('''
            WELCOME!
          1.DEPOSIT
          2.WITHDRAW
          3.EXIT
    ''')
    op=int(input("Enter option :"))
    if op==1:
        amount=float(input("Enter amount to be deposited :"))
        account.deposit(amount)
    elif op==2:
        amount=float(input("Enter amount to be withdrawn :"))
        account.withdrawal(amount)
    elif op==3:
        print("<<<<EXIT>>>>")
        break
    else:
        print("INVALID OPTION ENTERED")
