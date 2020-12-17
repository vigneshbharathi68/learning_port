#!/usr/bin/env python
# coding: utf-8

# In[52]:


def update(a):
    print(id(a))
    a[1] = 8
    
    print(id(a))
    print("x in fun ", a)

a = [10, 11, 12]
y = update(a)
print(y)
# print("a ", a)


# In[44]:


def fibo(x):
    c = [int(i) for i in str(input_string)]
    sum1 = 0
    
    for num in c:
        print("Printing the each sum1 value ", sum1)
        sum1 += int(num)
    print(len(str(sum1)))
    print(sum1)
    
x = input("Enter the number")
fibo(x)


# In[51]:


def fibo(x):
    
    c = [int(i) for i in str(input_string)]
    sum1 = 0
    for num in c:
        print("Printing the each sum 1 value ", sum1)
        sum1 += int(num)
    print(len(str(sum1)))
    print(sum1)


try:
    
    while sum1>9:
        fibo(sum1)

    else:
        input_string = input("Enter the number::")
        fibo(input_string)

except NameError as e:
    
    print("sum1 is not defined")


# In[54]:


#function arguments

def add(a,b): #If I know no value i am going to pass to fun
    c = a + b
    print(c)
    
add(10,12)

# Output
# 22


# In[62]:


#If I dont know hom many arguments i m going to pass

def add(*a): #This is how we defined fuction without mentioning the no of arguments we r passing
    b=0
    for i in a:
        b += i
    print(b)
    
add(1,2,3,4,5,6,7,8,9)


# In[ ]:




