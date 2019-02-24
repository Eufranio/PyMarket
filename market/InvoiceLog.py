from market import Main
import random

class InvoiceLog:
    __contents = list()
    __id = 0

    def __init__(self, contents):
        self.__contents = contents
        self.__id = random.randint(0, 999)

    def __init__(self, products, discount, total):
        self.__id = random.randint(0, 999)
        self.__contents.append("========================================")
        self.__contents.append(Main.getInstance().getName() + " - " + Main.getInstance().getSite())
        self.__contents.append(Main.getInstance().getAdress() + " - " + Main.getInstance().getPhone())
        self.__contents.append("========================================")
        self.__contents.append("Descrição das compras:")
        self.__contents.append(" ")
        for x in products:
            self.__contents.append("(cod " + str(x.getCode()) + ") - " + x.getName() + " - " + str(x.getPrice()))
        self.__contents.append("========================================")
        self.__contents.append("Desconto: R$" + str(discount))
        self.__contents.append("Total: R$" + str(total))
        self.__contents.append("========================================")

    def setId(self, id):
        self.__id = id

    def getId(self):
        return self.__id

    def getContents(self):
        return self.__contents