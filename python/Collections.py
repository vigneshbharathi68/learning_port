#!/usr/bin/env python
# coding: utf-8

# In[30]:


#Collections: Counter, namedtuple, OrderedDict, defaultdict, deque import counter
from collections import Counter #It means we are using counter module from collection package

a = 'aaaaaaaaaabbbbbbccc'
    
my_counter = Counter(a) #This function retruns the dictionary that caontains all the characters as key count wil be values
    
print(my_counter) #U can see that in output al the characters are seperated and have a values
# Output
# Counter({'a': 10, 'b': 6, 'c': 3})

#Methods in counter module

print(my_counter.items()) #It ill print as (key,value) pairs
# Output
# dict_items([('a', 10), ('b', 6), ('c', 3)])

print(my_counter.keys()) #it ill print the keys
# Output
# dict_keys(['a', 'b', 'c'])

print(my_counter.values())
# Output
# dict_values([10, 6, 3])

print(my_counter.most_common(1)[0]) #It return output as a tuple
# Output
# ('a', 10)

print(list(my_counter.elements())) #It will come back as list with ala the elements we converted first
# Output
# ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'b', 'b', 'c', 'c', 'c']


# In[42]:


from collections import namedtuple

Point = namedtuple('Point', 'x,y')  #It wil create the class with field x and y

print(point)
#<class '__main__.Point'>

pt = Point(1, 0.2)
print(pt)

# Output
# Point(x=1, y=0.2)

print(pt.x, pt.y)
# Output
# 1 0.2


# In[46]:


#Ordered dictionary is the regular dictionary but they konow the order always
from collections import OrderedDict
ordered_dict = {}

ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4

print(ordered_dict)
# Output
# {'a': 1, 'b': 2, 'c': 3, 'd': 4}


# In[51]:


from collections import defaultdict

# d = {} If we assign this the output ill be "{'a': 1, 'b': 2}" , But if we give a key that is not in our assignment
#Then it ill throw the key type error

d = defaultdict(int) # If we give this the output will return "defaultdict(<class 'int'>, {'a': 1, 'b': 2})"

d['a'] = 1
d['b'] = 2

print(d)
# Output
# defaultdict(<class 'int'>, {'a': 1, 'b': 2})

# we also print outputwith key 

print(d[a])
# Output
# 0

