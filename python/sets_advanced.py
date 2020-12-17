#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Creating with set brackets no need of assigning key, value pairs
# sets: Unordered, mutable, no duplicates
x = {1,2,3,4,5,6}
print(x)

# Output
# {1, 2, 3, 4, 5, 6}


# In[6]:


#It does not store a dupilcate value

x = {1,2,3,4,5,6,7,8,3,4,5,3,5} #As you see this input it has the some value more than one times
print(x) #Lets see what will print

# Output
# {1, 2, 3, 4, 5, 6, 7, 8}
#As you see the above output, It does not print duplicate values.


# In[7]:


# Now create a empty set

myset = {}
print(type(myset)) #Let's what type myset will be

# Output
# <class 'dict'>
#OOPS I got type as dictionary


# In[8]:


#We shoul use set() method to create a empty set

myset = set()
print(type(myset))

# Output
# <class 'set'>
# Hurrey i got the empty set


# In[17]:


#Lets see what ill happen when i give string as a value

myset = set("hello")
print(myset)

# Output
# {'e', 'h', 'o', 'l'}
# Hey i got each letters seperately this is because I use set method

myset = {"Hello"} #This is still a set because i did not give input as set,value pairs
print("The type of set 'Hello' is ",type(myset)) 
print(myset)

# Output
# The type of set 'Hello' is  <class 'set'>
# {'Hello'}


# In[29]:


#Will add a some value and remove some value using add method

myset = set()
myset.add(1)
myset.add(2)

print(myset)
# Output
# {1, 2}

#Will remove the values in set

myset.remove(1)
#Hint: I had facing the issue of remove method in list, I couldn't retrieve the data which i removed
#But in set it can reverse by just erasing method line

print(myset)
# Output
# {2}

# Lets use discard() method lets see what happen

myset.discard(1) #The use of this key is it doesn't throw error if argument we pass is not in out set

print(myset)
# Output
# {2}


# In[ ]:




