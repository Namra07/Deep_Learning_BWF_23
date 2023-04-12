import pandas as pd
import numpy as np

# Create a sample DataFrame with missing data
df = pd.DataFrame({'A': [1, 2, np.nan, 4],
                   'B': [5, np.nan, 7, 8],
                   'C': [np.nan, 10, 11, 12],
                   'D': [13, 14, 15, np.nan]})
print("Original DataFrame:")
print(df)

# Handling missing data
# Count the number of missing values in each column
print("\nMissing values in each column:")
print(df.isnull().sum())

# Fill missing values with the mean of each column
df.fillna(df.mean(), inplace=True)
print("\nDataFrame after filling missing values:")
print(df)

# Replacing values
# Replace all values greater than or equal to 10 with 10
df.replace(to_replace=df[df>=10], value=10, inplace=True)
print("\nDataFrame after replacing values:")
print(df)

# Removing duplicates
df.drop_duplicates(inplace=True)
print("\nDataFrame after removing duplicates:")
print(df)

# Detecting and removing outliers
# Calculate the z-score for each value in each column
z_scores = (df - df.mean()) / df.std()
# Threshold for identifying outliers (3 standard deviations from the mean)
threshold = 3
# Identify and remove all outliers
df = df[(np.abs(z_scores) < threshold).all(axis=1)]
print("\nDataFrame after removing outliers:")
print(df)
