#if-else
if(True): #True-boolean value
    print("Yes")
else:
    print("no")

if(False): #False-boolean value
    print("Yes")
else:
    print("no")





#comparison operator
print("win"=="win")
print("Win"=="win")
print("win"=="winn")





""" 1-if rcb=="win" print "Ee sala cup namde"
else print "valakam pola namaaku cup illa" """

rcb="win"
if(rcb=="win"):
    print("Ee sala cup namde")
else:
    print("valakam pola namaaku cup illa")

rcb="win"
if(rcb=="lose"):
    print("Ee sala cup namde")
else:
    print("valakam pola namaaku cup illa")





""" 2-Get user input for variable meghna, 
if meghna==died print "Surya meets Priya"
else print "Surya weds Meghna" """

meghna=input()
if(meghna=="died"):
    print("Surya meets Priya")
else:
    print("Surya weds Meghna")



meghna=input("IS MEGHNA IS ALIVE OR DEAD?")
if(meghna=="died"):
    print("Surya meets Priya")
else:
    print("Surya weds Meghna")





# 1-Get input for variable mark. If mark>35 print pass. Else print fail. 
mark=int(input("Type your mark:"))

if(mark>35):
    print("pass")
else:
    print("fail")





""" 2-Get input for variable income. If income is greater than 7000 
scholarship is availabe. Else not eligible for scholarship. """

income=int(input("Type your income:"))

if(income>7000):
    print("Eligible for Scholarship")
else:
    print("Not Eligible for Scholarship")





""" 3-Get input for a number and check whether it is divisible by both 3 and 5 or not. If yes then
print, the number is divisible by 3 and 5 else not divisible. """

a=int(input("Number:"))

if(a%3==0 and a%5==0):
    print("Number is divisible by both 3 and 5")
else:
    print("Number is not divisible by both 3 and 5")





# 4-Get input for a number and find it is even or odd. 
a=int(input("Number:"))

if(a%2==0):
    print("Number is even")
else:
    print("Number is odd")





""" 5-Get input for score out of 100.
If score is < 35 print poor.
>35 but <70 print average.
>70 print good"""
score=int(input("Score:"))

if(score<35):
    print("poor")
elif(score>35 and score<70):
    print("average")
elif(score>70 and score<100):
    print("good")
else:
    print("invalid score")





# 6-Make a mini calculator.
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





""" 7-Get a input for score percentage. Only if the percentage is greater than 70, get input for his name,
department and location. Then print you are elgible. If not print you are not elgible"""

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





""" 8-Get input for salary and age.

If salary greater than or equal to 20000 or age less than or equal to 25, get input for required
loan amount. If not print you are not elgible for loan.

If required loan amount is less than or equal to 50000 print you are eligibile for loan. if it is greater 
than 50000 print maximum loan amount is 50000."""

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





""" 9-Get input for five subject mark. Add all of it, and find average. if average mark is less than 35.
Print "Additional class is required" else print "good"."""  

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
        






























