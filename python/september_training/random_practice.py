#!/usr/bin/env python
# coding: utf-8

# In[1]:
#Addede new 

def tri_recursion(k):
    if (k>0):
#         print("printing k: ",k)
        result = k + tri_recursion(k-1)
        print("Printing tri recursion of k -2: ",tri_recursion(k-2))
        print("printing the result: ",result)
    else:
        result = 0
    return result

print("Tri Recusrion of the given number:")

tri_recursion(3)


# In[ ]:


# without passing any arguments to the function
def my_func():
    return lambda a: a*2

my_doubler = my_func() #Assigning the value for n throuh variable
my_tripler = my_func()

x = int(input("Enter the number to double and triple: "))
print("The doubler of the given number is : ",my_doubler(x))
print("The tripler of the given number is : ",my_tripler(x))

# Output
# Enter the number to double and triple: 11
# The doubler of the given number is :  22
# The tripler of the given number is :  22


# In[40]:


# Passing arguments to the function
def my_func(n):
    return lambda a: a*n

my_doubler = my_func(2) #Assigning the value for n throuh variable
my_tripler = my_func(3)

x = int(input("Enter the number to double and triple: "))
print("The doubler of the given number is : ",my_doubler(x))
print("The tripler of the given number is : ",my_tripler(x))

# Output
# Enter the number to double and triple: 11
# The doubler of the given number is :  22
# The tripler of the given number is :  33


# In[44]:





# In[47]:


#Dictionary
d = dict()
print(d)
d["xyz"] = 1
d["abc"] = 2
d["qwe"] = 3
print(d.values())


# In[8]:


#Variable
a = int(input("Enter A: "))
b = int(input("Enter B: "))

def fun(a,b):
    if a>b:
        return a//b
    
        try:
            print(a/b)

        except ZeroDivisionError as e:
            print("we cannot divide any number by zero")

        
   
    #elif a==b:
#         return 1
    else:
        print ("invalit input")
        
fun(a,b)
    


# In[9]:


print(__name__)


# In[14]:


import Calc

print("Demo says: ", __name__)


# In[13]:


import Calc

print("demo says: " + __main__)


# In[22]:


class Computer:
    def config(self): #As I understand self saying that arguments has his own in this defined function,
                        #So we don't need to pass any argument value while calling the function.
        print("i5, 4GB, 1TB")
        
com1 = Computer()

com1.config()


# In[ ]:


def fibo(n):
    n1 = 0
    n2 = 1
    f = [0, 1]
    while n>0:
        
        n1 = n2
        n2 = n1
        


# In[ ]:


try:
    age=int(input('Enter your age: '))
except:
    print ('You have entered an invalid value.')
else:
    if age <= 21:
        print('You are not allowed to enter, you are too young.')
    else:
        print('Welcome, you are old enough.')


# In[ ]:




