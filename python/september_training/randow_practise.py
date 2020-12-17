#!/usr/bin/env python
# coding: utf-8

# In[4]:


print("hi Jupiter")


# In[11]:


#( Fibonacci number ) is the sum of the two preceding numbers. I am going to write the code to print 1 to 100 fibanacci series.
#The simplest is the series 0,1, 1, 2, 3, 5, 8, etc.

Number = int(input("\n Please Enter the range number:"))

i = 0
First_num = 0
Second_num = 1

while (i<Number):
    if(i<=1):
        Next = i
    else:
        Next = First_num + Secound_num
        First_num = Second_num
        Second_num = Next
    print(Next)
    i = i + 1


# In[2]:


# Program to display the Fibonacci sequence up to i  no of term

i = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if i <= 0:
   print("Please enter a positive integer")
elif i == 1:
   print("Fibonacci sequence upto",i,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < i:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1
#output        
#Fibonacci series
#Enter number of terms: 5
#0
#1
#1
#2
#3


# In[36]:


x = str(input("Ënter the name:"))
y = str(input("Enter the nickname:"))

print("%s is his name, %s is his nickname" %(x,y))

    #output
    #Ënter the number1:Vignesh
    #Enter the number2:Vicky
    #Vignesh is his name, Vicky is his nickname


# In[ ]:


i = int(input("Ënter i:"))
j = int(input("Enter j:"))

def add(i, j):
    return i+j
def sub(i, j):
    return i-j
def div(i, j):
    return i/j
def mul(i, j):
    return i*j

print("The addition of two number is", add(i, j))
print("The subtraction of two number is", sub(i, j))
print("The division of two number is", div(i, j))
print("The multiplication of two number is", mul(i, j))


# In[ ]:


x = lambda : a + 10

a = int(input("Enter the num:"))
print("The given number is added with 10: ", x())


# In[16]:


from time import *
from threading import *

class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)

class Hi(Thread):
    def run(self):
        for i in range(4):
            print("Hi")
            sleep(1)

t1 = Hello()
t2 = Hi()

t1.start()
sleep(0.2)
t2.start()

t1.join()
t2.join()

print("Bye")


#Output
#Hello
#Hi
#Hello
#Hi
#Hello
#Hi
#Hello
#Hi
#Hello
#Bye

