#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
Python code:
Incremental search method
'''
""" An incremental search algorithm """
import numpy as np


# In[2]:


def incremental_search(f, a, b, dx):
    """
    :param f: The function to solve
    :param a: The left boundary x-axis value
    :param b: The right boundary x-axis value
    :param dx: The incremental value in searching
    :return: The x-axis value of the root,
                number of iterations used
    """
    fa = f(a)    
    c = a + dx 
    fc = f(c)    
    n = 1
 
    while np.sign(fa) == np.sign(fc):
        if a >= b:
            return a - dx, n
        
        a = c
        fa = fc
        c = a + dx
        fc = f(c)
        n += 1
 
    if fa == 0:
        return a, n
    elif fc == 0:
        return c, n
    else:
        return (a + c)/2., n


# In[3]:


y = lambda x: x**3 + 2.0*x**2 - 5


# In[4]:


root, iterations = incremental_search(y, -5., 5., 0.001)


# In[8]:


print("Root is:", root)
print("Iterations:", iterations)

