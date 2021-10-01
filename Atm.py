class ATM:
    withdraw = 3000
    balance = 20000


    def __init__(self,withdraw,balance):
        self.withdraw= withdraw
        self.balance = balance

    def ready(self):
        print("You have withdrawed Rs.",self.withdraw," and your balance is Rs.",self.balance)

widrw = input("Enter cash to be withdrawed")

cash1 = ATM(widrw,20000)
cash1.ready()




