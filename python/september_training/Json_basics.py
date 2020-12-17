#!/usr/bin/env python
# coding: utf-8

# In[14]:


import json

x = '{"name":"Vignesh", "age": 24, "designation":"trainee"}' #Json format always give dict inside single quotation
print(x) #Its print as normal dict but still its a json format
# {"name":"Vignesh", "age": 24, "designation":"trainee"}

# Parse x
y = json.loads(x)

# print(x) # TypeError: the JSON object must be str, bytes or bytearray, not dict

print(y["age"])
# Output
# 24


# In[18]:


# If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.

#This function is used to convert dict into json

try:
    z = json.dumbs(x) #Its throw error because x is already in json format

except:
    print("AttributeError: module 'json' has no attribute 'dumbs'")


# In[39]:


#Lets give a fresh dict
import json
person = {
          "name":"Vignesh",
          "age":24,
          "city":"Trichy"
         }
print(type(person))
type(json)
print (json)


j = json.dumps(person) #Converts dict into json

print(j) #It is print as string, json


# In[52]:


# we can convert Python objects of the following types, into JSON strings:

# dict
# list
# tuple
# string
# int
# float
# True
# False
# None

print(json.dumps({"name":"Vignesh", "age": 24, "designation":"trainee"}))
print(json.dumps(["Vignesh", "Ganesh", "Rajesh"]))
print(json.dumps(("python", "Javascript", "C-sharp")))
print(json.dumps("Vignesh"))
print(json.dumps(21))
print(json.dumps(21.5))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

# Output
# {"name": "Vignesh", "age": 24, "designation": "trainee"}
# ["Vignesh", "Ganesh", "Rajesh"]
# ["python", "Javascript", "C-sharp"]
# "Vignesh"
# 21
# 21.5
# true
# false
# null

    # When you convert from Python to JSON, Python objects are converted into the JSON (JavaScript) equivalent:

    # Python	JSON
    # dict	Object
    # list	Array
    # tuple	Array
    # str	String
    # int	Number
    # float	Number
    # True	true
    # False	false
    # None	null


# In[55]:


#Assigining a dictionary

x = {"name": "John", 
     "age": 30, 
     "married": True, 
     "divorced": False, 
     "children": ["Ann","Billy"], 
     "pets": None, 
     "cars": [{"model": "BMW 230", "mpg": 27.5}, {"model": "Ford Edge", "mpg": 24.1}]
    }

# The above input has True, False and None it is in dict format
y = json.dumps(x)

print(y)
# Output here True, False and None are changed into true, false and null in json string
# {"name": "John", "age": 30, "married": true, "divorced": false, "children": ["Ann", "Billy"], "pets": null, 
# "cars": [{"model": "BMW 230", "mpg": 27.5}, {"model": "Ford Edge", "mpg": 24.1}]}


# In[58]:


# JSON can store Lists, bools, numbers, tuples and dictionaries.
# But to be saved into a file, all these structures must be reduced to strings.
# It is the string version that can be read or written to a file.
# Python has a JSON module that will help converting the datastructures to JSON strings.

sorted_string = json.dumps(x, indent = 4)
print(sorted_string)

