#!/usr/bin/env python
# coding: utf-8

# In[3]:


# File handling
# Functions: open(), close(), read(), write(), readline()
# Modes: read, write, append

f = open("demofile.txt", 'w') # It tried open file, If file does not exist it creates a new one

f.close()


# In[9]:


# We declared the variable f to open a file named guru99.txt. Open takes 2 arguments,
# The file that we want to open and a string that represents the kinds of permission or operation we want to do on the file


f = open("demofile.txt", 'w+') # Plus sign indicates both read and write
for i in range(10):
    f.write("This is line %d\r\n" %(i + 1))

f.close()


# In[16]:


#We should open the file content
f = open("demofile.txt", "r")
content = f.read()
print(content.strip())

f.close()


# In[28]:


f = open("demofile.txt", 'r')

# print(f.read(5)) # This

# print(f.read(15))  # This is line 1 
for i in range(13):
    print(i)
    print(f.readline())


# In[29]:


# Mode	Description

# 'r'	This is the default mode. It Opens file for reading.

# 'w'	This Mode Opens file for writing.
    # If file does not exist, it creates a new file.
    # If file exists it truncates the file.

# 'x'	Creates a new file. If file already exists, the operation fails.

# 'a'	Open file in append mode.
    # If file does not exist, it creates a new file.

# 't'	This is the default mode. It opens in text mode.

# 'b'	This opens in binary mode.

# '+'	This will open a file for reading and writing (updating)


# In[37]:


f = open("demofile.txt", 'r')
# print(f.read().strip()) # This ill print the file content

for x in f:
    print(x.strip())


# In[52]:


f = open("demofile.txt", 'w')
x = "Helklo worlds"
f.write(x)
f.close()

f = open("demofile.txt", 'r')

print(f.read()) # Helklo worlds


# In[62]:


f = open("demofile.txt", 'a')

print(f.write("\nthis has more content"))
f.close()

f = open("demofile.txt", 'r')
print(f.read()) # Helklo worldsthis has more contentthis has more content
                # this has more content


# In[72]:


# pattern printing....

for i in range(0,10):
    for j in range(0, i+1):
        print("*", end = " ")
    
    print("\r")

