""" 1.Create a base class called shape with a method area() that returns 0. Create a derived class
called rectangle that inherits from shape and overrides the area() method to calculate
and return the area of a rectangle."""
class shape():
    def area(self):
        return 0
class rectangle(shape):
    def area(self):
        l=3
        b=22
        print(l*b)

r1=rectangle()
r1.area()




""" 2.create a base class called person with a constructor that takes a name as a parameter.
create a derived class called student that inherits from person and has a constructor
that takes a parameter calles grade. Write a method in student to display the namer and"""
class person():
    def __init__(self,name):
        self.name=name

class student(person):
    def __init__(self,name,grade):
        super().__init__(name)
        self.grade=grade
        
    def display(self):
        print(self.name)
        print(self.grade)

s1=student("shiiyam","C")
s1.display()



""" 3.Create a base class called vechile with a method start() that prints "Vechile started."
create a derived class called car that inherits from vechile and overrides the start() method 
to print "Car started". """



"""4.Create a base class called Employee with properties name and salary.
Create a derived class calles Manager that inherits from employee and
adds a property department. Write a method in manager to display the
name, salary, and department of the manager"""
class employee():
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        
class manager(employee):
    def department(self,department):
        super().__init__(self.name,self.salary)
        self.department=department
    def display(self):
        print(self.name,self.salary,self.department)

e1=manager("shiiyam","70000",)
e1.department("CST")
e1.display()

