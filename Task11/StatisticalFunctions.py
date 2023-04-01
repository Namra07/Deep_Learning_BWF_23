
# importing required packages
from scipy import stats as st
import numpy as np
random_array = np.random.randn(5,4)
#mean = random_array.mean()
print("Mean of matrix is : " , random_array.mean())
print("Sum of matrix is : " , random_array.sum())
print("Mode of matrix is : " , st.mode(random_array))
print("Mode of matrix is : " , random_array.quantile())

#axis argument \
# axis = 1
print("Mean of matrix is : " , random_array.mean(axis=1))

#axis = 0
print("Mean of matrix is : " , random_array.mean(axis=0))

print("Median of matrix is : " , random_array.std())

#boolean values
array = np.random.randn(100)
print(array)
print("Sum: ", (array > 0 ).sum())

bools = np.array([True,False,True,True])
print(bools.any())
print(bools.all())

#sorting array
array3 = np.random.randn(6)
print(array3)
print("Sorted array is : " , array3.sort())

