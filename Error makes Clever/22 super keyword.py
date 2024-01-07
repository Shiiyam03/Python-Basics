class a():
    def __init__(self):
        print("A")

    def display(self):
        print("you are in class a")

class b(a):
    def display(self):
        print("you are in class b")

ob1=b()

class a():
    def __init__(self):
        print("A")

    def display(self):
        print("you are in class a")

class b(a):
    def __init__(self):
        print("B")
        
    def display(self):
        print("you are in class b")

ob1=b()

class a():
    def __init__(self):
        print("A")

    def display(self):
        print("you are in class a")

class b(a):
    def __init__(self):
        super().__init__() #super key word = use to call parent class constructor
        print("B")
        
    def display(self):
        print("you are in class b")

ob1=b()

class a():
    def __init__(self):
        print("A")

    def display(self):
        print("you are in class a")

class b():
    def __init__(self):
        super().__init__() #super key word = use to call parent class constructor
        print("B")
        
    def display(self):
        print("you are in class b")

class c(a,b):
    def __init__(self):
        super().__init__() #super key word = use to call parent class constructor
        print("C")
        
    def display(self):
        print("you are in class C")
ob1=c()
