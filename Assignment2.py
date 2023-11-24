#!/usr/bin/env python
# coding: utf-8

# In[3]:


# 1. write a python code to add to a tuple.
countries_tuple = ("egypt", "russia", "morocco", "tunisia", "turkey")
countries_list = list(countries_tuple)
print(countries_list)
countries_list.append("japan")
print(countries_list)
countries_tuple = tuple[countries_list]
print(countries_tuple)


# In[4]:


# 2. write a python code to print the sum of a list.
my_list = [1, 2, 3, 4, 5]
total = sum(my_list)
print("The sum of the items in the list is:", total)


# In[6]:


# 3. Write a Python program to multiply all the items in a list.
import math 
list_mul = [1 , 2 , 3 , 4 , 4 , 5 , 1]
product = math.prod(list_mul)
print(product)


# In[27]:


# 4. Write a Python program to get the smallest number from a list.
search_list = [0 , -1 , 32 , 5 , 65 , 3 , 5 ]
smallest_number = 10000
for number in search_list:
    if number < smallest_number:
        smallest_number = number
print("The smallest number in the list is:", smallest_number)


# In[30]:


# 5. Write a Python program to get the largest number from a list.
search_list2 = [0 , -1 , 32 , 5 , 65 , 3 , 5 ]
largest_number = 0
for number in search_list2:
    if number > largest_number:
        largest_number = number
print("The largest number in the list is:", largest_number)


# In[33]:


# 6. Write a Python program to count the number of strings from a given list of strings.
count_list = ['abdallah' , 2 , 3 , 'cake' , 'amit' , 6 , 'money' , 'real madrid']
counter = 0
for String in count_list :
    if type(String) == str :
        counter += 1
print ('the number of strings in the list is ' , counter)


# In[34]:


# 7. Write a Python program to clone or copy a list.
original_list = [ 1 , 1 , 2 , 'boody' , 'cake' , 'joe']
copied_list = original_list.copy()
print("original list is " , original_list )
print("copied list is " , copied_list )


# In[35]:


# 8. Write a Python program to remove item(s) from a given set.
fruits = {"apple", "banana", "cherry"}
print(fruits)
fruits.remove("cherry")
print(fruits)


# In[46]:


# 9. Write a Python program to check if a set is a subset of another set.
fruits = {"apple" , "banana" , "cherry" , "orange"}
some_fruits = {"apple" , 'cherry'}
is_subset = True
for element in some_fruits:
    if element not in fruits:
        is_subset = False
        break 
if is_subset:
    print("set1 is a subset of set2.")
else:
    print("set1 is not a subset of set2.")


# In[52]:


# 10. Write a Python program to remove all elements from a given set.
my_set = {1 , 1 , 4 , 42 , 42 , 5 , 6 , 7 , 0 }
my_set.clear()
print(my_set)


# In[54]:


# 11. Write a Python program to find the maximum and minimum values in a set.
search_set = {0 , -1 , 32 , 5 , 65 , 3 , 5 }
largest_number = 0
smallest_number = 10000
for number in search_set:
    if number > largest_number:
        largest_number = number
    elif number < smallest_number :
        smallest_number = number
print("The largest number in the set is:", largest_number)
print("The smallest number in the set is:", smallest_number)


# In[55]:


12. Write a Python program to find the index of an item in a tuple.
search_tuple = (10, 20, 30, 40, 50)
item_to_find = 20
index = search_tuple.index(item_to_find)
print("the index is " , index)


# In[59]:


# 13. Write a Python program to convert a tuple to a dictionary.
my_tuple = (("a", 1), ("b", 2), ("c", 3), ("d",4))
my_dictionary = dict(my_tuple)
print (my_dictionary)


# In[60]:


# 14. Write a Python program to unzip a list of tuples into individual lists.


# In[61]:


# 15. Write a Python program to reverse a tuple.


# In[62]:


# 16. Write a Python program to convert a list of tuples into a dictionary.


# In[66]:


# 17. Write a Python program to replace the last value of tuples in a list.
#Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)] 
#Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]
# Sample list of tuples


sample_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
new_value = 100
updated_list = [tuple(x[:-1] + (new_value,)) for x in sample_list]
print(updated_list)


# In[ ]:


# 18. Write a Python program to sort a tuple by its float element.

