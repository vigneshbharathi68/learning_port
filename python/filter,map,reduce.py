#!/usr/bin/env python
# coding: utf-8

# In[24]:


#Using lambda functions instead of defining functions


# def is_even(n):
#     return n%2==0 I have ignored this function because i could use lambda to reduce the code.

nums = [1,5,8,6,10,15]


#I am going to took out even numbers from the above set


evens = list(filter(lambda n: n%2==0, nums)) #Using lambda function instead of defining

odds = list(filter(lambda n: n%2==1, nums))


double_even = list(map(lambda n: n*2, evens))

double_odd = list(map(lambda n: n*2, odds))


print("Even number in the set:",evens)              #this returns even num in the set nums
print("Odd number in the set:",odds)                #this returns  odd num in the set nums
print("Doubling the num in Even set:",double_even)  #this doubles the values in even set
print("Doubling the num in  Odd set:", double_odd)   #this doubles the values in  odd set


# output
# Even number in the set: [8, 6, 10]
# Odd number in the set: [1, 5, 15]
# Doubling the num in Even set: [16, 12, 20]
# Doubling the num in  Odd set: [2, 10, 30]

