#1
a=int(input("Enter num 1:"))
b=int(input("Enter num 2:"))
for i in range(a+1,b):
    print(i)

#2
for i in range(1,11):
    if(i%2==0):
        print(i)

#3
count=0
for i in range(1,11):
    if(i%2==0):
        count=count+1
print(count)

#4
countodd = 0
counteven = 0
for i in range(1,11):
    if(i%2==0):
        counteven = counteven+1
    else:
        countodd = countodd+1
print("Even:",counteven)
print("odd:",countodd)

#5
count = 0
for i in range(1,101):
    if(i%3==0 and i%5==0):
        count = count+1
print(count)

#6
sum=0
for i in range(1,6):
    sum=sum+i
print(sum)

#7[List(important)]
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

#8
n = int(input("Enter the number:"))
count = 0
for i in range(1,n+1):
    print(i)
    count = count+i
print(count)

#9        
n = int(input("Input number of terms:"))
for i in range(1, n + 1):
    print("Number is: " + str(i) + " and cube of " + str(i) + " is: " + str(i*i*i))


































