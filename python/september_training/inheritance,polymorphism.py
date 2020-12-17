#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Inheritance

class A: #parent class
    
    def feature1(self):
        print("Feature 1 is working")
    
    
    def feature2(self):
        print("Feature 2 is working")

        
class B(A):    #Child or sub class, so that we can access class A's features. 
               #Its kinnda like updating the features without changing the main class
    
    
    def feature3(self):
        print("Feature 3 is working")
        
    
    def feature4(self):
        print("Feature 4 is working")

a1 = A()
b1 = B()

a1.feature1()
a1.feature2()
b1.feature1()
b1.feature2()
b1.feature3()
b1.feature4()

# Output
# Feature 1 is working
# Feature 2 is working
# Feature 1 is working
# Feature 2 is working
# Feature 3 is working
# Feature 4 is working


# In[12]:


#muti level Inheritance

class A: #parent class
    
    def feature1(self):
        print("Feature '1' is working")
    
    
    def feature2(self):
        print("Feature '2' is working")

        
class B(A):    
    
    def feature3(self):
        print("Feature '3' is working")
        
    
    def feature4(self):
        print("Feature '4' is working")
        
class C(B): #It's a sub class of B. that means we can access Class A as well
            #Because B contains A features

    def feature5(self):
        print("Feature '5' is working")
        
    
    def feature6(self):
        print("Feature '6' is working")
        
    
a1 = A() #Instance of an Object for Class A
b1 = B() #Instance of an Object for Class B
c1 = C() #Instance of an Object for Class C


c1.feature1()
c1.feature2()
c1.feature3()
c1.feature4()
c1.feature5()
c1.feature6()

# Output
# Feature '1' is working
# Feature '2' is working
# Feature '3' is working
# Feature '4' is working
# Feature '5' is working
# Feature '6' is working


# In[22]:


#Multiple Inheritance

class A: #parent class
    
    @staticmethod
    def Detail():
        print("Feature in Class A:\n")
        
    def feature1(self):
        print("Feature '1' is working")
    
    
    def feature2(self):
        print("Feature '2' is working")

        
class B(): #It has a specific feature. Its not contains A's feature
    
    @staticmethod
    def Detail():
        print("Feature in Class B:\n")
    
    
    def feature3(self):
        print("Feature '3' is working")
        
    
    def feature4(self):
        print("Feature '4' is working")
        
class C(A,B): #It can have access to Class A and B.
              #
    @staticmethod
    def Detail():
        print("Feature in Class C:\n")
    
    def feature5(self):
        print("Feature '5' is working")
        
    
    def feature6(self):
        print("Feature '6' is working")
        
    
a1 = A() #Instance of an Object for Class A
b1 = B() #Instance of an Object for Class B
c1 = C() #Instance of an Object for Class C

a1.Detail()
a1.feature1()
a1.feature2()
print("\n\n")

b1.Detail()
b1.feature3()
b1.feature4()
print("\n\n")

c1.Detail()
c1.feature1()
c1.feature2()
c1.feature3()
c1.feature4()
c1.feature5()
c1.feature6()

# Output
# Feature in Class A:

# Feature '1' is working
# Feature '2' is working



# Feature in Class B:

# Feature '3' is working
# Feature '4' is working



# Feature in Class C:

# Feature '1' is working
# Feature '2' is working
# Feature '3' is working
# Feature '4' is working
# Feature '5' is working
# Feature '6' is working


# In[25]:


class A: #parent class
    
    
    def __init__(self):
        print("in init A\n")
        
    def feature1(self):
        print("Feature '1' is working")
    
    
    def feature2(self):
        print("Feature '2' is working")

        
class B(A):
    
    def __init__(self):
        super().__init__() #Super Method calls each init method which we use in both class
        print("in B init\n")
    
    
    def feature1(self):
        print("Feature '1' is working")
    
    
    def feature2(self):
        print("Feature '2' is working")
        
    def ini(self):
        super().__init__()

    
a1 = B() #by using super method we actually print all the init method in the classes


# In[39]:


class A: #parent class
    
    
    def __init__(self):
        print("in init A\n")
        
    def feature1(self):
        print("Feature '1-A' is working")
    
    
    def feature2(self):
        print("Feature '2' is working")

        
class B(A):
    
    def __init__(self):
        super().__init__() #Super Method calls each init method which we use in both class
        print("in B init\n")
    
    
    def feature1(self):
        print("Feature '1-B' is working")
    
    
    def feature3(self):
        print("Feature '3' is working")
        
    def ini(self):
        super().__init__()

    
a1 = B()
a1.feature1() #It print the fuction from left to right.

# Output
# in init A

# in B init

# Feature '1-B' is working


# In[44]:


class A: #parent class
  
  
  def __init__(self):
      print("in init A\n")
      
  def feature1(self):
      print("Feature '1-A' is working")
  
  
  def feature2(self):
      print("Feature '2' is working")

      
class B():
  
  def __init__(self):
      super().__init__() #Super Method calls each init method which we use in both class
      print("in B init\n")
  
  
  def feature1(self):
      print("Feature '1-B' is working")
  
  
  def feature3(self):
      print("Feature '3' is working")
      
  def ini(self):
      super().__init__()
      
class C(A,B):
  def __init__(self):
      super().__init__()
      print("In init C")
      
  def feature1(self):
      print("Fearure 1-C is working")
  
  def initi(self):
      super().feature1()
  
a1 = C()
a1.initi()
#It will print the init fuction from left to right.


# Output
# in init A

# In init C


# In[52]:


# Duck Typing

class pycharm:
    
    def execute(self):
        print("Compiling")
        print("Running")

        
class myeditor:
    
    def execute(self):
        print("Spell Check")
        print("COnventional check")
        print("Compiling")
        print("Running")
        
class laptop:
    
    def code(self, ide):
        ide.execute()
        
ide = myeditor()

        
lap1 = laptop()
lap1.code(ide)

#Output
# Spell Check
# COnventional check
# Compiling
# Running


# In[58]:


#Operator Overloading

class student:
    
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2
        
    def __add__(self,other):
        r1 = self.m1 + other.m1
        r2 = self.m2 + other.m2
        s3 = student(m1,m2)
        
        return s3
        

s1 = student(50,40)
s2 = student(40,50)

s3 = s1 + s2

print(s3.m1)


# In[ ]:




