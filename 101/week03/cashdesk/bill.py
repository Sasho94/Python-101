class Bill:

    def __init__(self, sum):
        self.sum = sum

    def __str__(self):
        return "A {}$ Bill".format(self.sum)

    def __repr__(self):
        return str(self)

    def __int__(self):
        return int(self.sum)

    def __eq__(self, other):
        return self.sum == other.total()

    def total(self):
        return self.sum
