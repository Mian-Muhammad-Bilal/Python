try:
    l = [1, 2, 3, 4, 5]
    i = int(input("Enter the index: "))
    print(l[i])
except:
    print("Some error occurred")
finally:  # always run...functions ka return k bad bad b agar ya function ma huwa to run hoga but simple print run ni hoga...this is the difference
    print("Run in all situations")

# can use this instead of fianlly but no works in functions
print("Run in all situations")
