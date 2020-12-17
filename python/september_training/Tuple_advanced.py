#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Tuple always assigned inside () this

mytuple = ("Vicky", 20, "Musiri")

print(mytuple)

# Output
# ('Vicky', 20, 'Musiri')


# In[5]:


#Tuples are immutable and I am going to make of mytuple to mytuple2 as list

my_list = []
mytuple2 = list(mytuple) #Tuple converted into list and stored to mytuple2.
my_list = tuple([])
print(my_list)
print(mytuple2)

# Output
# ()
# ['Vicky', 20, 'Musiri']


# In[7]:


#Using tuple in if statement

if "Vicky" in mytuple:
    print("Yes")
else:
    print("No")

print(mytuple)

# Output
# Yes
# ('Vicky', 20, 'Musiri')


# In[8]:


#Updating value in tuple lets try if it is work or not

mytuple[0] = "Rocky"

# Output
# TypeError                                 Traceback (most recent call last)
# <ipython-input-8-7f6b32c063c4> in <module>
#       1 #Updating value in tuple lets try if it is work or not
#       2 
# ----> 3 mytuple[0] = "Rocky"

# TypeError: 'tuple' object does not support item assignment


# In[12]:


#No we caanot update value in tuple
#Once we assigned in tuple it cannot be mutable
#Now will try cpunt and length in the tuples

my_tuple = ('a', 'c', 'f', 'c', 'd', 'e', 'f', 'f', 'g', 'h', 'i', 'g', 'j', 'k', 'g', 'l', 'l')

x = input("Enter which alphabet u want to search in tuple... Please enter upto l:-->")

print(my_tuple.count(x))


# Output
# Enter which alphabet u want to search in tuple... Please enter upto l:-->l
# 2


# In[13]:


# Going to chek the index of the element

print(my_tuple.index('f')) #this il return first 'f' index in the tuple

# Output
# 2


# In[26]:


#Now ill search ebery index num for the element in my_tuple
#We should use for loop to print all index number in the my_tuple

for i in my_tuple:
    print(my_tuple.index(i, 0, 17), i) # It again takes the index number for the first element and 
                                # print the same index number for the rest of the duplicates
                                # I couldn't print each duplicate has a seperate index number
        
# Output
# 0 a
# 1 c
# 2 f
# 1 c
# 4 d
# 5 e
# 2 f
# 2 f
# 8 g
# 9 h
# 10 i
# 8 g
# 12 j
# 13 k
# 8 g
# 15 l
# 15 l


# In[42]:


#Tuple slicing

a = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print(a[2:])
# Output
# (2, 3, 4, 5, 6, 7, 8, 9, 10)

print(a[:2])
# Output
# (0, 1)

print(a[2:5])
# Output
# (2, 3, 4)

print(a[::2]) #It print all secound elements, Its also means jumps two index number
# Output
# (0, 2, 4, 6, 8, 10)

print(a[::1]) #It prints all elements means one by one
#Output
# (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print(a[2::5]) #It prints 2nd index number's element and again start's in 2nd index number and then prints the 5th element
# Output
# (2, 7)

print(a[3::10])
# Output
# (3,)

print(a[1::3]) #start with 1 and print 3 jumps
# Output
# (1, 4, 7, 10) 

print(a[4::2]) #Start with 4 and print 2 jumps from 4
# Output
# (4, 6, 8, 10)

print(a[5::2])
# Output
# (5, 7, 9)


# In[43]:


# Assigning variable for the each element in tuple
my_tuple2 = ('Vignesh', 20, 'Trichy')
name, age, location = my_tuple2

print(name)
print(age)
print(location) #We can print it through the key

# Output
# Vignesh
# 20
# Trichy


# In[46]:


# Unpack elements with *. Lets see what happen

b = (1, 2, 3, 4, 5, 6)

i1, *i2, i3 = b
print(i1) # It returns the first element
print(i3) # It returns the last element
print(i2) # It return the remaining elements as list

# Output
# 1
# 6
# [2, 3, 4, 5]


# In[48]:


#Memory allocations for list and tuple
#As you see the output, Tuple takes less memory allocation space than list.
#
import sys

print(sys.getsizeof(mytuple2), "Bytes")`
print(sys.getsizeof(mytuple), "Bytes")


# In[50]:


#Tried install numpy
import numpy

arr = numpy.array([1, 2, 3, 4, 5])

print(arr)

