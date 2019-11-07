#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!/usr/bin/env python
# coding: utf-8

# In[4]:


import sympy as sym
sym.init_printing()
x = sym.symbols('x')

sym.Limit (1 / x, x, sym.oo)


# In[2]:


# In[2]:


print ("grup 1")
sym.Limit ((x**2-1)/ (x-1) ,x,1)


# In[3]:


print ("jawaban")
sym.Limit((x**2-1)/(x-1),x,1).doit()


# In[ ]:




