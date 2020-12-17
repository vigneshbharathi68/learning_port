#!/usr/bin/env python
# coding: utf-8

# In[4]:


#I am going to chech whether the user input is in the list or not?
#Assign the list
x = ['Vignesh', 'Baskaran', 'Kumaran', 'Gnanavel', 'Ashwin', 'Sitharth', 'Appu', 'Partha']

print("Number of folks working in Chadura is",len(x))

n = input("Enter the name to find if he work here: ")

if n in x:
    print("Yes he is working here")
else:
    print("OOPS there is no employee with this name in our organisation...\nHe may come to our organization in the future...")
    
# Output:
# Number of folks working in Chadura is 8
# Enter the name to find if he work here: Vignesh
# Yes he is working here

# # Output:
# Number of folks working in Chadura is 8
# Enter the name to find if he work here: Sandhosh
# OOPS there is no employee with this name in our organisation...
# He may come to our organization in the future...


# In[8]:


my_list = ['India', 'America','Afganisthan', 'china', 'Pakisthan', 'Switzerland', 'Singapore']

list_copy = my_list.copy()

list_copy.append('Malasia')
print("Copy of my list is ",list_copy)
print("My list is ",my_list)

# Output
# Copy of my list is  ['India', 'America', 'Afganisthan', 'china', 'Pakisthan', 'Switzerland', 'Singapore', 'Malasia']
# My list is  ['India', 'America', 'Afganisthan', 'china', 'Pakisthan', 'Switzerland', 'Singapore']

#As you see the above output the chages i made in List_copy is not affecting my_list
#That is the use of copy() method


# In[11]:


list_copy.insert(1,'France') #Its added france three times because I run this code three time 
print(list_copy)

# Output
# ['India', 'France', 'France', 'France', 'America', 'Afganisthan', 'china', 'Pakisthan', 'Switzerland', 'Singapore', 'Malasia']


# In[13]:


#I have to remove two dupilcate france in list_copy
list_copy = list(dict.fromkeys(list_copy))
print(list_copy)

# Output
# ['India', 'France', 'America', 'Afganisthan', 'china', 'Pakisthan', 'Switzerland', 'Singapore', 'Malasia']


# In[31]:


def dup_remove(x):
    return(dict.fromkeys(x))
print(my_list)

#I have removed all the values in my_list
#I want to retrive all the values in the list, But I think its impossible
#Better copy the list_copy

my_list = list_copy.copy()

print(my_list)


# In[34]:


#Now remove 'malaysia'
#by using this  "my_list.remove('malaysia')" removed 'malaysia'
print(my_list)

# Output
# ['India', 'France', 'America', 'Afganisthan', 'china', 'Pakisthan', 'Switzerland', 'Singapore']


# In[35]:


for x in my_list:
    print(x)
    
# Output
# India
# France
# America
# Afganisthan
# china
# Pakisthan
# Switzerland
# Singapore


# In[44]:


#List slicing

# my_list.sort() #this method sorting as ascending order
# my_list.reverse()
print(my_list)

print(int(my_list.index('India'))+ 1) 

# Output
# ['china', 'Switzerland', 'Singapore', 'Pakisthan', 'India', 'France', 'America', 'Afganisthan']
# 5


# In[45]:


#India is in 5 th place
#No,I don't want that

my_list[0] = 'India'
my_list[4] = 'China'
print(my_list)

# Output
# ['India', 'Switzerland', 'Singapore', 'Pakisthan', 'China', 'France', 'America', 'Afganisthan']


# In[46]:


my_list[1] = 'America'
my_list[3] = 'Switzerland'
my_list[4] = 'France'
my_list[5] = 'China'
my_list[6] = 'Pakisthan'

print(my_list)

# Output
# ['India', 'America', 'Singapore', 'Switzerland', 'France', 'China', 'Pakisthan', 'Afganisthan']


# In[50]:


#Slicing list
print('The most beautiful countries in the world',my_list[:4])
print('The unpeacefull countries: ',my_list[5:])

# Output
# The most beautiful countries in the world ['India', 'America', 'Singapore', 'Switzerland']

