#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Fibonacci series
class fibonacci:
    
    n1 = 0
    n2 = 1
    f = [0, 1]
    n = int(input("Enter no of terms you want to print: "))
    i = 0

    def fibo(n1,n2):
        for i in range(1, n-1):
            n3 = n2 + n1
            f.append(n3)
            n1 = n2
            n2 = n3
            i += 1
            

f1 = fibonacci()


print(f)
            


# In[ ]:


#Operator Overloading
class Student:
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        
    def report(self):
        return self.m1, self.m2, self.m3
    
    def __add__(self, other):
        return self.m1 + other.m1
    
#     def __add__(self, other):
#         return self.m2 + other.m2
    
    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3


s1 = Student(11, 21,50)
s2 = Student(30, 34,60)

total_mark = s1 + s2
total_mark2 = s1 + s2

print(s1.report())
print(s2.report())
print("The total mark of m1 is:", total_mark)
print("The total mark of m2 is:", total_mark2)
print("The average of s1 is", s1.avg())
print("The average of s2 is", s2.avg())


# In[ ]:


n = 10
for i in range(1,n+1):
    for j in range(0, i):
        print( "*", end = " ")
    print("\r")


# In[ ]:


#decorator- without touching the div function, we can use decorator to swap the value if a<b.
# That's where decorator comes into picture


def div(a,b):
    print (a/b)
        
        
def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)
    return inner

# a = int(input("Enter a:"))
# b = int(input("Enter b:"))

div1 = smart_div(div)

div1(5, 10)

