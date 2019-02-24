from market.Storage import Storage
from market.FileStorage import FileStorage


class Main:
    __instance = None

    __storage = None
    __name = ""
    __phone = ""
    __address = ""
    __site = ""

    def __init__(self):
        self.__storage = Storage(FileStorage())
        Main.__instance = self

    @staticmethod
    def getInstance():
        return Main.__instance

    def getStorage(self):
        return self.__storage

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def getPhone(self):
        return self.__phone

    def getAdress(self):
        return self.__address

    def getSite(self):
        return self.__site

    def setPhone(self, phone):
        self.__phone = phone

    def setAddress(self, address):
        self.__address = address

    def setSite(self, site):
        self.__site = site