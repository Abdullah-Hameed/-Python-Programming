#!/usr/bin/env python
# coding: utf-8

# In[1]:


#create a list with duplicate values
my_list = [2,5,1,7,2,8,9,1,3,5]
size_of_my_list = len(my_list) 
duplicate_values = [] 
for i in range(size_of_my_list): 
    k = i + 1
    for j in range(k, size_of_my_list): 
        if my_list[i] == my_list[j] and my_list[i] not in duplicate_values: 
            duplicate_values.append(my_list[i])
print(duplicate_values)


# In[ ]:




