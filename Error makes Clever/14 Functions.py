def painter():
    print("painting")

painter()

def painter(msg):
    print("Message:",msg)

painter("paint my house")

""" 1.Create a function called add(), sub(), mul(), div()
And get the input for a and b inside every function then print the result. """
def add():
    print("Addition")
    a=int(input("Enter a:"))
    b=int(input("Enter b:"))
    print(a+b)

def sub():
    print("Subtraction")
    a=int(input("Enter a:"))
    b=int(input("Enter b:"))
    print(a-b)

def mult():
    print("Multiplication")
    a=int(input("Enter a:"))
    b=int(input("Enter b:"))
    print(a*b)

def div():
    print("Division")
    a=int(input("Enter a:"))
    b=int(input("Enter b:"))
    print(a/b)

add()
sub()
mult()
div()





""" 2.Get a integer number from user and pass it to the function called findevenorodd(). Let the function
print whether the number is even or odd. """
def findevenorodd(num):
    if(num%2==0):
        print("The number is even")
    else:
        print("The number is odd")

findevenorodd(5)

def findevenorodd(num):
    if(num%2==0):
        print("The number is even")
    else:
        print("The number is odd")

a=int(input("Enter a number:"))
findevenorodd(a)





""" 3.Get a integer number from user and pass it to the function called findpassorfail(). 
Let the function print whether the number is even or odd."""
def findpassorfail(score):
    if(a>=35):
        print("Pass")
    else:
        print("fail")

a=int(input("Enter your Score:"))
findpassorfail(a)





# 4.Get input for a and b and pass it to the function called printrange() let the function print numbers from a to b. """
def printrange(num1,num2):
    for i in range(num1,num2+1):
        print(i)
num1 = int(input("Enter num1:"))
num2 = int(input("Enter num2:"))
printrange(num1,num2)





""" 5.Set s_username and s_password
Get input for uname and password
Create a function called validate.
If uname and password matches the function should return true else false. """
s_username="Shiiyam"
s_password="03"

username=input("Enter username:")
password=input("Enter password:")

def validate():
    if (s_username==username and s_password==password):
        print("Correct")
    else:
        print("Wrong")
validate()

s_username="Shiiyam"
s_password="03"

username=input("Enter username:")
password=input("Enter password:")

def validate():
    if (s_username==username and s_password==password):
        return "Correct"
    else:
        return "Wrong"

a=validate()
print (a)




""" 6.(a+b)*c
Get input for a and b and function called add() which should return the sum a and b
And multiply that sum with c. """
def add(n1,n2):
    return n1+n2

a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))

added=add(a,b)

output=added*c

print(output)






























