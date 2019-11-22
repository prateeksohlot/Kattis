
# coding: utf-8

# In[67]:


import sys

# Standard inputs
a = input()   #input here gives me a line
a = a.split() #we are saving it to variable a
# print(len(a))
x = int(a[0]) #typecasting mentioning explicitly what we want
y = int(a[1])
n = int(a[2])

for i in range(1,n+1):
    if i%x==0 and i%y==0:
        print("fizzbuzz")
    elif i%y ==0: 
        print("buzz")
    elif i%x==0:
        print("fizz")    
    else:
        print(i)
        








    
    


# In[ ]:




