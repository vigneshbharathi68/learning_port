#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#While loop

num = int(input("Enter the number: "))
sum = 0
i = 1
while i<=5:
    sum = sum + i
    i += 1
print("The sum till the given num is: ", sum)


# In[ ]:


#while loop to add digits in out given number
n = 9790058868

tot = 0

while 0<n:
    dig = n % 10 # This one took the last digit of the given num for eg. 1234 is a n it takes 4 as the value
    tot = dig + tot #adding last digit of the given number with tot and store it in tot
    n = n//10 #It removes the last digit of the given num and executes the while condition as we given
    print(tot)
    
# def add_digit():
    
#     if tot > 9:
#         print("We have a two digit numbers as result, So we added that too!!!")
#         x = tot
#         dig = x % 10
#         tot = dig + x
#         x = x//10
#         print ("Printing the total:", x)
        
    if tot>9:
        y = tot
        while y>=9:
            y = tot
            dig2 = y % 10 
            tot = dig2 + 10
            z = tot//10
#             print("given number", tot)
    

# except:
#     print("we cannot add the two digit result")
    

# finally:
#     Print("xxxxxxxx")

# def length_digit(a):
#     a = tot
#     a_string = str(a)
#     length = len(a_string)
#     return length
    


# print("The length of the result", length_digit(a)) #this will print the first digit of the number

#now took out lastdigit and add with total and store that in tot. then remove the last digit and again execute the loop.
#So that we could get the sum of the digits we given
print()
print("The sum of the given number digit is:" , tot)


# In[ ]:


#Fibonacci number using function
fib(n):
    a = 0
    b = 1
    if n==1:
        print(a)
    else:
        print(a)
        print(b)
        
        for i in range(2,n):
            c = a+b
            a=b
            b=c
            print("A is now: ",a ,"B is now: ",b)
            print(c)
            
fib(5)


# In[ ]:


#while loop to add digits in out given number
n = 9790058868

tot = 0

while 0<n:
    dig = n % 10 # This one took the last digit of the given num for eg. 1234 is a n it takes 4 as the value
    tot = dig + tot #adding last digit of the given number with tot and store it in tot
    n = n//10 #It removes the last digit of the given num and executes the while condition as we given
print(tot)


# In[ ]:




