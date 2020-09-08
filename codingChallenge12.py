class Computer:
    def __init__(self, size, price, core):
        self.size = size
        self.price = price
        self.core = core

    def getspecs(self):
        return self.size, self.price, self.core

    def displayspecs(self):
        print("This computer has size ", self.size, " inches")
        print("This computer is ", self.price, " dollars")
        print("This computer has ", self.core, " as core")

class Desktop(Computer):
    def __init__(self, storage, *args):
        super().__init__(*args)
        self.storage = storage

    def getspecs(self):
        return super().getspecs(), self.storage

    def displayspecs(self):
        super().displayspecs()
        print("This desktop has ", self.storage, " GB storage")

class Laptop(Computer):
    def __init__(self, weight, *args):
        super().__init__(*args)
        self.weight = weight

    def getspecs(self):
        return super().getspecs(), self.weight

    def displayspecs(self):
        super().displayspecs()
        print("This laptop is ", self.weight, " lbs")

prototype = Computer(150, 9999, "Intel 4004")
myLap = Laptop(4.23, 13, 800, "AMD 360")
myDesc = Desktop(2048, 21, 1500, "NVIDIA GEFORCE 1080")
print(prototype.getspecs())
prototype.displayspecs()
print(myLap.getspecs())
myLap.displayspecs()
print(myDesc.getspecs())
myDesc.displayspecs()
