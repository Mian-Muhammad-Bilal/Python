# for i in range(12):
#     if (i == 10):
#         break  # loop ko chor l nikl jao
#     print("5 X ", i+1, " = ", (1+i)*5)

# for i in range(12):
#     if (i == 10):
#         print("This itration is skipped using continou")
#         continue  # itration ko chor l nikl jao
#     print("5 X ", i, " = ", 5*i)

# emulating do while loop:
i = 0
while True:
    print(i)
    i = i+1
    if (i % -1 == 0):
        break
