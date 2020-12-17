#!/usr/bin/env python
# coding: utf-8

# In[5]:


#numpy, 2d array
#In array package we can only work with single diminsional array. That's where numpy comes into picture

#But numpy is not a defalt package we should install it externally
#We use pip to install it
#We should go to command prompt to install it
get_ipython().system('pip install numpy')


# In[13]:



x = int(input("Please enter the number to print"))

def greet(x):
    if x==1:
        print("xxxx")
    else:
        print("Please give 1 to print")


g1 = greet()
g1.greet(x)


# In[20]:


#Fibonacci number using function
def fib(n):
    
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
            print("\n",c,"\n")
            
fib(10)


# In[55]:


#while loop to add digits in out given number
n = int(input("Enter the number to print the value: "))
t1 = n
tot = 0

while 0<n:
    dig = n % 10 # This one took the last digit of the given num for eg. 1234 is a n it takes 4 as the value
    tot = dig + tot #adding last digit of the given number with tot and store it in tot
    n = n//10 #It removes the last digit of the given num and executes the while condition as we given
# print(tot,"is not a single digit number, So again we summing the digits")

if tot<=9:
    print(tot)

else:
    tot_1 = tot
    tot_2 = 0

    while 0<tot_1:
        dig = tot_1 % 10 # This one took the last digit of the given num for eg. 1234 is a n it takes 4 as the value
        tot_2 = dig + tot_2 #adding last digit of the given number with tot and store it in tot
        tot_1 = tot_1//10 #It removes the last digit of the given num and executes the while condition as we given
    print("Sum of the digits of ",t1,"is",tot_2)

#Output
# Enter the number to print the value: 979588
# 46 is not a single digit number, So again we summing the digits
# Sum of the digits of  979588 is 10

