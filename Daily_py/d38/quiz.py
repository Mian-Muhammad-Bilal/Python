a = input("Enter any value between 1 and 9: ")

if (a == "quit"):
    print("Good to go")
else:
    a = int(a)
    if (a < 1 or a > 9):
        raise ValueError("Number should be between 1 and 9")
    else:
        print("Good to go")
