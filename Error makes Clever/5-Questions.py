#1
mark=int(input("Type your mark:"))

if(mark>35):
    print("pass")
else:
    print("fail")

#2
income=int(input("Type your income:"))

if(income>7000):
    print("Eligible for Scholarship")
else:
    print("Not Eligible for Scholarship")

#3
a=int(input("Number:"))

if(a%3==0 and a%5==0):
    print("Number is divisible by both 3 and 5")
else:
    print("Number is not divisible by both 3 and 5")

#4
a=int(input("Number:"))

if(a%2==0):
    print("Number is even")
else:
    print("Number is odd")

#5
score=int(input("Score:"))

if(score<35):
    print("poor")
elif(score>35 and score<70):
    print("average")
elif(score>70 and score<100):
    print("goog")
else:
    print("invalid score")

#6
num1 = int(input("Enter number one:"))
num2 = int(input("Enter number two:"))
operator = input("Enter the operator +(or)-(or)*(or)/:")

if(operator == "+"):
    print(num1+num2)
elif(operator == "-"):
    print(num1-num2)
elif(operator == "*"):
    print(num1*num2)
elif(operator == "/"):
    print(num1/num2)
else:
    print("operator invalid")

#7
percentage = int(input("Enter your percentage:"))

if(percentage>=70):
    print("Eligible")
    name = input("Enter your name:")
    department = input("Enter your department:")
    location = input("Enter your location:")

    print("Your name is:",name)
    print("Your department is:",department)
    print("Your location is:",location)
    
else:
    print("Not Eligible")

#8
salary = int(input("Enter your salary:"))
age = int(input("Enter your age:"))

if(salary>=20000 or age<25):
    loan = int(input("Enter your loan amount:"))
    if(loan<=50000):
        print("You are eligible")
    else:
        print("Maximum loan amount is 50000")
else:
    print ("Not eligible")

#9
a = int(input("Tamil:"))
b = int(input("English:"))
c = int(input("Math:"))
d = int(input("science:"))
e = int(input("Social:"))
total = (a+b+c+d+e)/5
print(total)

if(total<35):
    print("Additional class is required")
else:
    print("You are good to go")
        































