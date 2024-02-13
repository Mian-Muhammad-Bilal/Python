a = [33, 55, 66, 86, 35, 22, 98]

# for mark in a:
#     print(mark)
#     if mark == 33:
#         print("Biologist")


# index = 0  # index lgana pra or phr incriment b krna pra...sardard
# for mark in a:
#     print(mark)
#     if index == 3:
#         print("Biologist")
#     index += 1


# enumerate index dy ga(pehly veriable ma),,,can start from anything
for index, mark in enumerate(a, start=1):
    print(mark)
    if index == 3:
        print("Biologist")
