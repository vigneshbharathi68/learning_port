#!/usr/bin/env python
# coding: utf-8

# In[19]:


# Itertools: product, permutations, combinations, accumulate, groupby, and infinte iterators

from itertools import product
from itertools import permutations
from itertools import combinations
from itertools import accumulate
from itertools import groupby
a = [1, 2]
b = [3, 4]

prod = product(a, b)

print(list(prod))

# Output
# [(1, 3), (1, 4), (2, 3), (2, 4)]


# In[20]:


#Permutations

a = [1, 2, 3]
# perm = permutations(a)
perm = permutations(a,2)
print(list(perm))

# Output
# [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]


# In[21]:


#Combinations

comb = combinations(a, 2)

print(list(comb))
# Output
# [(1, 2), (1, 3), (2, 3)]


# In[22]:


#accumulation

import operator
a = [1, 2, 3, 4]

acc = accumulate(a, func = operator.add)

print(a)
print(list(acc))

# Output
# [1, 2, 3, 4]
# [1, 3, 6, 10]


# In[46]:


#groupby. It prints the both true and false expressions

a = [0, 1, 2, 5, 3, 4]
group_obj = groupby(a, key = lambda x: x<3)
for key, value in group_obj:
    print(key,list(value))


# Output
# True [0, 1, 2]
# False [5, 3, 4]

#With this function I am going to groupby dictionaries with their age

persons = [{'name':'Vignesh', 'age': 24}, {'name':'Prince', 'age': 24}, {'name':'Narendra Modiji', 'age': 70},
{'name':'Shankar', 'age': 28}]

group_dict = groupby(persons, key = lambda x: x['age'])

for key, value in group_dict:
    print("In age ",key,"the group", list(value))
    
# Output
# True [0, 1, 2]
# False [5, 3, 4]
# In age  24 the group [{'name': 'Vignesh', 'age': 24}, {'name': 'Prince', 'age': 24}]
# In age  70 the group [{'name': 'Narendra Modiji', 'age': 70}]
# In age  28 the group [{'name': 'Shankar', 'age': 28}]

