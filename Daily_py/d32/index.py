s1 = {0, 2, 4, 5}
s2 = {5, 6, 8, 10}
# print(s1.union(s2))  # the values remain unchanged
# print(s1, s2)

# update...if want to update
# s1.update(s2)
# print(s1, s2)

# intersection
# union

# semitric difference_wo values jo commen nhi hain
# s3 = s1.symmetric_difference(s2)
# print(s3)

# difference(jo pehly ma ha dusry ma ni ha) and difference.update
s3 = s1.difference(s2)
print(s3)


# isdisjoint(koi intersection na ho)
print(s1.isdisjoint(s2))

# issuperset()
print(s1.issuperset(s1))

# add
print(s1)
s1.add(15)
print(s1)

# remove
print(s1)
s1.remove(15)
print(s1)
# agar 15 ho he na to remove k sath error a jay ga but discard k sath ni
# discard
print(s1)
s1.discard(15)
print(s1)

# pop...removed the last value but dont know that value bcz set is unordered

s3 = s1.pop()
print(s3)

# del
del s3
# print(s3)

# clear if want to cler the set not del
s1.clear()
print(s1)
