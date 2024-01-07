"""#single inheritance
class dad():
    def phone(self):
        print("Dad's Phone")

class son(dad):
    def laptop(self):
        print("Son's laptop")

ram=son()
ram.phone()

#multiple inheritance
class dad():
    def phone(self):
        print("Dad's Phone")

class mom():
    def sweet(self):
        print("Mom's Sweet")

class son(dad,mom):
    def laptop(self):
        print("Son's laptop")

ram=son()
ram.phone()
ram.sweet()

#multi level inheritance
class grandpa():
    def phone(self):
        print("Grandpa's Phone")

class dad(grandpa):
    def money(self):
        print("Dad's Money")

class son(dad):
    def laptop(self):
        print("Son's Laptop")

ram = son()
ram.laptop()
ram.money()

ravi = dad()
ravi.phone()

ram.phone()

#hierarchical inheritance
class dad():
    def money(self):
        print("Dad's Money")

class son1(dad):
    pass #empty class

class son2(dad):
    pass #empty class

class son3(dad):
    pass #empty class

s2=son2()
s2.money()
"""
#hybrid inheritance
class dad():
    def money(self):
        print("Dad's Money")

class land():
    def important(self):
        print("Important Land")
        
class son1(dad,land):
    pass #empty class

class son2(dad):
    pass #empty class

class son3(dad):
    pass #empty class

s2=son2()
s2.money()







        


























