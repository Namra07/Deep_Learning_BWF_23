import numpy as np

# Dot Product
arr1 = np.array([[2,5,78],[5,89,45]])
arr2 = np.array([[2,6],[7,90],[45,78]])
print("Dot product of two matrices is : \n" ,arr1.dot(arr2))

from numpy.linalg import inv,qr
x = np.random.rand(5,5)
print("5 x 5 matrix" , x)
mat = x.dot(x)
mat2 = x.T.dot(x)     #dot product with transpose of a matrix
print("Inverse of matrix\n " , inv(mat))
print("Dot product with Transpose of matrix\n " , mat2)


#Pseudorandom Number Generation
random_array = np.random.normal(size=(3,3))
print("Array Generated using random number\n",random_array)

random_array2 = np.random.randint(10,size=(5,5))
print(random_array2)

array3 = np.eye(5)
print("Matrix with 1's in diagonal and 0's in other places\n",array3)

#identity matrix
identity_array = np.identity(4)
print("4 x 4 identity matrix is\n",identity_array)
