class Discount:
    __percentage = False
    __amount = 0.0

    def __init__(self, percentage, amount):
        self.__percentage = percentage
        self.__amount = amount

    def apply(self, cashier):
        return self.applyTotal(cashier.getTotal())

    def applyTotal(self, total):
        if self.__percentage:
            return total * (1 - (self.__amount/100))
        else:
            return total - self.__amount