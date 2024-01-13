def add(a,b,c=3):
    print(a+b+c)
add(3,22)
add(3,22,10)

""" 1. Create a class called aninmal with a method sound() that prints "Animals makes a sound."
Create a derived class called Dog that inherits from Animal and overrides the sound() method
to print "Dog Barks". Create another derived class called Bird that inherits from animal 
and overrides the sound() method to print "Birds Sing.". """
class animal():
    def sound(self):
        print("Animal makes a sound")

class Dog(animal):
    def sound(self):
        print("Dog Barks")

class Bird(animal):
    def sound(self):
        print("Birds Sings")

d1=Bird()
d1.sound()
