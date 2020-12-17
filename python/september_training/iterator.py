#!/usr/bin/env python
# coding: utf-8

# In[32]:


#Iterator
class TopTen:
    
    def __init__(self):
        self.num = 1
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.num <=10:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration
        
value = TopTen()

# print(value.__next__())
# print(value.__next__())

for i in value:
    print(i)

# Output
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

