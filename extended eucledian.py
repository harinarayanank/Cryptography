#!/usr/bin/env python
# coding: utf-8

# In[1]:


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

print (egcd(53947^-1, 56211))

print(egcd(19385^-1, 43159))


# In[ ]:




