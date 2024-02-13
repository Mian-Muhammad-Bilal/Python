import pandas as pd
import numpy as np
import pandas as pd

Ds = pd.read_csv(
    '/home/biologist/Documents/UMT/semmester5/code/AI/l14_final/emails_dataset.csv')


# ## 1=========================
# empty cells
e_Ds = Ds.dropna(inplace=True)

# duplicates cells
d_Ds = Ds.drop_duplicates(inplace=True)


# ## 2=========================
# prob of span
total = Ds['spam'].count()
# print(total)

spam = (Ds['spam'] == 1).sum()
# print(spam)

P_spam = spam / total
# print(P_spam)

# prob of not span
not_spam = (Ds['spam'] == 0).sum()
# print(not_spam)

P_notspam = not_spam / total
# print(P_notspam)


# ##3=========================

text = ' '.join(Ds['text'])
words = text.split()
lst = set(words)

notspan = len(Ds) - total
p_dollar_spam = Ds.loc[Ds['spam'] == 1, '$'].sum() / total
p_free_spam = Ds.loc[Ds['spam'] == 1, 'free'].sum() / total
p_dollar_not_spam = Ds.loc[Ds['spam'] == 0, '$'].sum() / notspan
p_free_not_spam = Ds.loc[Ds['spam'] == 0, 'free'].sum() / notspan

print(p_dollar_spam)
print(p_free_spam)
print(p_dollar_not_spam)
print(p_free_not_spam)


q4_1 = P_spam * p_dollar_spam * p_free_spam

q4_2 = P_notspam * p_dollar_not_spam * p_free_not_spam
