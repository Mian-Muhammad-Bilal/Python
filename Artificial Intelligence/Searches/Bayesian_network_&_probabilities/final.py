# Making Tables from the given values in dictionary data structures

P_Rain = {'True': 0.3, 'False': 0.7}

P_Umbrella_given_Rain = {
    ('True', 'True'): 0.9,
    ('True', 'False'): 0.1,
    ('False', 'True'): 0.2,
    ('False', 'False'): 0.8
}

P_Grass_given_Umbrella = {
    ('True', 'True'): 0.8,
    ('True', 'False'): 0.2,
    ('False', 'True'): 0.1,
    ('False', 'False'): 0.9
}

###Questions:
###a)What is the probability of Rain being True given that Umbrella is False?

P_Rain_given_Umbrella_False = (P_Rain['True'] * P_Umbrella_given_Rain[('True', 'False')]) / P_Umbrella_given_Rain[('False', 'False')]
print(f"a. P(Rain=True | Umbrella=False) = {P_Rain_given_Umbrella_False:.2f}")

#====================================================================================================================================

###b)P(Rain = True, Umbrella = True)

P_Rain_Umbrella_True = P_Rain['True'] * P_Umbrella_given_Rain[('True', 'True')]
print(f"b. P(Rain=True, Umbrella=True) = {P_Rain_Umbrella_True:.2f}")

#====================================================================================================================================

###c)P(Rain = True, Umbrella = False)

P_Rain_Umbrella_False = P_Rain['True'] * \ P_Umbrella_given_Rain[('True', 'False')]
print(f"c. P(Rain=True, Umbrella=False) = {P_Rain_Umbrella_False:.2f}")

#====================================================================================================================================

###d)P(Rain = False, Umbrella = True)

P_NoRain_Umbrella_True = P_Rain['False'] * \ P_Umbrella_given_Rain[('False', 'True')]
print(f"d. P(Rain=False, Umbrella=True) = {P_NoRain_Umbrella_True:.2f}")

#====================================================================================================================================

###e)P(Rain = False, Umbrella = False)

P_NoRain_Umbrella_False = P_Rain['False'] * \ P_Umbrella_given_Rain[('False', 'False')]
print(f"e. P(Rain=False, Umbrella=False) = {P_NoRain_Umbrella_False:.2f}")

#====================================================================================================================================

###f)Find the probability of Umbrella being True given that Rain is False.

P_Umbrella_given_NoRain = (P_Rain['False'] * P_Umbrella_given_Rain[('False', 'True')]) / P_Rain['False']
print(f"f. P(Umbrella=True | Rain=False) = {P_Umbrella_given_NoRain:.2f}")

#====================================================================================================================================

###g)P(Grass = True | Umbrella = True) 

P_Grass_True_Umbrella_True = P_Grass_given_Umbrella[('True', 'True')] * P_Umbrella_given_Rain[('True', 'True')]
print(f"g. P(Grass=True | Umbrella=True) = {P_Grass_True_Umbrella_True:.2f}")

#====================================================================================================================================

###h)P(Grass = False | Umbrella = False)

P_Grass_False_Umbrella_False = P_Grass_given_Umbrella[('False', 'False')] * P_Umbrella_given_Rain[('False', 'False')]
print(f"h. P(Grass=False | Umbrella=False) = {P_Grass_False_Umbrella_False:.2f}")

#====================================================================================================================================

###i) Determine the probability of Grass being False given that Umbrella is False.

P_Grass_False_Umbrella_False = P_Grass_given_Umbrella[('False', 'False')] * P_Umbrella_given_Rain[('False', 'False')]
print(f"i. P(Grass=False | Umbrella=False) = {P_Grass_False_Umbrella_False:.2f}")

#====================================================================================================================================

###j)Suppose you observe that the Grass is True. What is the probability that it is raining?
#we will use use Bayes' Theorem

P_Rain_Given_Grass_True = (P_Rain['True'] * P_Grass_given_Umbrella[('True', 'True')]) / P_Grass_True_Umbrella_True
print(f"j. Probability that it's raining is {P_Rain_Given_Grass_True:.2f}")
