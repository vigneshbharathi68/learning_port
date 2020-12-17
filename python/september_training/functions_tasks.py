#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Create a function that can accept two arguments name and age and print its value

def Person(name, age): # Initiating two arguments
    print(name, age)
    
    
Person('Vignesh', '21') # passing two arguments
# Ouput
# Vignesh 21


# In[15]:


# Write a function func1() such that it can accept a variable length of  argument and print all arguments value
# Expected Output:
# After func1(20, 40, 60):
# 20
# 40
# 60

# After func1(80, 100):
# 80
# 100

def func1(a, b, c=None): # Here 0 is the default argument Keyword arguments, positional arguments
    print(a)
    print(b)
    print(c)

func1(20, 40, 60)
# Output
# 20
# 40
# 60

func1(80, 100) # The below output prints 0 at c, I don't want that
# Output
# 80
# 100
# None

def func2(*args):
    for i in args:
        print(i)
        
func2(10,20,30,40,50)
# Output
# 10
# 20
# 30
# 40
# 50


# In[8]:


def myfunc(text, num):
    while num > 0:
        print(text, end="\n")
        num = num - 1

myfunc('Hello', 4)

# Output
# Hello
# Hello
# Hello
# Hello


# In[23]:


# Write a function calculation() such that it can accept two variables and calculate 
# the addition and subtraction of it. And also it must return both addition and subtraction in a single return call

def Calculation(a, b):
    return a+b, a-b

res = Calculation(40, 10)
print(res)
# Output
# (50, 30)

sub, add = Calculation(40, 10) # Sub defined to a + b and add defined to a - b
print(add) #So it return 30 
print(sub) #It returns 50
# Output
# 50
# 30


# In[24]:


# Create a function showEmployee() in such a way that it should accept employee name, and it’s salary and display both,
# and if the salary is missing in function call it should show it as 9000

def showEmployee(name, salary = 9000):
    print("The Employee",name,"salary is",salary)
    
showEmployee('Vignesh')


# In[32]:


# Create an inner function to calculate the addition in the following way

    # Create an outer function that will accept two parameters a and b
    # Create an inner function inside an outer function that will calculate the addition of a and b
    # At last, an outer function will add 5 into addition and return it
def outerfunc(a, b):
    square = a**2
    def innerfunc(a, b):
        return a+b
    add = innerfunc(a, b)
    return add + 5

result = outerfunc(5, 10)
print(result)
# Output
# 20


# In[34]:


# Generate a Python list of all the even numbers between 4 to 30

print(list(range(4,30,2)))

# Output
# [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]


# In[37]:


# Return the largest item from the given list

aList = [10, 12, 35, 45, 100]

print(max(aList))

# Output
# 100


# In[57]:


class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        self.email = name+ '.' + '@company.com'

    def detail(self):
        return '{} is {} years old.'.format(self.name, self.age)
    


emp_1 = Employee('Vignesh', 24, 50000)
# emp_2 = Employee()

# emp_1.name = 'Vignesh'
print(emp_1.name)
print(emp_1.age)
print(emp_1.salary)
print(emp_1.email) # emp_1


# In[59]:


# Format printing

print('{} is {} years old.'.format(emp_1.name, emp_1.age))
# Ouput
# Vignesh is 24 years old.

# Istead of doing this i am defining a function for this 
    
print(emp_1.detail())


# In[ ]:




