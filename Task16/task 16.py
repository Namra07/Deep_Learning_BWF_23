import pandas as pd
import numpy as np

# Create two sample DataFrames
df1 = pd.DataFrame({'key': ['A', 'B', 'C', 'D'],
                    'value': np.random.randn(4)})
df2 = pd.DataFrame({'key': ['B', 'D', 'E', 'F'],
                    'value': np.random.randn(4)})

# Merge the DataFrames on the 'key' column
merged_df = pd.merge(df1, df2, on='key', how='outer')
print("Merged DataFrame:")
print(merged_df)

# Combine two sample DataFrames
df3 = pd.DataFrame({'key': ['C', 'D', 'E', 'F'],
                    'value2': np.random.randn(4)})
combined_df = pd.concat([df1, df3], axis=1)
print("\nCombined DataFrame:")
print(combined_df)

# Reshape data
df4 = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
                    'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
                    'C': np.random.randn(8),
                    'D': np.random.randn(8)})
print("\nOriginal DataFrame:")
print(df4)

# Pivot the DataFrame
pivoted_df = df4.pivot_table(values='C', index=['A'], columns=['B'])
print("\nPivoted DataFrame:")
print(pivoted_df)

# Stack the pivoted DataFrame
stacked_df = pivoted_df.stack()
print("\nStacked DataFrame:")
print(stacked_df)
