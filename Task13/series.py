import pandas as pd
import numpy as np
from pandas import Series,DataFrame
#index on left and coressponding values on right
obj = pd.Series([4,5,6,7,9])
print(obj)
#to print only values
print(obj.values)
#shows the iteration of index
print(obj.index)

#we can also assign the index
obj1 = pd.Series([3,5,7,9,34,67], index=['a','b','c','d','e','f'])
print(obj1)
print(obj1.index)
print(obj1['a'])
print(obj1[['c','e']])
print(obj1[obj1 > 10])
print(obj1 * 3)

#using numpy with series
print(np.exp(obj1))

#using booleans
print(56 in obj1)

#creating series using py dict
data = {'ali' : 20, 'Ahmed' : 25, 'Alia' : 18}
obj2 = pd.Series(data)
print("Dictionary in series is " , obj2)

#isnull notnull to detect missing data
print(pd.isnull(obj2))