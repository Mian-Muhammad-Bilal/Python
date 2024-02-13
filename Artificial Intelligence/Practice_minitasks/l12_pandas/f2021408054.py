# # Q1
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(
    '/home/biologist/Documents/UMT/semmester5/code/AI/l12/data.csv')

# practice
# print(df['Age'])
# ndf = df.drop(10, axis=0)
# print(ndf)
# ndf = df.drop('Age', axis=1)
# print(ndf)
# print(df[df['Age'] <= 40.0])
# # Q2:skipped
# Read the CSV file
df = pd.read_csv(
    "/home/biologist/Documents/UMT/semmester5/code/AI/l12/dist_data.csv")

# Calculate and save the marginal distributions
marginal_distributions = df.apply(pd.Series.value_counts)
marginal_distributions.to_csv("marginal_distributions.csv")

# Calculate and save the conditional distributions
conditional_distributions = df.groupby(
    ["Age", "Salary"]).size().reset_index(name="Count")
conditional_distributions.to_csv("conditional_distributions.csv")


# # Handling Empty Cells

# df = pd.read_csv('data.csv')
# print(df)
# df = df.dropna()
# print('After Cleaning empty cells')
# print(ndf)


# # Handling Data in the Wrong Format

# df['Salary'] = pd.to_numeric(df['Salary'])
# print(df)


# # Handling Wrong Data

# for x in df.index:
#     if df.loc[x, 'Age'] > 40.0:
#         df.drop(x, inplace=True)
# print(df)


# # Handling Duplicates

# df.drop_duplicates(subset=['Name'], inplace=True)
# print(df)

# # Q2:skipped
# Read the CSV file


# # Q3
# df.plot(kind='bar', title='Dataset After Handling Empty Cells')
# plt.show()

# df['Age'].plot(kind='hist', title='Distribution of Ages')
# plt.show()


# df['Gender'].value_counts().plot(kind='pie', title='Distribution of Gender')
# plt.show()
