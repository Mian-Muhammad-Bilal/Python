import pandas as pd

# Read the dataset
ds = pd.read_csv(
    '/home/biologist/Documents/UMT/semmester5/code/AI/l13/emails_dataset.csv')

# Preprocessing Tasks:
# 1. Drop empty cells
ds.dropna(inplace=True)

# 2. Format 'spam' column as numeric
ds['spam'] = pd.to_numeric(ds['spam'])

# 3. Filter out emails with text length <= 200
ds = ds[ds['text'].str.len() <= 200]

# 4. Drop duplicate emails
ds.drop_duplicates(subset=['text'], inplace=True)

# Naive Bayes Classification:
# 1. Calculate the probabilities of spam and not spam
total_emails = len(ds)
spam_emails = (ds['spam'] == 1).sum()
not_spam_emails = (ds['spam'] == 0).sum()

P_spam = spam_emails / total_emails
P_not_spam = not_spam_emails / total_emails

# print(f"Probability of Spam: {P_spam}")
# print(f"Probability of Not Spam: {P_not_spam}")

# 2. Concatenate all email texts into a single string
text = ' '.join(ds['text'])

# Split the text into words
words = text.split()

# Get unique words (vocabulary)
vocabulary = set(words)
# print(vocabulary)

# Calculate conditional probabilities of each word given spam or ham
word = 'money'

# Count occurrences of word in spam emails
spam_word_count = ds[ds['text'].str.contains(
    word) & (ds['spam'] == 1)].shape[0]

# Count occurrences of word in ham emails
ham_word_count = ds[ds['text'].str.contains(word) & (ds['spam'] == 0)].shape[0]

# Calculate conditional probabilities
P_word_given_spam = spam_word_count / spam_emails
P_word_given_ham = ham_word_count / not_spam_emails

print(f"P(word = {word} | spam) = {P_word_given_spam:.4f}")
print(f"P(word = {word} | ham) = {P_word_given_ham:.4f}")
