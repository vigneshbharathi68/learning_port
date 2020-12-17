#!/usr/bin/env python
# coding: utf-8

# In[8]:


#  Write a Python program to find validity of a string of parentheses,
# '(', ')', '{', '}', '[' and ']. These brackets must be close in the correct order,
# for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid.


class py_solution:
    
    def paranthesis_valid(self, str1):
        stack, pchar = [], {'[': ']', '(': ')', '{': '}'}
        
        for paranthesis in str1:
            if paranthesis in pchar:
                print(paranthesis)
                stack.append(paranthesis)
                print("THe stack is now",stack)
            elif len(stack) == 0 or pchar[stack.pop()] != paranthesis:
                return false
        print("The length of slack",len(stack) == 0)
    
print(py_solution().paranthesis_valid("()[]{}"))
print(py_solution().paranthesis_valid("([{"))
print(py_solution().paranthesis_valid("[]"))


# In[20]:


# Python Exercise: Sort (ascending and descending) a dictionary by value
# import operator
d = {4:6, 0:2, 2:7, 3:9, 1:90}

sorted_d = dict(sorted(d.items())) # {0: 2, 1: 90, 2: 7, 3: 9, 4: 6}
print(sorted_d)
# sorted_dict = dict(sorted(d.items(), key = operator.itemgetter(1)))
# print(sorted_dict)


# In[60]:


# Write a Python script to concatenate following dictionaries to create a new one

# Sample Dictionary :
dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50,6:60}
dic4 = {}
for i in dic1, dic2, dic3:
    print(i)
#     {1: 10, 2: 20}
#     {3: 30, 4: 40}
#     {5: 50, 6: 60}

for d in dic1, dic2, dic3: dic4.update(d)
print(dic4)
# {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


# Write a Python script to check whether a given key already exists in a dictionary.

def is_present(x):
    
    if x in dic4:
        
        print("Yes it is here in dictionary")
    else:
        print("no its not there")

is_present(1)
print("what is d here", d)


# In[61]:


# Write a Python program to iterate over dictionaries using for loops.

for dict_key, dict_value in dic4.items():
    print(dict_key,'-->', dict_value)
#     Output
#     1 --> 10
#     2 --> 20
#     3 --> 30
#     4 --> 40
#     5 --> 50
#     6 --> 60


# In[68]:


# Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
d = {}
n = int(input("Enter the number of key u want to add in dictionary: "))
for e in range(1,n+1): 
    d[e] = e*e
    
print(d)


# In[71]:


# Write a Python script to merge two Python dictionaries.

d1 = {1:1, 2:2}
d2 = {3:3, 4:4}
d3 = {}
for d in d1,d2: d3.update(d)
print(d3)


# In[72]:


# Python Exercise: Iterate over dictionaries using for loops

dictionary = {'Red':1, 'Orange':2, 'Yellow':3}

for color_key, values in dictionary.items():
    print(color_key, 'Corresponds to',values)
#     Output
#     Red Corresponds to 1
#     Orange Corresponds to 2
#     Yellow Corresponds to 3


# In[77]:


# Write a Python program to get the maximum and minimum value in a dictionary.

mydict = {'A':1234, 'B':456, 'c':9873}

# key_max = max(mydict.keys(), lambda k: mydict[k]) # '>' not supported between instances of 'function' and 'dict_keys'
key_max = max(mydict.keys(), key = (lambda k: mydict[k]))
print(key_max)
# Output
# c


# In[82]:


student_data = {'id1': 
   {'name': ['Sara'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id2': 
  {'name': ['David'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id3': 
    {'name': ['Sara'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id4': 
   {'name': ['Surya'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
}

result = {}

for key, value in student_data.items():
    print(key)
    #   Output
    #   id1
    #   id2
    #   id3
    #   id4
    print(value)
    # Output
    # id1
    # {'name': ['Sara'], 'class': ['V'], 'subject_integration': ['english, math, science']}
    # id2
    # {'name': ['David'], 'class': ['V'], 'subject_integration': ['english, math, science']}
    # id3
    # {'name': ['Sara'], 'class': ['V'], 'subject_integration': ['english, math, science']}
    # id4
    # {'name': ['Surya'], 'class': ['V'], 'subject_integration': ['english, math, science']}
    
    if value not in result.values():
        result[key] = value
        
print(result.keys())
# Output
# dict_keys(['id1', 'id2', 'id4'])

print(result.values())
# Output
# dict_values([
#            {'name': ['Sara'], 'class': ['V'], 'subject_integration': ['english, math, science']}, 
#            {'name': ['David'], 'class': ['V'], 'subject_integration': ['english, math, science']}, 
#            {'name': ['Surya'], 'class': ['V'], 'subject_integration': ['english, math, science']}
#            ])


# In[ ]:




