import random


class Employee:
    __rank = None
    __name = ""
    __id = 0

    def __init__(self, name, rank):
        self.__rank = rank
        self.__name = name
        self.__id = random.randint(0, 999)

    def getRank(self):
        return self.__rank

    def setId(self, id):
        self.__id = id

    def getName(self):
        return self.__name

    def getId(self):
        return self.__id
