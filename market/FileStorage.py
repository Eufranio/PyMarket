from os import listdir
from os.path import isdir, isfile, join
from market.Section import Section
from market.Product import Product
from market.InvoiceLog import InvoiceLog
from market.Rank import Rank
from market.Employee import Employee
from market.Main import Main

class FileStorage:

    def fill(self):
        Main.getInstance().getStorage().reset()

        sectionsPath = "/sections"
        sections = [f for f in listdir(sectionsPath) if isdir(join(sectionsPath, f))]
        for sectionName in sections:

            section = Section(sectionName)
            Main.getInstance().getStorage().addSection(section)

            sectionDir = join(sectionsPath, sectionName)
            products = [f for f in listdir(sectionsPath) if isfile(join(sectionDir, f))]

            for productName in products:
                f = open(join(sectionDir, productName), 'r')
                code, price, name = f.readlines()
                product = Product(name, int(price))
                product.setCode(int(code))
                Main.getInstance().getStorage().addProduct(product, sectionName)
                f.close()

        logsPath = "/logs"
        logs = [f for f in listdir(logsPath) if isdir(join(logsPath, f))]
        for logName in logs:
            f = open(join(logsPath, logName), 'r')
            lines = f.readlines()
            id = int(lines[0])
            del lines[0]
            log = InvoiceLog(lines)
            log.setId(id)
            Main.getInstance().getStorage().addLog(log)
            f.close()

        ranksPath = "/ranks"
        ranks = [f for f in listdir(ranksPath) if isdir(join(ranksPath, f))]
        for rankName in ranks:
            f = open(join(ranksPath, rankName), 'r')
            name, level = f.readlines()
            rank = Rank(name, int(level))
            Main.getInstance().getStorage().addRank(rank)
            f.close()

        employeesPath = "/employees"
        employees = [f for f in listdir(employeesPath) if isdir(join(employeesPath, f))]
        for employeeName in employees:
            f = open(join(employeesPath, employeeName), 'r')
            rank, name, id = f.readlines()
            employee = Employee(name, Main.getInstance().getStorage().getRank(rank))
            employee.setId(int(id))
            Main.getInstance().getStorage().addEmployee(employee)
            f.close()

        storagePath = "/storage"
        storageEntries = [f for f in listdir(storagePath) if isdir(join(storagePath, f))]
        for entryName in storageEntries:
            f = open(join(storagePath, entryName), 'r')
            id, amount = f.readlines()
            Main.getInstance().getStorage().addProductEntry(int(id), int(amount))
            f.close()

    def save(self):
        sectionsPath = "/sections"
        for section in Main.getInstance().getStorage().getSections():
            for product in section.getProducts():
                f = open(join(sectionsPath, section, product.getName() + ".txt"), 'w')
                f.write(str(product.getCode()))
                f.write(str(product.getPrice()))
                f.write(product.getName())
                f.close()

        logsPath = "/logs"
        for log in Main.getInstance().getStorage().getLogs():
            f = open(join(logsPath, str(log.getId()) + ".txt"), 'w')
            f.write(str(log.getId()))
            f.writelines(log.getContents())
            f.close()

        ranksPath = "/ranks"
        for rank in Main.getInstance().getStorage().getRanks():
            f = open(join(ranksPath, rank.getName() + ".txt"), 'w')
            f.write(rank.getName())
            f.write(str(rank.getLevel()))
            f.close()

        employeesPath = "/employees"
        for employee in Main.getInstance().getStorage().getEmployees():
            f = open(join(employeesPath, str(employee.getId()) + ".txt"), 'w')
            f.write(employee.getRank().getName())
            f.write(employee.getName())
            f.write(str(employee.getId()))
            f.close()

        storagePath = "/storage"
        for product, amount in Main.getInstance().getStorage().getEntries().items():
            f = open(join(storagePath, str(product.getCode()) + ".txt"), 'w')
            f.write(str(product.getCode()))
            f.write(str(amount))
            f.close()