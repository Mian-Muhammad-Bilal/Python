# # lists are ordered collections of items
# # list can be change but tuple cannot
# # why list? -eik name k under multiple items rakhni ho to
# l = [3, 5, 6, "Biologist", 7.7, True]
# print(type(l))
# print(l)
# print(l[0])  # index starts from 0
# # for i in l:#ASY B PRINT HO SKTA
# #     print(i)

# negative indexing
# marks = [3, 4, 6, 7, 8, "biologist"]
# print(marks[-3])
# print(marks[len(marks)-3])
# print(marks[5-3])
# print(marks[2])

# if 6 in marks:
#     print("Yes")
# else:
#     print("No")


# if "6" in marks:
#     print("Yes")
# else:
#     print("No")

# print(marks)
# print(marks[1:])  # print(marks[1:len(marks)])ya python khud lga ly ga
# print(marks[1:-1])
# print(marks[1:9:2])

# list comprehension: run time py list bnana

list = [i for i in range(5)]
print(list)

list = [i for i in range(5) if i % 2 == 0]  # can put condition
print(list)
