class Rank:
    __name = ""
    __permissionLevel = 0

    def __init__(self, name, level):
        self.__name = name
        self.__permissionLevel = level

    def getLevel(self):
        return self.__permissionLevel

    def getName(self):
        return self.__name