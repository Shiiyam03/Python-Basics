#instant variable
class phone():
    def __init__(self,brand,price,charger):
        self.brand=brand
        self.price=price
        self.charger=charger
    def display(self):
        print("Brand:",self.brand)
        print("Price:",self.price)
        print("Charger:",self.charger)

samsung = phone("samsung","100000","B-type")
samsung.display()

#class variable
class phone():
    chargertype="C-type"
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def display(self):
        print("Brand:",self.brand)
        print("Price:",self.price)
        print("Charger:",self.chargertype)

samsung = phone("samsung","100000")
samsung.display()

google = phone("pixel","60000")
google.display()

oneplus = phone("oneplus","70000")
oneplus.display()

class phone():
    chargertype="C-type"
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def display(self):
        print("Brand:",self.brand)
        print("Price:",self.price)
        print("Charger:",self.chargertype)

phone.chargertype="B-type"

samsung = phone("samsung","100000")
samsung.display()

google = phone("pixel","60000")
google.display()

oneplus = phone("oneplus","70000")
oneplus.display()
