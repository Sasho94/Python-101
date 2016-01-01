import unittest
from bill import Bill
from batch_bill import BatchBill


class TestBatchBill(unittest.TestCase):

    def setUp(self):
        self.bill7 = Bill(7)
        self.bill4 = Bill(4)
        self.batch = BatchBill([self.bill7, self.bill4])

    def test_batchbill_init(self):
        self.insert(self.bill7, self.batch)
        self.insert(self.bill4, self.batch)
if __name__ == '__main__':
    unittest.main()
