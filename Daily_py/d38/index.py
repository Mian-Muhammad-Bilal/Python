a = int(input("Enter any value between 1 and 9: "))

if (a < 1 or a > 9):
    raise ValueError("Number should be between 1 and 9")
else:
    print(f"The value of a is: {a}")
