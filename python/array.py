#!/usr/bin/env python
# coding: utf-8

# In[16]:


#array
from array import *

arr = array('i', [])

n = int(input("Enter the length of the array"))

for i in range(n):
    x = int(input("Enter the vnext value: "))
    arr.append(x)

print(i)  #I am printing this to find out no:of times the loop executes as initiate the value with 0
print(arr)


# In[20]:


#I anm checking the values in arr, If it is there means it ill print the index number of the array.
val = int(input("Enter the value for search: "))

k = 0
for e in arr:
    if e==val:
        print("The index number of the array is ",k)
        
    k+=1
    
# Output, Its printing all the 15's index number in the loop
# Enter the value for search: 15
# The index number of the array is  0
# The index number of the array is  2

