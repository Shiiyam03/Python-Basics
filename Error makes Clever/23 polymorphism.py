def add(a,b,c=3):
    print(a+b+c)
add(3,22)
add(3,22,10)

#1
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
