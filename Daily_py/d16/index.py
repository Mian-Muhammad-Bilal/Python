x = int(input("Enter any number: "))
match x:
    case 0:
        print("x is zero")
    case 4 if x % 2 == 0:  # case with if-condition
        print("x % 2 == 0 and case is 4")
    case _ if x < 10:  # underscore use for default case...empty case with if-condition
        print("x is <= 10")
    case _:
        print(x)
