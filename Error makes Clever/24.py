#1
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

#2
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

#3

#4
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

