import numpy as np
import pandas as pd
from pandas import Series,DataFrame
#fetching data from matches.csv file
data = pd.read_csv('matches.csv')
print(data)

#showing data preview 
#first five rows
print(data.head())

#last five rows
print(data.tail())

#knowing the info of data
print(data.info())

#for working on numerical values
print(data.describe())

data = pd.read_table('matches.csv')
print(data)


