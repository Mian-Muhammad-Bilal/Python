import pandas as pd
ds = pd.read_csv(
    '/home/biologist/Documents/UMT/semmester5/code/AI/l13/emails_dataset.csv')
# count = ds.count()
# print(count)
# print('RAW')
# print(ds)
# # Preprocessing Tasks:
# ds.dropna(inplace=True)
# print('After Cleaning empty cells')
# print(ds)


# ds['spam'] = pd.to_numeric(ds['spam'])
# print('After formatting spam')
# print(ds)


# ds = ds[ds['text'].str.len() <= 200]
# print(ds)

# ds.drop_duplicates(subset=['text'], inplace=True)
# print('After droping duplicate cells')
# print(ds)

# Naive Bayes Classificat:

count = ds.count()
Total = count['spam']
# print(Total)

Spam = (ds['spam'] == 1).sum()
N_Spam = (ds['spam'] == 0).sum()

# print(f"Spam:{Spam} Not Spam: {N_Spam} Total: {Total}")
P_Spam = Spam / Total
P_N_Spam = 1 - P_Spam

# print(f"Probability of Spam: {P_Spam}")
# print(f"Probability of Not Spam: {P_N_Spam}")


# Concatenate all email texts into a single string
text = ' '.join(ds['text'])

# Spliting the text into words
words = text.split()

# Get unique words...means it will not take the duplicate words
vocabulary = set(words)
# print(vocabulary)

# Assuming you have the 'Spam' column in your DataFrame and 'vocabulary' is already calculated

# Create dictionaries to store counts for each word in spam and not spam emails
word_count_spam = {}
word_count_not_spam = {}

# Count occurrences of each word in spam and not spam emails
for index, row in ds.iterrows():
    words = row['text'].split()
    for word in words:
        # Increment count for the word based on the class
        if row['spam'] == 1:
            word_count_spam[word] = word_count_spam.get(word, 0) + 1
        else:
            word_count_not_spam[word] = word_count_not_spam.get(word, 0) + 1

# Calculate conditional probabilities for each word in the vocabulary
prob_word_given_spam = {word: (count + 1) / (sum(word_count_spam.values()) + len(
    vocabulary)) for word, count in word_count_spam.items()}
prob_word_given_not_spam = {word: (count + 1) / (sum(word_count_not_spam.values(
)) + len(vocabulary)) for word, count in word_count_not_spam.items()}

print(word_count_spam, word_count_not_spam)
