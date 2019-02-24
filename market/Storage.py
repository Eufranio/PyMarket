class Storage:
    __sections = list()
    __logs = list()
    __employees = list()
    __ranks = list()
    __products = dict()
    __discount = None
    __database = None

    def __init__(self, database):
        self.__database = database

    def registerProduct(self, product, amount = 1):
        if product.getCode() in self.__products.keys():
            self.__products[product.getCode()] += amount
        else:
            self.__products[product.getCode()] = amount

    def withdrawProduct(self, product, amount = 1):
        if product.getCode() in self.__products.keys():
            current = self.__products[product.getCode()]
            if amount >= current:
                self.__products[product.getCode()] = 0
            else:
                self.__products[product.getCode()] -= amount
        else:
            return "Este produto não está cadastrado no estoque"

    def addProduct(self, product, sectionName):
        section = self.getSection(sectionName)
        if section is None:
            return "Esta seção não está cadastrada"
        return section.addProduct(product)

    def removeProduct(self,product, sectionName):
        section = self.getSection(sectionName)
        if section is not None:
            return section.remove(product)
        return "Este produto não está cadastrado nessa seção"

    def addSection(self, section):
        if section in self.__sections:
            return "Esta seção já está cadastrada"
        self.__sections.append(section)

    def removeSection(self, sectionName):
        section = self.getSection(sectionName)
        if section not in self.__sections:
            return "Esta seção não está cadastrada"
        self.__sections.remove(section)

    def getSection(self, sectionName):
        for x in self.__sections:
            if x.getName() == sectionName:
                return x

    def getDiscount(self):
        return self.__discount

    def setCurrentDiscount(self, currentDiscount):
        self.__discount = currentDiscount

    def getLogs(self):
        return self.__logs

    def getEmployees(self):
        return self.__employees

    def getProduct(self, id):
        for x in self.__sections:
            for y in x.getProducts():
                if id == y.getCode():
                    return y
        return "Este produto não foi encontrado"

    def addLog(self, log):
        self.__logs.append(log)

    def addRank(self, rank):
        self.__ranks.append(rank)

    def getRank(self, name):
        for x in self.__ranks:
            if x.getName() == name:
                return x

    def getRanks(self):
        return self.__ranks

    def addProductEntry(self, id, amount):
        self.__products[id] = amount

    def getEntries(self):
        return self.__products

    def reset(self):
        self.__sections.clear()
        self.__logs.clear()
        self.__employees.clear()
        self.__products.clear()
        self.__ranks.clear()

