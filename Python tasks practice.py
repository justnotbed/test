#!/usr/bin/env python
# coding: utf-8

# In[2]:


#1 task.
print("Hello, World!")


# In[3]:


#2 task. IF-ELSE
import math
import os
import random
import re
import sys

n=int(input())

if n>=1 and n<=100 and n%2==1 :
    print("Weird")
elif n%2==0 and (n>=2 and n<=5):
    print("Not Weird")
elif n%2==0 and (n>=6 and n<=20):
    print("Weird")
elif n%2==0 and n>20:
    print("Not Weird")


# In[4]:


#3 task. Arithmetic operators
a=int(input())
b=int(input())
print(a+b)
print(a-b)
print(a*b)


# In[5]:


#4 task. Arithmetic operators
a = int(input())
b = int(input())
print(a//b)
print(a/b)


# In[6]:


#5 task. Loop structure
n = int(input())
for i in range(n):
    print(i*i)


# In[ ]:




