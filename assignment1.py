#!/usr/bin/env python
# coding: utf-8

# # Assignment 1

# ## Test your knowledge. 
# 
# ** Answer the following questions **

# ## Strings

# Given the string 'hello' give an index command that returns 'e'. Enter your code in the cell below:

# In[1]:


s = 'hello'
# Print out 'e' using indexing
print(s[1])


# Reverse the string 'hello' using slicing:

# In[2]:


s ='hello'
# Reverse the string using slicing
print(s[::-1])


# Given the string hello, give two methods of producing the letter 'o' using indexing.

# In[3]:


s ='hello'
# Print out the 'o'

# Method 1:
print(s[-1])


# In[5]:


# Method 2:
print(s[4])


# ## Lists

# Build this list [0,0,0] two separate ways.

# In[7]:


# Method 1:
my_list = [0] * 3
print(my_list)


# In[8]:


# Method 2:
my_list = [0 , 0 , 0]
print(my_list)


# Reassign 'hello' in this nested list to say 'goodbye' instead:

# In[9]:


list3 = [1,2,[3,4,'hello']]

list3[2][2] = "goodbye"
list3


# Sort the list below:

# In[11]:


list4 = [5,3,4,6,1]
list4.sort()
list4


# ## Dictionaries

# Using keys and indexing, grab the 'hello' from the following dictionaries:

# In[13]:


d = {'simple_key':'hello'}
# Grab 'hello'
grab1 = d['simple_key']
print(grab1)


# In[16]:


d = {'k1':{'k2':'hello'}}
# Grab 'hello'
grab2 = d["k1"]['k2']
print(grab2)


# In[19]:


d = {'k1':[{'nest_key':['this is deep',['hello']]}]}

#Grab hello
grab3 = d["k1"][0]['nest_key'][1][0]
grab3


# In[22]:


d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
#Grab hello
grab4 = d['k1'][2]['k2'][1]['tough'][2][0]
grab4


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ** Given the variables:**
# 
#     planet = "Earth"
#     diameter = 12742
# 
# ** Use .format() to print the following string: **
# 
#     The diameter of Earth is 12742 kilometers.

# In[23]:


planet = "Earth"
diameter = '12742'
print('the diameter of {} is {} kilometers'.format(planet , diameter))


# ** Given this nested list, use indexing to grab the word "hello" **

# In[25]:


lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]


# In[27]:


lst[3][1][2][0]


# ** Given this nested dictionary grab the word "hello". **

# In[28]:


d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}


# In[34]:


grab6 = d['k1'][3]['tricky'][3]['target'][3]
grab6


# ### Write a Python program to swap two variables.
# 

# In[35]:


a = 5
b = 10

temp = a
a = b
b = temp

print("After swapping:")
print("a =", a)
print("b =", b)


# ## Thanks

# In[ ]:




