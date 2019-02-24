from market.entities.discount.Discount import Discount


class SectionDiscount(Discount):
    __section = None

    def __init__(self, percentage, amount, section):
        super().__init__(percentage, amount)
        self.__section = section

    def apply(self, cashier):
        total = cashier.getTotal()
        for x in cashier.getCurrentProducts():
            if x in self.__section.getProducts():
                total -= super().applyTotal(x.getPrice())
        return cashier.getTotal() - total
