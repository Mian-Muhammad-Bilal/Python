import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# Handling Empty Cells
df = pd.read_csv('data.csv')

# new_df = df.dropna()
# print(df)
# print('After Cleaning empty cells')
# print(new_df)
# Handling Data in the Wrong Format

# df['Salary'] = pd.to_numeric(df['Salary'])
# print(df)
# Handling Wrong Data
# for x in df.index:
#     if df.loc[x, 'Age'] > 40.0:
#         df.drop(x, inplace=True)
# print(df)
# Handling Duplicates
# df.drop_duplicates(inplace=True)
# df.drop_duplicates(subset=['Name'], inplace=True)

# print(df)


# Plotting dataset after handling empty cells
df.plot(kind='bar', title='Dataset After Handling Empty Cells')
plt.show()

df.plot(kind='hist', title='Distribution of Ages')
plt.show()


df.plot(kind='pie', title='Distribution of Gender')
plt.show()
