#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Operator overloading

class Book:
    
    def __init__(self, price):
        self.price = price
        
book1 = Book(10) #Instance Object one
book2 = Book(20) #Instance Object two

total_price = book1 + book2 #We cannot add two objects

print(total_price) 

#Output
# typeError                                 Traceback (most recent call last)
# <ipython-input-1-6ffbd851cf91> in <module>
#       8 book2 = Book(20)
#       9 
# ---> 10 total_price = book1 + book2
#      11 
#      12 print(total_price)

# TypeError: unsupported operand type(s) for +: 'Book' and 'Book'


# In[ ]:


class Book:
    
    def __init__(self, price):
        self.price = price
        
    def __add__(self, other):
        return self.price + other.price
        
book1 = Book(10) #Instance Object one
book2 = Book(20) #Instance Object two

compare = book1.price < book2.price #We are passing price argument so we can get the output

# total_price = book1 + book2 #We cannot add two objects

print(compare) 

# Output
# True


# In[2]:


class Book:
    
    def __init__(self, price):
        self.price = price
        
    def __add__(self, other):
        return self.price + other.price
        
book1 = Book(10) #Instance Object one
book2 = Book(20) #Instance Object two


compare = book1.price < book2.price #You can see the difference while comparing below object
total_price = book1 + book2 #We defined two objects with there we passing the price to functions

print(total_price)
print(compare)

# Output
# 30
# True


# In[3]:


class Book:
    
    def __init__(self, price):
        self.price = price
        
    def __add__(self, other):
        return self.price + other.price
    
    def __lt__(self, other):
        return self.price < other.price
        
book1 = Book(10) #Instance Object one
book2 = Book(20) #Instance Object two


compare = book1 > book2 
total_price = book1 + book2 

print(total_price)
print(compare)


# In[4]:


#fibonacci seires 0,1,1,2,3,5,8,13

n1 = 0 #The first two numbers
n2 = 1
f = [n1,n2]

#Using while loop for this sequence

i = 1        #Initaiting the sequence
while i < 8: #I want to print 7 numbers continue with n1 and n2.
    f.append(i) #Here appending to list f 
    i += 1
    
print(f)

# Output
# [0, 1, 1, 2, 3, 4, 5, 6, 7]


# In[5]:


n1 = 0 #The first two numbers
n2 = 1
f = [n1,n2]

#Using while loop for this sequence

i = 1        #Initaiting the sequence
while i < 8: #I want to print 7 numbers continue with n1 and n2.
    f.append(n1+n2) #Its appending to n1+n2 7 times and adding the result in list f 
    i += 1
    
print(f)

# So the output will be 
# [0, 1, 1, 1, 1, 1, 1, 1, 1]


# In[6]:


n1 = 0 #The first two numbers
n2 = 1
f = [n1,n2]

#Using while loop for this sequence

i = 1        #Initaiting the while loop
while i < 8: #I want to print 7 numbers continue with n1 and n2.
    n3 = n1 + n2 #I am storing the values n1 + n2 into n3
    f.append(n3) #Its appending n3 to list and adding the result in list f 
    n1 = n2 #Changing the values. Actually incrementing the preciding values
    n2 = n3
    print("n1 is",n1 , "n2 is", n2)
    
    i += 1
    
    
    
    
print(f)

# Output
# n1 is 1 n2 is  1
# n1 is 1 n2 is  2
# n1 is 2 n2 is  3
# n1 is 3 n2 is  5
# n1 is 5 n2 is  8
# n1 is 8 n2 is  13
# n1 is 13 n2 is  21
# [0, 1, 1, 2, 3, 5, 8, 13, 21]


# In[7]:


n1 = 0 #The first two numbers
n2 = 1
f = [n1,n2]

#Using for loop for this sequence

for i in range(1, 8): #I want to print 7 numbers appending with n1 and n2.
    n3 = n1 + n2 #I am storing the values n1 + n2 into n3
    f.append(n3) #Its appending n3 to list and adding the result in list f 
    n1 = n2 #Changing the values. Actually incrementing the preciding values
    n2 = n3
    print("n1 is",n1 , "n2 is", n2)
    
print(f)


# In[8]:


# create 10 rows
#print * for 10 rows
#print * as the number of rows which means row 2 should have 2 start

#Using for loop
for i in range(1,11): #So that we can get 1 to 10
    for j in range(0,i):
        print("*", end = " ")
        
    print("\r")
    
# Output
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * * * 
# * * * * * * * 
# * * * * * * * * 
# * * * * * * * * * 
# * * * * * * * * * * 


# In[9]:


#Using while loop
i = 1
while i<=10:
    j = 1
    while j<=i:
        print('*' , end = ' ')
        j+=1
    print("\r")
    i+=1
    


# In[10]:


n = 10
for i in range(1,n+1):
    for j in range(0,n):
        print(" ", end = " ")
    n-=1
    for k in range(0,i):
        print(" *  ", end = "")
    
    print("\r") #Empty rows


# In[14]:


n = 10
for i in range(1,n+1):
    for j in range(0,n):
        print("", end = "") #Without putting space here which means its a empty one
    n-=1
    for k in range(0,i): #So this one only executing
        print("* ", end = "")
    
    print("\r") #Empty rows

    
# Output
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * * * 
# * * * * * * * 
# * * * * * * * * 
# * * * * * * * * * 
# * * * * * * * * * * 


# In[25]:


str1='ABCD'
str2='PQR'
for i in range(4):
     print(str1[ :i +1 ] + str2[ i: ])


# In[ ]:




