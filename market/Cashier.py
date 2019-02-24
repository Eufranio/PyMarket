from market.entities.CashRegister import CashRegister
from market.Main import Main
from market.entities.Product import Product
from market.entities.logging.InvoiceLog import InvoiceLog


class Cashier:
    __operator = None
    __products = list()
    __cashRegister = None

    def __init__(self, operator):
        self.__operator = operator
        self.__cashRegister = CashRegister()

    def getTotal(self):
        total = 0
        for x in self.__products:
            total += x.getPrice()
        return total

    def getCurrentProducts(self):
        return self.__products

    def applyDiscounts(self):
        discount = Main.getInstance().getStorage().getDiscount()
        return discount.apply(self)

    def processProduct(self, id):
        product = Main.getInstance().getStorage().getProduct(id)
        if isinstance(product, Product):
            self.__products.append(product)
        else:
            return product

    def confirmShopping(self):
        currentValue = self.applyDiscounts()
        discount = self.getTotal() - currentValue
        log = InvoiceLog(self.__products, discount, currentValue)
        Main.getInstance().getStorage().addLog(log)

        for x in self.__products:
            Main.getInstance().getStorage().withdrawProduct(x)
        self.__products.clear()

    def cancelProduct(self, id):
        if self.__operator.getRank().getLevel() >= 2:
            for x in self.__products:
                if x.getCode() == id:
                    self.__products.remove(x)
        else:
            return "Você não possui o nível de permissão para realizar esta operação"

    def cancelShopping(self):
        if self.__operator.getRank().getLevel() >= 2:
            self.__products.clear()
        else:
            return "Você não possui o nível de permissão para realizar esta operação"

    def changeOperator(self, operator):
        self.__operator = operator