class BankAccount:

    def __init__(self, name, ballance, curruncy):
        self.name = name
        self.ballance = ballance
        self.curruncy = curruncy
        self.hist = []
        self.hist.append("Account was created")

    def deposit(self, suma):
        if suma < 0:
                raise ValueError("Cannot deposit negative money")
        self.ballance += suma
        self.hist.append("Deposited {}{}".format(suma, self.curruncy))

    def withdraw(self, suma1):
        if((suma1 > self.ballance)and (suma1 > 0)):
            self.hist.append(
                "Withdraw for {}{} failed".format(suma1, self.curruncy))
            return False
        else:
            self.hist.append("{}$ was withdrawed".format(suma1))
            self.ballance = self.ballance - suma1

            return True

    def holder(self):
        return self.name

    def __str__(self):
        return "Bank account for {}".format(self.name) + " with balance of {}".format(self.ballance) + "{}".format(self.curruncy)

    def balance(self):
        self.hist.append(
            "Balance check -> {}{}".format(self.ballance, self.curruncy))
        return self.ballance

    def __int__(self):
        self.hist.append(
            "__int__check -> {}{}".format(self.ballance, self.curruncy))
        return self.ballance

    def transfer_to(self, account, amount):
        if self.curruncy == account.curruncy:
            if self.ballance > amount:
                self.ballance = self.ballance - amount
                account.ballance = account.ballance + amount
                self.hist.append(
                    "Transfer to{} {}{}".format(account.name, amount, account.curruncy))

                return True
            else:
                return False
        else:
            return False

    def history(self):
        return self.hist
