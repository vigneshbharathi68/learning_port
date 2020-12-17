#!/usr/bin/env python
# coding: utf-8

# In[10]:


class Computer:
    
    def config(self):
        print("i5, 16gb, 1TB")
        
    def config2(self):
        print("i9, 14gb, 2TB")

com1 = Computer()
com2 = Computer()

com1.config()
com1.config2()
com2.config()


# In[27]:


class Computer:
    
    def _init_(self, name, age):
        self.name = name
        self.age = age

#c1 and c2 are the objects and every object has different memory allocations
c1 = Computer()
c2 = Computer()

print(id(c1))
print(id(c2))

c1.name = "Bharathi"
c2.name = "Vignesh"

print("Second name is", c1.name)
print("First name is", c2.name)


# In[38]:


class Computer:
    
    def __init__(self):
        self.name = "Bharathi"
        self.age = 20
        
c1 = Computer()
c2 = Computer()

c1.name = "Vignesh"

print(c1.name)
print(c2.name)


# In[85]:


class Computer:
    
    
    
    def __init__(self):
        self.name = "Vignesh"
        self.age = 20
        
    def __init__(self):
        self.name = "xxx"
        self.age = 45
        
    def update(self):
        self.age = 30
        
    def compare(self, other):
        if self.age == other.age:
            return true
        else:
            return false
        
        
c1 = Computer()
c2 = Computer()
c3 = Computer()
c4 = Computer()


print(c1.name)
print(c2.name)
print(c1.age)


# In[ ]:


class car:
    wheel = 4 #We cannot change the value, its called class variable
    
    
    def __init__(self): #This one is a Instance variable, We can update the value later
        self.mil = 10
        self.com = "BMW"
    
    @staticmethod
    def Hello():
        print("Hello World!")    
        
c1 = car()

print(c1.com, c1.mil, c1.wheel)


c1.com = "AUDI" #updating the value

print(c1.com, c1.mil, c1.wheel) #Now the output will print as Audi instead of BMW
car.Hello() 

# Output
# BMW 10 4
# AUDI 10 4
# Hello World!


# In[ ]:


class student:
    school = "Chadura"
    
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    
    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3
    
    @classmethod
    def info(cls):
        return cls.school
    
s1 = student(21,22,33)
s2 = student(45,55,78)



print("The average marks of student 1 is: ", s1.avg())
print("The average marks of student 2 is: ", s2.avg())
print("The students are studied in ", student.info())    
        


# In[ ]:


class student:
    
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        
    def show(self):
        print(self.name, self.rollno)


#     class laptop:
#         def __init__(self):
#             self.brand = "HP"
#             self.cpu = "i5"
#             self.ram = 8

s1 = student("Vignesh", 1) #Passing the value to the variable
s2 = student("Bharathi", 2)

s1.show()
s2.show()
    


# In[ ]:




