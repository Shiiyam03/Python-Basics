#for loop
for i in "apple":
    print(i)





#range function
for i in range(5):
    print(i)

for i in range(1,4):
    print(i)





#Print 2 table
for i in range(1,11):
    print(i*2)

for i in range(1,11):
    print(i,"x2=",i*2)





#list variables
a=[]
for i in range(10):
    num=int(input())
    a.append(num)
print(a)





""" 1.Get input for number a and b
print the number between a and b """

a=int(input("Enter num 1:"))
b=int(input("Enter num 2:"))
for i in range(a+1,b):
    print(i)





""" 2.Print even number between 1 to 10 """

for i in range(1,11):
    if(i%2==0):
        print(i)





""" 3.Count the number of odd numbers between 1 to 10 """
count=0
for i in range(1,11):
    if(i%2==0):
        count=count+1
print(count)




""" 4.Count the number of odd and even numbers between 1 to 10 and print it. """
countodd = 0
counteven = 0
for i in range(1,11):
    if(i%2==0):
        counteven = counteven+1
    else:
        countodd = countodd+1
print("Even:",counteven)
print("odd:",countodd)




#5 Count the number which are divisible by 3 and 5. Range 1 - 100
count = 0
for i in range(1,101):
    if(i%3==0 and i%5==0):
        count = count+1
print(count)




#6 Write a program to compute the sum of the first 5 natural numbers
sum=0
for i in range(1,6):
    sum=sum+i
print(sum)




#7 Write a program to read 10 numbers from the keyboard and find their sum and average. [List(important)]
a=[]
for i in range(10):
    num=int(input("Enter num"+str(i+1)))
    a.append(num)
print(a)

sum=0
for i in a:
    sum=sum+int(i)
print(sum)
print(sum/10)





#8 Write a program to display n terms of natural numbers and their sum.
n = int(input("Enter the number:"))
count = 0
for i in range(1,n+1):
    print(i)
    count = count+i
print(count)




#9 Write a program to display the cube of the number up to an integer.       
n = int(input("Input number of terms:"))
for i in range(1, n + 1):
    print("Number is: " + str(i) + " and cube of " + str(i) + " is: " + str(i*i*i))


































