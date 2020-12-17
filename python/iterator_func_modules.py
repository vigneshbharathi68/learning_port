#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Iterator
# Return an iterator from a tuple, and print each value:

mytuple = ("Vignesh", "Sitharthan", "Baskaran")

myit = iter(mytuple)

print(myit) # <tuple_iterator object at 0x05E57FB0>

print(next(myit), next(myit), next(myit)) # It will print in a order
# Output
# Vignesh Sitharthan Baskaran


# In[4]:


# We can also use a for loop to iterate through an iterable object:

for x in mytuple:
    print(x)
#     Output
#     Vignesh
#     Sitharthan
#     Baskaran


# In[8]:


# Create an Iterator
# The __iter__() method acts similar, you can do operations (initializing etc.), but must always return 
# the iterator object itself.
# The __next__() method also allows you to do operations, and must return the next item in the sequence.

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        self.a += 1
        return x
c1 = MyNumbers()
myiter = iter(c1)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
# Output
# 1
# 2
# 3
# 4


# In[12]:


# What is a Module?
# Consider a module to be the same as a code library.

# A file containing a set of functions you want to include in your application.

import platform

x = dir(platform)
print(x)


# In[ ]:




