import unittest
from bill import Bill


class TestBill(unittest.TestCase):

    def setUp(self):
        self.bill = Bill(3)

    def test_bill_init(self):
        self.assertEqual(self.bill.sum)

    def test_bill_str(self):
        self.assertEqual(str(self.bill), "A 5$ bill")

    def test_bill_int(self):
        self.assertEqual(int(self.bill), 5)

    def test_bill_eq(self):
        bill1 = Bill(7)
        bill2 = Bill(3)
        self.assertNotEqual(self.bill, bill1)
        self.assertEqual(self.bill, bill2)

    if __name__=='__main__':
        unittest.main()
