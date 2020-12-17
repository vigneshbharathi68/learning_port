#!/usr/bin/env python
# coding: utf-8

# In[7]:


#decorator- without touching the div function, we can use decorator to swap the value if a<b.
# That's where decorator comes into picture


a = int(input("Enter a: "))
b = int(input("Enter b: "))

def div(a,b):
    print (a/b)
        
#Decorator        
def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)
    return inner

div1 = smart_div(div)

div1(a, b)

# output
# Enter a: 5
# Enter b: 15
# 3.0
#As Above you can see the output as 3 even I gave b is greater than a, as Decorator swap values and give us the output as 
#3.0. This is the use of decorator.