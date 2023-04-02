import pandas as pd
from pandas import Series,DataFrame
data = {'state' : ['Ohio', 'Ohio' , 'Ohio', 'NewYork','NewYork','NewYork'],
        'year' : [2000,2007,2005,2008,2009,2006],
        'pop' : [1.5,1.9,1.9,1.6,1.4,1.2]}
#represents data in rectangular table form
print(pd.DataFrame(data))
print(DataFrame(data).head())

#can change the order of columns
print(pd.DataFrame(data, columns=['year','pop','state']))

#can name the index too
print(pd.DataFrame(data, columns=['year','pop','state'], index=[1,2,3,4,5,6]))

#can print individual columns too
print(pd.DataFrame(data['state']))

#deleting columns
del data['pop']
print(pd.DataFrame(data))



