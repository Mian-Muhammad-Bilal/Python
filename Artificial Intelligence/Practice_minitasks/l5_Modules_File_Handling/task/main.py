import calculator
print('''Welcome to the calculator!!!
Which type of calculation do you want to perform?
A - Basic
B - Scientific
C - Conversion''')

choice = input("Select A, B, or C: ")

if choice == 'A':
    print('''Which basic calculation do you want to perform?
    A - Addition
    B - Subtraction
    C - Multiplication
    D - Division''')

    Achoice = input("Select A, B, C, or D: ")

    if Achoice == 'A':
        add1 = int(input("Enter the first number you want to add: "))
        add2 = int(input("Enter the second number you want to add: "))
        result = calculator.basic.add(add1, add2)
        print("Result: ", result)

    elif Achoice == 'B':
        sub1 = int(input("Enter the first number you want to subtract: "))
        sub2 = int(
            input("Enter the second number from which you want to subtract: "))
        result = calculator.basic.sub(sub1, sub2)
        print("Result: ", result)

    elif Achoice == 'C':
        mul1 = float(input("Enter the first number you want to multiply: "))
        mul2 = float(
            input("Enter the second number with which you want to multiply: "))
        result = calculator.basic.mul(mul1, mul2)
        print("Result: ", result)

    elif Achoice == 'D':
        div1 = float(input("Enter the divisor: "))
        div2 = float(input("Enter the dividend: "))
        if div2 == 0:
            print("Cannot divide by zero.")
        else:
            result = calculator.basic.division(div1, div2)
            print("Result: ", result)
    else:
        print("Invalid choice! Please choose the calculation type again")

elif choice == 'B':
    print('''Which scientific calculation do you want to perform?
        A - Exponentiation(a^b)
        B - Square root
        C - sin()''')

    Bchoice = input("Select A,B or C: ")

    if Bchoice == 'A':
        base = float(input("Enter the base (a): "))
        pov = float(input("Enter the exponent (b): "))
        result = calculator.scientific.power(base, pov)
        print("Result: ", result)

    elif Bchoice == 'B':
        num = float(input("Enter the number for square root calculation: "))
        result = calculator.scientific.root(num)
        print("Square root: ", result)

    elif Bchoice == 'C':
        num = float(input("Enter the number for sin(): "))
        result = calculator.scientific.sin(num)
        print('Sin of ', num, ' is ',  result)

    else:
        print("Invalid choice! Please choose the calculation type again")

elif choice == 'C':
    print('''Which conversion do you want to perform?
    A - Curency Conversion (USD to PKR)
    B - Temperature Conversion (Celsius to Fahrenheit)
    C - Length Conversion (cm to Inches)''')

    Cchoice = input("Select A,B or C: ")

    if Cchoice == 'A':
        c = float(input("Enter temperature in Celsius: "))
        result = calculator.converter.c_to_f(c)
        print("Temperature in Fahrenheit: ", result)

    elif Cchoice == 'B':
        cm = float(input("Enter length in meters: "))
        result = calculator.converter.cm_to_inches(cm)
        print("Length in inches: ", inches)
    else:
        print("Invalid choice! Please choose the conversion type again")

else:
    print("Invalid choice! Please choose A, B, or C.")
