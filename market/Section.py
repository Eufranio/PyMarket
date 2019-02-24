import random
class Section:
    __products = list()
    __name = ""
    __code = 0

    def __init__(self, name):
        self.__code = random.randint(0, 99)
        self.__name = name

    def addProduct(self, product):
        if product in self.__products:
            return "Essa seção já possui este produto"
        else:
            self.__products.append(product)

    def getProducts(self):
        return self.__products

    def getProduct(self, id):
        for x in self.__products:
            if id == x.getCode():
                return x
        return "Esse produto não está cadastrada nesta seção"

    def removeProduct(self, product):
        if product in self.__products:
            self.__products.remove(product)
        else:
            return "Esse produto não existe nessa seção"


    def getName(self):
        return self.__name

