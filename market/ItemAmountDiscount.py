from market.entities.discount.Discount import Discount


class ItemAmountDiscount(Discount):

    __minimum = 0

    def __init__(self, percentage, amount,  minimum):
        super().__init__(percentage, amount)
        self.__minimum = minimum

    def apply(self, cashier):
        if len(cashier.getCurrentProducts()) >= self.__minimum:
            return super().apply(cashier)
        return cashier.getTotal()