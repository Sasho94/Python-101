import unittest
from Bank import BankAccount


class BankAccountTest(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount("Rado", 0, "$")

    def test_can_create_bank_account(self):
        self.assertTrue(isinstance(self.account, BankAccount))

    def test_get_name(self):
        self.assertEqual(self.account.holder(), "Rado")

    def test_initial_zero_balance(self):
        self.assertEqual(self.account.balance(), 0)

    
    def test_deposit_in_empty_account(self):
        self.account.deposit(500)
        self.assertEqual(self.account.balance(), 500)

    def test_deposit_in_not_empty_account(self):
        account = BankAccount("Ivo", 1000, "$")
        account.deposit(500)
        self.assertEqual(account.balance(), 1500)

    def test_deposit_negative_amount(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-100)

    def test_withdraw_from_not_empty_account(self):
        self.account.deposit(100)
        result = self.account.withdraw(50)

        self.assertTrue(result)
        self.assertEqual(self.account.balance(), 50)

    def test_withdraw_from_empty_account(self):
        result = self.account.withdraw(50)

        self.assertIsNotNone(result)
        self.assertFalse(result)

    def test_history(self):
        account = BankAccount("Test", 0, "$")
        account.deposit(20)
        account.balance()
        int(account)
        expected = ["Account was created", "Deposited 20$",
                    "Balance check -> 20$", "__int__check -> 20$"]

        self.assertEqual(account.history(), expected)

if __name__ == '__main__':
    unittest.main()
