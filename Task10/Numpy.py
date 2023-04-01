import numpy as np
data1 = [6,7.7,8,0,1]
arr1 = np.array(data1)
print(arr1)
print(arr1.ndim)
print(arr1.dtype)

data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr2 = np.array(data2)
print(arr2)
print(arr2.ndim)
print(arr2.dtype)
print(arr2.shape)

#zeros in py 1D
arr3 = np.zeros(10)
print(arr3)

#3D 
arr4 = np.zeros((3,4))
print(arr4)

#range function
arr5 = np.arange(10)
print(arr5)

#dataTypes
print(arr5.dtype)

#Arithmetic with Numpy Arrays
array1 = np.array([[1,2,3,4],[4,6,7,8]])
array2 = np.array([[3,6,7,8],[2,5,8,4]])
#array3 = np.array(array1*array2)
print("Multiplication of 2 arrays is" , array1*array2)
print("Division of 2 arrays is" , array1/array2)
print("Subtraction of 2 arrays is" , array1-array2)
print("Addition of 2 arrays is" , array1+array2)
