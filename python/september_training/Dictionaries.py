#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Dictionary assigning
#To create a Dictionary, use {} curly brackets to construct the dictionary and [] square brackets to index it.
#Separate the key and value with colons : and with commas , between each pair.
dict = {1:'Vignesh', 2:'Sidharth', 3:'Prince'}
print(dict)


# In[2]:


dict


# In[7]:


# print(dict[0])
print(dict[1]) #Inside of sqyare brackets we should give the key
print(dict[2])


# In[14]:


#Using get method to avoid error
#get expected at least 1 arguments, got 0

dict.get(0,'Not found') #0 key is not assigned instead od throw error I get output as 'Not found'


# In[18]:


#If I call the dictionary without give print function, It only taking the last dict.get() and give the output
#If i want each key seperately I should use print function to get the each key as output
print(dict.get(1))
print(dict.get(2))
print(dict.get(3))


# In[19]:


#Above all are simple dictionaries
#Now assign a dictionary inside of the assigned dictionary. Simply like a nested dictionary
#Below I am assigning key as a programming language, and values as the tools for using the corresponding languages 
prog = {'JS':'Atom', 'CS':'VS', 'python':['pycharm', 'Jupyter Notebook'], 'Java':{'JEE':'Eclipse', 'JSE':'Netbeans'}}

#The above has list and dictionaries. Python key has a list, java has a dictionary and everything assigned in prog


prog


#Output
# {'JS': 'Atom',
#  'CS': 'VS',
#  'python': ['pycharm', 'Jupyter Notebook'],
#  'Java': {'JEE': 'Eclipse', 'JSE': 'Netbeans'}}


# In[32]:


#Will print each key. Let's see what ill happen

print(prog.get('JS')) #I am getting error because I missed the single quotes, and it totally stops the print function
print(prog.get('CS'))
print(prog.get('python'))
print(prog.get('Java'))

#Output
# Atom
# VS
# ['pycharm', 'Jupyter Notebook']
# {'JEE': 'Eclipse', 'JSE': 'Netbeans'}

# The above output as u seen giving the values as it is


# In[37]:


#Will get the output inside java dictionary

print(prog['Java']['JEE']) # This is how u ill get the Java's dictionary key values seperately

# Output
# Eclipse


# In[45]:


#Now we are going to update keys and values in dictionaries
prog

#Output before update
# {'JS': 'Atom',
#  'CS': 'VS',
#  'python': ['pycharm', 'Jupyter Notebook'],
#  'Java': {'JEE': 'Eclipse', 'JSE': 'Netbeans'}}

# keys = ['Vignesh', 'Sidharth', 'Prince']
# values = ['python', 'Java', 'HTML']

prog['Vignesh'] = 'python'

prog

#Output
# {'JS': 'Atom',
#  'CS': 'VS',
#  'python': ['pycharm', 'Jupyter Notebook'],
#  'Java': {'JEE': 'Eclipse', 'JSE': 'Netbeans'},
#  'Vignesh': 'python'}

# As you see the above output key 'Vignesh' updated in the prog dictionary eith value 'python'


# In[55]:


#Now we delete the key and value 
del prog['python']

prog
# Output
# {'CS': 'VS',
#  'python': ['pycharm', 'Jupyter Notebook'],
#  'Java': {'JEE': 'Eclipse', 'JSE': 'Netbeans'}}

#As you see the above dictionary, U can see the JS key deleted


# In[61]:


prog1 = {1:'Empty'}
prog2 =  {'JS':'Atom', 'CS':'VS', 'python':['pycharm', 'Jupyter Notebook'], 'Java':{'JEE':'Eclipse', 'JSE':'Netbeans'}}


# In[63]:


print(prog1)
print(prog2)


# In[70]:


#I am going to merge two dictionaries
#By using function
prog1
prog2

def updatedict(prog1, prog2):
    return (prog2.update(prog1))

print(updatedict(prog1,prog2)) #This return none, Ijust calling functin here. It doesn't assigned to any variable

print(prog2)
print(prog1)
    
# Output
# None

# {'JS': 'Atom',
#  'CS': 'VS',
#  'python': ['pycharm', 'Jupyter Notebook'],
#  'Java': {'JEE': 'Eclipse', 'JSE': 'Netbeans'},
#  1: 'Empty'}  #this return prog2

# {1: 'Empty'} this returns prog1

# As we see in the above out we could see prog 1 is updated with prog 2 and prog 2 ill have prog1 and prog 1 remains same.


# In[76]:


# Using ** method to update

dict1 = {'a':1, 'b':2 , 'C':3}
dict2 = {'d':4, 'e':5, 'f':6}

def merge(dict1, dict2):
    res = {**dict1, **dict2} #Using ** [double star] is a shortcut that allows you to pass multiple arguments to a 
                                #function directly using a dictionary.
    return res

dict3 = merge(dict1, dict2) #Just bescause dict1 variable 

print("Printing with function",merge(dict1, dict2)) #We can print with function itself

print("Printing with variable",dict3) #Or we can print with variable


# Output
# Printing with function {'a': 1, 'b': 2, 'C': 3, 'd': 4, 'e': 5, 'f': 6}
# Printing with variable {'a': 1, 'b': 2, 'C': 3, 'd': 4, 'e': 5, 'f': 6}

