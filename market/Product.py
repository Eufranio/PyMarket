import random


class Product:
    __code = 0
    __price = 0
    __name = ""

    def __init__(self, name, price):
        self.__name = name
        self.__price = price
        self.__code = random.randint(0, 9999)

    def setCode(self, code):
        self.__code = code

    def getCode(self):
        return self.__code

    def getPrice(self):
        return self.__price