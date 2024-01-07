def painter():
    print("painting")

painter()

def painter(msg):
    print("Message:",msg)

painter("paint my house")

#1
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

#2
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

#3
def findpassorfail(score):
    if(a>=35):
        print("Pass")
    else:
        print("fail")

a=int(input("Enter your Score:"))
findpassorfail(a)
            
#4
def printrange(num1,num2):
    for i in range(num1,num2+1):
        print(i)
num1 = int(input("Enter num1:"))
num2 = int(input("Enter num2:"))
printrange(num1,num2)

#5
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

#6
def add(n1,n2):
    return n1+n2

a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))

added=add(a,b)

output=added*c

print(output)






























