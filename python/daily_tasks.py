#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Python program to know the area of the circle
#As we know area of circle is the multiplication of pi, squares of r
#this was my solution

pi = 3.14
r = int(input("Enter the radius to find the area of circle:"))

square_r = r * r

print("The square root of the given radius",r,"is",pi * square_r)

# Output
# Enter the radius to find the area of circle:5
# The suare root of the given radius 5 is 78.5


# In[10]:


#Using import method to print the area of the circle

from math import pi
r = float(input("Enter the radius :"))
print("The area of the circle for the radius " +str(r)+" is:",str(pi*r**2))

# output
# Enter the radius :1.1
# The area of the circle for the radius 1.1 is: 3.8013271108436504


# In[24]:


#This is my solution
#Write a Python program which accepts the user's first and last name and 
#print them in reverse order with a space between them

n = int(input("Enter How many number of names you want to print:"))

# f_l = first_name
# l_1 = last_name
f=[]
for i in range(0,n):
    
    first_name = input("Enter the first name:")
    last_name = input("Enter the last name:")
    f.append(last_name)
    f.append(first_name)
    
    
for j in f:
    print(j)

# # print(l_1,f_1)
# print(f)
    
print("Bye")

# Output
# Enter How many number of names you want to print:1
# Enter the first name:Vignesh
# Enter the last name:Bharathi
# Bharathi
# Vignesh
# Bye


# In[ ]:


#Sum of the digits 
input_string = input("Enter the number::")
c = [int(i) for i in str(input_string)]
sum1 = 0
for num in c:
    sum1 += int(num)
print(len(str(sum1)))
print(sum1)


# In[ ]:


#Write a Python program which accepts a sequence of comma-separated numbers from user and 
#generate a list and a tuple with those numbers

value = input("Enter the values with ',' :")

list = value.split(',')
tuple = tuple(list)

print(list)


# In[10]:


# Given a two integer numbers return their product and  
# If the product is greater than 1000, then return their sum

a = 50
b = 20
c = a*b
# print(c)

if c>1000:
    print(a+b)
else:
    print(a*b)

    
# This one is my solution


# In[13]:


#Using function

def mul_sum(a,b):
    product = a * b
    if product <= 1000:
        return product
    else:
        return a + b
    
a = int(input("Enter a:"))
b = int(input("Enter b:"))

result = mul_sum(a,b)
print("The result is :", result)

# Output
# Enter a:10
# Enter b:10
# The result is : 100


# In[ ]:


# Question 2: Given a range of first 10 numbers, 
# Iterate from start number to the end number and print the sum of the current number and previous number

