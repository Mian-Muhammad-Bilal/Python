a = input("Enter a number: ")
print(f"The table of {a} is: ")

try:
    for i in range(1, 11):
        print(f"{int(a)} x {i} = {int(a)*i}")
except Exception as e:
    print(e)
# except:
#     print("Error")
except ValueError:
    print("Error")

print("some important lines of code")
print("End of code")
