class BankAccount:

    def __init__(self, name, ballance, curruncy):
        self.name = name
        self.ballance = ballance
        self.curruncy = curruncy
        self.hist = []
        self.hist.append("Account was created")

    def deposit(self, suma):
        self.ballance += suma
        self.hist.append("Deposited" + str(suma) + str(self.curruncy))

    def withdraw(self, suma1):
        if(suma1 > self.ballance):
            self.hist.append("Withdraw for {}$ failed".format(suma1))
            return False
        else:
            self.hist.append("{}$ was withdrawed".format(suma1))
            self.ballance = self.ballance - suma1

            return True

    def __str__(self):
        return "Bank account for {}".format(self.name) + " with balance of {}".format(self.ballance) + "{}".format(self.curruncy)

    def balance(self):
        self.hist.append("Ballance check->{}".format(self.ballance))
        return self.ballance

    def __int__(self):
        self.hist.append("__int__check->{}".format(self.ballance))
        return self.ballance

    def transfer_to(self, account, amount):
        if self.curruncy == account.curruncy:
            if self.ballance > amount:
                self.ballance = self.ballance - amount
                account.ballance = account.ballance + amount
                self.hist.append(
                    "Transfer to" + account.name + str(amount) + account.curruncy)

                return True
            else:
                return False
        else:
            return False

    def history(self):
        return self.hist

bacc = BankAccount("Pe6o", 0, "$")
print(bacc.ballance)
bacc.deposit(1000)
print(bacc.balance())
print(bacc.withdraw(500))
print(str(bacc))
print(int(bacc))
tosho = BankAccount("Te6o", 0, "$")
print(bacc.transfer_to(tosho, 100))
print(str(tosho))
print(bacc.history())
print(tosho.history())
