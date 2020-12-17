#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Source:
# https://pynative.com/python-basic-exercise-for-beginners/


# In[4]:


# Started this at 10:00 AM and ends in 10:43AM...

# Question 3: Given a string, display only those characters which are present at an even index number.
# For example str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.

a = "VigneshBharathiw" #I am giving 15char string

def EvenIndexChar(str):
    for i in range(0, len(str), 2): # Giving range for-in loop, here it ill take range(0,14,2)
        print("index[",i,"]", str[i]) #Index[",i,"]
        
def OddIndexChar(str):
    for i in range(1,len(str),2):
        print("index[",i,"]", str[i])


print("The original srting", a)
# Output
# The original srting VigneshBharathiw

print("Printing only even index char")
EvenIndexChar(a)
# Output
# The original srting VigneshBharathiw
# Printing only even index char
# index[ 0 ] V
# index[ 2 ] g
# index[ 4 ] e
# index[ 6 ] h
# index[ 8 ] h
# index[ 10 ] r
# index[ 12 ] t
# index[ 14 ] i

print("Printing only odd index char")
OddIndexChar(a)
# Output
# Printing only odd index char
# index[ 1 ] i
# index[ 3 ] n
# index[ 5 ] s
# index[ 7 ] B
# index[ 9 ] a
# index[ 11 ] a
# index[ 13 ] h
# index[ 15 ] w


# In[13]:


# Question 4: Given a string and an integer number n, 
# remove characters from a string starting from zero up to n and return a new string
def RemoveCharLeft(str, n): # Here we passing two arguments one is String which we given, And another is no of elements we are
                        # going to remove
    return str[n:]

# def RemoveCharRight(str, n):
#     return str(n)

f = input(f"Enter the number of char u want to remove from {a} :")
value = int(f)

print("Printing the string char removed from left: ",RemoveCharLeft(a, value))
# print("Printing the string char removed from right: ",RemoveCharRight(a, value))

# Output
# Enter the number of char u want to remove from VigneshBharathiw :5
# Printing the string char removed from left:  shBharathiw

