#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().system('pip install numpy')


# # Q1: Import the numpy package under the name np

# In[2]:


import numpy as np


# # Q2: Create a null vector of size 10

# In[6]:


x = np.zeros(10)
print(x)


# # Q3: Create a vector with values ranging from 10 to 49

# In[10]:


a = np.arange(10, 50)
print(a)


# 
# # Q4: Find the shape of previous array in question 3

# In[14]:


print("Shape of Range is :", a.shape)


# # Q5: Print the type of the previous array in question 3

# In[19]:


print(a.dtype)


# # Q6: Print the numpy version and the configuration

# In[24]:


print(np.__version__)


# In[27]:


print(np.show_config())


# # Q7: Print the dimension of the array in question 3

# In[28]:


print(a.ndim)


# # Q8: Create a boolean array with all the True values

# In[30]:


np.full((3,3), True)


# # Q9: Create a two dimensional array

# In[33]:


arr1 = np.arange(36).reshape(6 , 6)
print(arr1)


# # Q10: Create a three dimensional array

# In[37]:


arr2 = np.arange(27).reshape(3 , 3 , 3)
print(arr2)


# In[38]:


arr2 = np.arange(64).reshape(4 , 4 , 4)
print(arr2)


# # Q11: Reverse a vector (first element becomes last)

# In[6]:


arr3 = np.array([1,2,3,4,5,6])
print("Orriginal Array : ")
print(arr3)

print("Reversed Array")
y = arr3[:: -1]
print(y)


# # Q12: Create a null vector of size 10 but the fifth value which is 1

# In[12]:


arr4 = np.zeros(10)
print("Original array: ")
print(arr4)

print("Update 5th Index: ")
arr4[5] = 1
print(arr4)


# # Q13: Create a 3x3 identity matrix

# In[15]:


arr5 = np.identity(3)
print("3 x 3 Matrix ")

print(arr5)


# # Q14 : Convert the data type of the given array from int to float

# In[21]:


arr = np.array([1,2,3,4,5])
print(arr)

arr.astype(float)


# # Q15: Multiply arr1 with arr2

# In[27]:


arr1 = np.array([[1., 2., 3.], [4., 5., 6.]]) 
arr2 = np.array([[0., 4., 1.], [7., 2., 12.]])
print(arr1)
print(arr2)

print("Multiplying two arrays")
np.multiply(arr1 , arr2)


# # Q16: Make an array by comparing both the arrays provided above

# In[8]:


arr1 = np.array([[1., 2., 3.], [4., 5., 6.]]) 
arr2 = np.array([[0., 4., 1.], [7., 2., 12.]])
print(arr1)
print(arr2)
arr3 = (arr1 != arr2).all()
print(arr3)


# # Q17: Extract all odd numbers from arr with values(0-9)

# In[15]:


arr1 = np.array([1,2,3,4,5,6,7,8,9])
print(arr1)

print("Odd Number ")
odd = (arr1[arr1 % 2 == 1])
print(odd)


# # Q18: Replace all odd numbers to -1 from previous array

# In[21]:


arr1 = np.array([1,2,3,4,5,6,7,8,9])
print(arr1, "\n")
print("Replaced Values", "\n")
arr1[arr1 % 2 == 1] = -1
print(arr1)


# # Q19: Replace the values of indexes 5,6,7 and 8 to 12

# In[22]:


arr = np.arange(10)
print(arr, "\n")
print("Replaced Values", "\n")
arr[5 : 9] = 12
print(arr)


# # Q20 : Create a 2d array with 1 on the border and 0 inside

# In[25]:


arr = np.ones((6,6))
print("Original array : ", "\n")
print(arr, "\n" )
print("1 on the border and 0 inside in the array", "\n")
arr[1:-1, 1:-1] = 0
print(arr)


# # Q21: Replace the value 5 to 12

# In[21]:


arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d, "\n")
print("Replacing 5 with 12" , "\n")
arr2d[1 , -2] = 12
print(arr2d)


# # Q22: Convert all the values of 1st array to 64

# In[13]:


arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr3d)
arr3d[0 , -2].astype('int64')


# # Q23: Make a 2-Dimensional array with values 0-9 and slice out the first 1st 1-D array from it

# In[18]:


arr2d = np.array([[0,1,2,3,4] , [5,6,7,8,9]])
print(arr2d , "\n")
print("Slicing 1-D Array" , "\n")
arr2d[0]


# # Q24: Make a 2-Dimensional array with values 0-9 and slice out the 2nd value from 2nd 1-D array from it

# In[24]:


arr2d = np.array([[0,1,2,3,4] , [5,6,7,8,9]])
print(arr2d , "\n")
print("Slicing 2nd value from 2nd 1-D Array" , "\n")
arr2d[1, 1]


# # Q25: Make a 2-Dimensional array with values 0-9 and slice out the third column but only the first two rows

# In[ ]:





# # Q26: Create a 10x10 array with random values and find the minimum and maximum values

# In[30]:


arr = np.random.rand(10 ,10)

print(arr , "\n")

max_element = np.max(arr)
min_element = np.min(arr)

print("Maximum value = " , max_element ,  "\n")
print("Minimum value = " , min_element )


# # Q27: Find the common items between a and b

# In[34]:


a = np.array([1,2,3,2,3,4,3,4,5,6]) 
b = np.array([7,2,10,2,7,4,9,4,9,8])

print(a)
print(b , "\n")

print("Common Values", "\n")
print(np.intersect1d(a , b))


# # Q28: Find the positions where elements of a and b match

# In[35]:


a = np.array([1,2,3,2,3,4,3,4,5,6]) 
b = np.array([7,2,10,2,7,4,9,4,9,8])

print(a)
print(b , "\n")


# # Q29: Find all the values from array data where the values from array names are not equal to Will

# In[9]:


names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe']) 
data = np.random.randn(7, 4 )

print(names)
print(data)


# In[ ]:




