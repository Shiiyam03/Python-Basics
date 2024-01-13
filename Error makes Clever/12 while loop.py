""" The for loop is usually used when the number of iterations is known.
    The while loop is usually used when the the number of iterations is unknown. """
i=0
while(i==0):
    print(i)
    i=i+1




# 1.Print a number from 1 to 5 using while loop.
i=int(input("Enter a Number:"))
while(i<=5):
    print (i)
    i=6

i=1
while(i<=5):
    print (i)
    i=i+1





# 2.Write a loop statement to print 10 series till 200.  
i=10
while(i%10==0) and (i<=200):
    print(i,end=",")
    i=i+10




# 3.Write a program to print first 10 natural numbers in reverse order.
i=10
while(i>0):
    print(i,end=",")
    i=i-1




# 4.Write a program to find the factorial of a number.
i=3
fact=1
while(i>0):
    fact=fact*i
    i=i-1
print (fact)

i=int(input("Enter a Number:"))
fact=1
while(i>0):
    fact=fact*i
    i=i-1
print (fact)

    
