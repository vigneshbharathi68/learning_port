#!/usr/bin/env python
# coding: utf-8

# In[1]:


a = 1
b = 2
print(a+b)


# In[1]:


a = 1
print(a)


# In[3]:


a = 1
print(a)


# In[4]:


str1 = "Vignesh"
str2 = "Bharathi"
print(str1[0])
print(str2[1])


# In[6]:


a = '''str1
str2
str3
'''
print(a)


# In[7]:


a = 1>2 and 0
print(a)


# In[7]:


a = 100
b = 50
if a>b:
    print("a is greater than b")
elif a==b:
    print("a and b are equal")
else:
    print("b is greater than a")


# In[10]:


str1 = 'hello-world'
print(str1[0:5])


# In[11]:


str1.find("lo")


# In[13]:


str1.replace("lo","l")


# In[14]:


splitword = "w1,w2,w3"
splitword.split(",")


# In[15]:


a = "MalayalaM"
a.count("M")


# In[16]:


a.count("l")


# In[17]:


a.count("a")


# In[18]:


print(a.count("M"))
print(a.count("a"))
print(a.count("l"))


# In[19]:


a.upper()


# In[20]:


a.lower()


# In[22]:


mytuple = ('a','b','c','d')
mytup2 = ('e','f')
mytuple+=mytup2
print(mytuple)


# In[25]:


print(mytuple*2)


# In[26]:


print(mytuple)


# In[31]:


list = ("a","b","c","d")
print(list)


# In[39]:


list = ["a","b","c"]
list1 = ["d"]
list+=list1
print(list)


# In[40]:


list.append("10")
print(list)


# In[41]:


list1 = ["x","z"]
list.append(list1)
print(list)


# In[8]:


s1 = {"a","b","c"}
s2 = {"c","d","e"}
s1 & s2


# In[10]:


s1 | s2


# In[14]:


s1 = ["a","b","c"]
s2 = {"c","d","e"}
print(s1*2)


# In[16]:


import OS
import socket
print(OS)
print(Socket)


# In[17]:


a = [1,2,3]
x,y,z=a
print(x)


# In[18]:


print(y)


# In[19]:


print(z)


# In[3]:


def my_function(c):
       return c
       pass


# In[4]:


p = my_function(6)
print(p)


# In[7]:


p = my_function(6)
p.my_function()


# In[15]:


class Person:
    def _init_(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hi my name is " + self.name)

p1 = Person("Vignesh", 24)
p1.myfunc()


# In[20]:


class Computer:
    def config(self):
        print('i5, 1TB HDD, 16gb Ram')

#creating object of the class 
com1 = Computer()
com2 = Computer()

#Using com1 instead of class name to call and print the function's output
com1.config()
com2.config()

#Using class name and passing the function
Computer.config(com1)

a = 5
    def _length_


# In[27]:


class Computer:
    def _init_(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("Config is ", self.cpu, self.ram)

com1 = Computer('i5', 8)
com2 = Computer('i5', 16)

com1.config()
com2.config()


# In[ ]:




