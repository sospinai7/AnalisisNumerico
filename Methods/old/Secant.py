#!/usr/bin/env python
# coding: utf-8

# In[1]:


""" The secant root-finding method """


def secant(f, a, b, tol=0.001, maxiter=100):
    """
    :param f: The function to solve
    :param a: Initial x-axis guess value
    :param b: Initial x-axis guess value, where b>a
    :param tol: The precision of the solution
    :param maxiter: Maximum number of iterations
    :return: The x-axis value of the root,
                number of iterations used
    """
    n = 1
    while n <= maxiter:
        c = b - f(b)*((b-a)/(f(b)-f(a)))
        if abs(c-b) < tol:
            return c, n

        a = b
        b = c
        n += 1

    return None, n


# In[3]:


y = lambda x: x**3 + 2*x**2 - 5
root, iterations = secant(y, -5.0, 5.0, 0.00001, 100)
print("Root is:", root)
print("Iterations:", iterations)

