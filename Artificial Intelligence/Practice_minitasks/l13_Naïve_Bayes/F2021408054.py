import pandas as pd
ds = pd.read_csv(
    '/home/biologist/Documents/UMT/semmester5/code/AI/l13/emails_dataset.csv')
# count = ds.count()
# print(count)
print('RAW')
print(ds)

# Preprocessing Tasks:
# 1
ds.dropna(inplace=True)
print('After Cleaning empty cells')
print(ds)

# 2
ds['spam'] = pd.to_numeric(ds['spam'])
print('After formatting spam')
print(ds)

# 3
ds = ds[ds['text'].str.len() <= 200]
print(ds)

# 4
ds.drop_duplicates(subset=['text'], inplace=True)
print('After droping duplicate cells')
print(ds)

# Naive Bayes Classificat:

# 1
count = ds.count()
Total = count['spam']
print(Total)

Spam = (ds['spam'] == 1).sum()
N_Spam = (ds['spam'] == 0).sum()

print(f"Spam:{Spam} Not Spam: {N_Spam} Total: {Total}")
P_Spam = Spam / Total
P_N_Spam = 1 - P_Spam

print(f"Probability of Spam: {P_Spam}")
print(f"Probability of Not Spam: {P_N_Spam}")


# 2
# Concatenate all email texts into a single string
text = ' '.join(ds['text'])
# Spliting the text into words
words = text.split()
# Get unique words...means it will not take the duplicate words
vocabulary = set(words)
print(vocabulary)


# 3
