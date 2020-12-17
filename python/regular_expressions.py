#!/usr/bin/env python
# coding: utf-8

# In[59]:


# Regular Expression: 
# Methods / functions: findall(), search(), split(), sub(), .span(), .string, .group()

import re
# import inspect
print(dir())
# inspect.getsource()


# In[64]:



class player():
    
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        
    def get_age(self):
        print(self.name, "age is ",self.age)
        
    def get_height(self):
        print(self.name, "height is ", self.height)
    
    def get_weight(self):
        print(self.name, "weight is", self.weight)
        
p1 = player("David Jones", 25, 6.5, 80)

p1.get_age()
p1.get_height()
p1.get_weight()

# inspect.getsource(get_age)

# Output
# David Jones age is  25
# David Jones height is  6.5
# David Jones weight is 80


# In[2]:


import json

x = {"name":"Vignesh", "rollno": 1414, "class":"Msc"}

y = json.dumps(x, indent = 4)

print(y)


# In[9]:


import re

txt = "The rain in the spain"

x = re.search("Yesterd.*Musiri", txt)

if x:
    print("Yes")
    
else:
    print("No")
    
    
# Ouput
# Yes


# In[10]:


# RegEx Functions
# Function	Description

# findall	Returns a list containing all matches
# search	Returns a Match object if there is a match anywhere in the string
# split	Returns a list where the string has been split at each match
# sub	Replaces one or many matches with a string

def testing(num):
    if(num>50):
        return (num - 2)
    return testing(testing(num+10))

print(testing(30))

# Output
# 52


# In[11]:


x = re.findall("ai", txt)

print(x)


# In[31]:


# txt = "The rain in the spain"

x = re.findall("spain", txt) # Yes match found ['spain']
x = re.findall("\AThe", txt) # Yes match found ['The']
x = re.findall(r"ain\b",txt) # Yes match found ['ain', 'ain']
x = re.findall(r"\bain",txt) # No match found, r takes a input as a raw_string
x = re.findall("\d", txt) # No match found, Returns nthe match from 0-9
x = re.findall("\D", txt) # Yes match found 
                # ['T', 'h', 'e', ' ', 'r', 'a', 'i', 'n', ' ', 'i', 'n', ' ', 't', 'h', 'e', ' ', 's', 'p', 'a', 'i', 'n']
                # Returns a match where the string DOES NOT contain digits.It actually wrote each char seperated

x = re.findall("\s", txt) # Yes match found [' ', ' ', ' ', ' '], It simply wrote the whitespace,
            # Returns a match where the string contains a white space character

x = re.findall("\S", txt) # Yes match found
            # ['T', 'h', 'e', 'r', 'a', 'i', 'n', 'i', 'n', 't', 'h', 'e', 's', 'p', 'a', 'i', 'n'] 
            # Returns a match where the string DOES NOT contain a white space character
        
x = re.findall("\w", txt) # Yes match found
        #  ['T', 'h', 'e', 'r', 'a', 'i', 'n', 'i', 'n', 't', 'h', 'e', 's', 'p', 'a', 'i', 'n']
        # Returns a match where the string contains any word characters
        # (characters from a to Z, digits from 0-9, and the underscore _ character)
        # Return a match at every NON word character (characters NOT between a and Z. Like "!", "?" white-space etc.):
        
x = re.findall("\W", txt) # Yes match found
        # [' ', ' ', ' ', ' ']
        
x = re.findall("\Z", txt) # Yes match found
                          # ['']
        # Returns a match if the specified characters are at the end of the string
        
if x:
    print("Yes match found\n", x)
else:
    print("No match found")
    


# In[68]:


# Search() function
# The search() function searches the string for a match, and returns a Match object if there is a match.

# If there is more than one match, only the first occurrence of the match will be returned:


x = re.search("\s", txt)

x = re.search("\AHi", txt)
if x:
    print("Yes match found")
else:
    print("No match found")
print("The first white-space character is located in position:",x)
# Output
# Yes match found
# The first white-space character is located in position: 3


# In[74]:


# split() function

x = re.split("\s", txt) #Splitted using space
x = re.split("\W", txt)
x = re.split("\AThe", txt)

print(x)


# In[97]:


# sub() function
# The sub() function replaces the matches with the text of your choice:
x = re.sub("s", "9", txt) # The rain in the 9pain, Its changing the char
x = re.sub("\s", "9", txt) # The9rain9in9the9spain
x = re.sub("\w", "9", txt) # It changes each char
x = re.sub("\W", "9", txt) # The9rain9in9the9spain
x = re.sub("\A", "0", txt) # 0The rain in the spain
x = re.sub("\b", "0", txt)
x = re.sub("\B", "0", txt) # T0h0e r0a0i0n i0n t0h0e s0p0a0i0n
x = re.sub("\d", "0", txt)
x = re.sub("\D", "0", txt) # 000000000000000000000, Returns a match where the string DOES NOT contain digits
x = re.sub("\Z", "0", txt) # The rain in the spain0 

x = re.sub("i", "0", txt, 2) # The ra0n 0n the spain, This returns first two occurence


print(x)


# In[111]:


# Some search methods
import re
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt) 


print(x.span()) # (12, 17), #Search for an upper case "S" character in the beginning of a word,
                        # and print its position:
    
print(x.string) # The rain in Spain, The string property returns the search string
print(x.group()) # Spain, Search for an upper case "S" character in the beginning of a word, and print the word

