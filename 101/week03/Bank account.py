class BankAccount:

    hist = []

    def __init__(self, name, ballance, curruncy):
        self.name = name
        self.ballance = ballance
        self.curruncy = curruncy
        BankAccount.hist.append("Account was created")

    def deposit(self, suma):
        self.ballance += suma
        BankAccount.hist.append("Deposited" + str(suma) + str(self.curruncy))

    def withdraw(self, suma1):
        if(suma1 > self.ballance):
            return False
        else:
            self.ballance = self.ballance - suma1
            return True

    def __str__(self):
        return "Bank account for {}".format(self.name) + " with balance of {}".format(self.ballance) + "{}".format(self.curruncy)

    def _balance(self):
        return self._deposit()

    def __int__(self):
        return self.ballance

    def transfer_to(self, account, amount):
        if self.curruncy == account.curruncy:
            if self.ballance > amount:
                self.ballance = self.ballance - amount
                account.ballance = account.ballance + amount
                BankAccount.hist.append(
                    "Transfer to" + account.name + str(amount) + account.curruncy)
                BankAccount.hist.append(
                    "Transfer from" + self.name + str(amount) + self.curruncy)
                return True
            else:
                return False
        else:
            return False

    def _history(self):
        return BankAccount.hist

bacc = BankAccount("Pe6o", 0, "$")
print(bacc.ballance)
bacc.deposit(1000)
print(bacc.ballance)
print(bacc.withdraw(500))
print(str(bacc))
print(int(bacc))
tosho = BankAccount("Te6o", 0, "$")
print(bacc.transfer_to(tosho, 100))
print(str(tosho))
print(bacc._history())
print(tosho._history())
