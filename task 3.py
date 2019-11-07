#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sympy as sym
sym.init_printing()
a, b, x, y, z, t, w, = sym.symbols('a b x y z t w')


# In[3]:


print ('1')
sym.Integral (4*x**6-2*x**3+7*x-4)


# In[4]:


print ('jawaban')
sym.integrate (4*x**6-2*x**3+7*x-4)


# In[5]:


print ('6')
sym.Integral (3*sym.sqrt(w)+10*sym.sqrt(w**3))


# In[6]:


print ('6')
sym.integrate (3*sym.sqrt(w)+10*sym.sqrt(w**3))


# In[7]:


print ('11')
sym.Integral (sym.sqrt(z)*(z**2-1/(4*z)))


# In[8]:


print ('11')
sym.integrate (sym.sqrt(z)*(z**2-1/(4*z)))


# In[1]:


print ('16')
sym.Integral (12 + csc(x)*(sin(x)+csc(x)))


# In[ ]:





# In[ ]:





# In[ ]:




