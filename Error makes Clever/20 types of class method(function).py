#instant method
class laptop():
    chargertype="C Type"

    def __init__(self):
        self.brand=""
        self.price=34

    def setPrice(self,price):
        self.price=price

    def getPrice(self):
        print(self.price)

hp=laptop()
hp.getPrice()

hp.setPrice(20000)
hp.getPrice()

#class method
class laptop():
    chargertype="C Type"

    def __init__(self):
        self.brand=""
        self.price=34

    def setPrice(self,price):
        self.price=price

    def getPrice(self):
        print(self.price)

    def changeChargerType(cls):
        cls.chargertype="B TYPE"
        print("Charger type changed to B")

hp=laptop()
hp.setPrice(20000)
hp.getPrice()

laptop.changeChargerType(laptop)

class laptop():
    chargertype="C Type"

    def __init__(self):
        self.brand=""
        self.price=34

    def setPrice(self,price):
        self.price=price

    def getPrice(self):
        print(self.price)
        
    @classmethod #decorator
    def changeChargerType(cls):
        cls.chargertype="B TYPE"
        print("Charger type changed to B")

hp=laptop()
hp.setPrice(20000)
hp.getPrice()

laptop.changeChargerType()

#static method
class laptop():
    chargertype="C Type"

    def __init__(self):
        self.brand=""
        self.price=34

    def setPrice(self,price):
        self.price=price

    def getPrice(self):
        print(self.price)
        
    @classmethod #decorator
    def changeChargerType(cls):
        cls.chargertype="B TYPE"
        print("Charger type changed to B")

    @staticmethod #decorator
    def info():
        print("This is laptop class")
        
hp=laptop()
hp.setPrice(20000)
hp.getPrice()

laptop.changeChargerType()

hp.info()

























