#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Assigining strings
a = "Hello world" #Single line strings
b= "I'm Vignesh working in Chadura" #Use single quotes or use \ this to avoid getting error
c = """Hello word
hello world""" #This one is used for multi line strings printing

print(a)
print(b)
print(c)

# Output
# Hello world
# I'm Vignesh working in Chadura
# Hello word
# hello world


# In[2]:


#Print using index number

char = a[1] #The inde3x number of the string 1 wil print

print(char)

# Output
# e


# In[3]:


#Print each character in the string

for i in a:
    print(i)

# Output
# H
# e
# l
# l
# o
 
# w
# o
# r
# l
# d


# In[9]:


# Remove white space in the given string 

my_string = '    Hello World    '

print(my_string)

my_string = my_string.strip() #Strip method is used to remove the white space

print(my_string)

my_string = my_string.upper()

print(my_string)

my_string = my_string.lower()

print(my_string)

print(my_string.startswith("hello"))
print(my_string.endswith("world"))

print(my_string.replace("world", "universe"))

# Output
#     Hello World    
# Hello World
# HELLO WORLD
# hello world
# True
# True
# hello universe


# In[10]:


#Splitting words and convert string into list

my_string = "How are you doing"

my_list = my_string.split() #In default it spilts the strings with space

print(my_list) #This il converts into list
print(my_string) #Still it remains samw as we entered

# Output
# ['How', 'are', 'you', 'doing']
# How are you doing


# In[14]:


#splitting the words and make a new list with that
my_string = "How, are, you, doing"

my_list = my_string.split(", ")

new_string = ' '.join(my_list)

print(my_list)
print(new_string)

# Output
# ['How', 'are', 'you', 'doing']
# How are you doing


# In[28]:


#Will see the use of join method in the below program

from timeit import default_timer as timer
my_list = ['a'] * 6
print(my_list)
start = timer()

# Will join this and make a string

my_string = ''
for i in my_list:
    my_string += i #It will concatinate each elements in the list and make that as a string
stop = timer()

# print(my_string)

print("The time takes to execute for loop",stop-start)
# Output
# aaaaaa

start = timer()
my_string = ''.join(my_list)
stop = timer()

# print(my_string)

print("The time takes to execute join method",stop-start)

# Output
# The time takes to execute for loop 0.0003620000006776536
# The time takes to execute join method 0.0001680999994277954


# In[ ]:




