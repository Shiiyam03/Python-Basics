class laptop:
    def __init__(self):
        print("demo")
    def display(self):
        print("display")

hp=laptop()

class laptop:
    def __init__(self):
        self.price=0
        self.ram=""
        self.processor=""
    def display(self):
        print("display")

hp=laptop()
hp.price=75000
hp.ram="16gb"
hp.processor="i9"
print(hp.processor)

class laptop:
    def __init__(self):
        self.ram=""
        self.processor=""
    def display(self):
        print("Ram:",self.ram)
        print("Processor:",self.processor)

hp=laptop()
dell=laptop()

hp.ram="16gb"
hp.processor="i9"

dell.ram="8gb"
dell.processor="i7"

hp.display()
dell.display()

class laptop:
    pass




""" 1.Create a class called student
create a variable = name and register number using constructor.
Create a function called display which should display the name and register number of the student."""
class student:
    def __init__(self):
        self.name=""
        self.register=""
    def display(self):
        print("Name:",self.name)
        print("RegNo:",self.register)

shiiyam=student()
viimal=student()

shiiyam.name="Shiyam R"
shiiyam.register="713321TS047"

viimal.name="Vimal R"
viimal.register="713321TS055"

shiiyam.display()
viimal.display()




""" 2.Create a class called fruit
Create a variable called colour using __init__ method
Create a object called apple "Pass the colour variable as a parameter through object". """
class fruit:
    def __init__(self,col):
        self.color="black"
        
apple=fruit("red")
print(apple.color)




""" 3.Create a class teacher 
Create a variable = name and register number using constructor
Create a function called display which should display the name and register number of the teacher
Create t1 and t2 object and pass the name and reg no value through object. """
class teacher:
    def __init__(self,name,reg):
        self.name=name
        self.register=reg
    def display(self):
        print("Name:",self.name)
        print("RegNo:",self.register)

t1=teacher("Shiyam","47")
t2=teacher("Vimal","55")

t1.display()
t2.display()




""" 4.Create  a class called calcuator
Create 2 varoiable a and b
Create a function called add, sub, mul, div all functions should take 2 variables as parameter.
Pass a and b value through object()."""
class calculator:
    def __init__(self,num1,num2):
        self.a=num1
        self.b=num2
        
    def add(self):
        plus=int(self.a)+int(self.b)
        print("Addition:",plus)

    def sub(self):
        plus=int(self.a)-int(self.b)
        print("Subtraction:",plus)

    def mul(self):
        plus=int(self.a)*int(self.b)
        print("Multiplication:",plus)
        
    def div(self):
        plus=int(self.a)/int(self.b)
        print("division:",plus)
        
num=calculator(3,22)

num.add()
num.sub()
num.mul()
num.div()

class calculator:
    def __init__(self,num1,num2):
        self.a=num1
        self.b=num2
        
    def add(self):
        print("Addition:",self.a+self.b)

num=calculator(3,22)

num.add()















