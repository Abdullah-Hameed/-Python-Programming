#!/usr/bin/env python
# coding: utf-8

# In[6]:


val1 = input("Enter first value")
val2 = input("Enter second value")
operator = input("Enter Operator")

val1 = int(val1)
val2 = int(val2)
if operator == "+":
    val = val1 + val2
    print(val, "answer")
elif operator == "-":
    val = val1 - val2 
    print(val, "answer")
elif operator == "*":
    val = val1 * val2 
    print(val, "answer")
elif operator == "/":
    val = val1 / val2 
    print(val, "answer")
elif operator == "**":
    val = val1 ** val2 
    print(val, "answer")     
else:
    print("Enter correct operator")


# In[ ]:





# In[ ]:




