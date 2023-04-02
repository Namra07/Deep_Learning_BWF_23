import numpy as np

#scalar value 4 has been broadcast to all of the other elements in the multiplication operation.
arr = np.array([1,2,3,4,5])
scalar_product = arr * 4
print("Scalar product of matrix is : " , scalar_product)


#demean
arr1 = np.random.randn(3,2)
column_mean = arr1.mean(0)
demeaned = arr1 - column_mean
print("Demeaned column are : " , demeaned)


#broadcasting Rules
# RULE 1 if 1 row in matrix A then columns of both column_A == column_B & vice versa
arr_A = np.random.randn(1,3)
arr_B = np.random.randn(4,3)
sum = arr_A + arr_B
print("Sum of two matrix is : " , sum)

#RULE 2 same matrices can be broadcasted smoothly
arr3 = np.random.randn(2,4)
arr4 = np.random.randn(2,4)
multiply = arr3 * arr4
print("Multiplication of two matrices that are broadcasted is " , multiply)

#RULE 3 if we perform any arithmetic operation on these two it'll trough error
arr_C = np.random.randn(1,4)
arr_D = np.random.randn(3,2)

#RULE 4 in this case corresponding should be same
array1 = np.random.randn(1,3)
array2 = np.random.randn(3,1)
divide = array1 / array2
print("Division of two matrices is " , divide)

