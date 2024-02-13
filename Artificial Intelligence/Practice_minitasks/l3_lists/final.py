# ========================LAB WORK=================================

# # # for i in range(5):
# # #     print(i)


# # l=range(4,8)
# # print(l)

# def sum(a,b):
#     """This is doc string of the func which can only be display when call the fun like:fun_name.__doc__ and it should be in the very first line"""
#     return(a+b)
# print(sum.__doc__)
# # f=sum
# f(5,9)

# write a fun that takes a list as an argument and display list element in a single line
# def disp(lis):
#     for i in lis:
#         print(i, end=" ")
# l=[1,2,3,4,5,"hello world"]
# disp(l)


# if int so it will display else not
# def disp(lis):
#     for i in lis:
#         if type(i)==int:
#             print(i, end=" ")
# l=[1.0,2,3,4,5,"hello world",8.8,9]
# disp(l)

# func with default perameters
# def sum(n1,n2=10,n3=20):
#     print(n1+n2+n3)
# sum(1)
# sum(1,3)
# sum(1,3,4)

# python functions always have the last value
# def f(a,l=[]):
#     l.append(a)
#     return l
# print(f(1))
# print(f(2))
# print(f(3))
# print(f("This"))
# print(f("Function"))
# print(f("is creating"))
# print(f("list"))

# python functions always have the last value until initialize the func with 'None'
# def f(a,l=None):
#     if l is None:
#         l=[]
#     l.append(a)
#     return l
# print(f(1))
# print(f(2))
# print(f(3))
# print(f("This"))
# print(f("Function"))
# print(f("is not"))
# print(f("creating"))
# print(f("list"))

# insert fun in lists
# l=[1,2,3,4,5,6,7,"Hello",3.3,[1,5,7]]
# print(l)
# l.insert(1,777)
# print(l)

# if list so it will display else not
# def disp(lis):
#     for i in lis:
#         if type(i)==list:
#             print(i, end=" ")
# l=[1.0,2,3,4,5,"hello world",8.8,9,[1,2,3],['Hello'],['world']]
# disp(l)

# remove,pop,clear functions in lists
# l=[1,2,3,4,5,6,7,"Hello",3.3,[1,5,7]]
# print(l)
# l.remove(1)
# print(l)
# l.pop(6)
# print(l)
# l.clear()
# print(l)

# stack data structure
# stack=[1,2,3]
# stack.append(4)
# stack.append(5)
# print(stack)
# print(stack.pop())
# print(stack)
# print(stack.pop())
# print(stack)

# queue data structure
# from collections import queue
# queue = deque(["abc", "xyz"])
# queue.append("Bilal")
# queue.append("ali")
# queue.popleft()
# queue.popleft()
# queue
# deque(['ali', 'bilal'])


# squares = []
# for x in range(10):
#     squares.append(x**2)
# print(squares)

# comprihension statment
# squares = [x**2 for x in range(10)]
# print(squares)
# squares = [x for x in range(10)]
# print(squares)
# my solution for coping one list inbto other usng comprihension statment
# x = [1, 2, 3, 6, 6, 6]
# squares = [x[i] for i in range(len(x))]
# print(squares)

# sir. solution
# x = [1, 2, 3, 6, 6, 6]
# squares = [i for i in x]
# print(squares)

# print([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y])

# converting a for loop into comprihension statment
# l1=[1,2,3,4,5]
# l2=[2,4,5,6,7]
# l3=[]
# for i in range(4):
#     lTemp=[]
#     for j in range(4):
#         lTemp.append(j)
#     l3.append(lTemp)
# print(l3)

# my solution
# print([ltemp.append(i) for i in range(4) l3.append(ltemp) for j in range(4)])
# sir solution
# print([[j for i in range(4)]  for j in range(4)])

# transpose of matrix with loop and then with comprihension statment
# matrix=[
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12]
#     ]

# print(matrix)

# with loop:
# transposed = []
# for i in range(4):
# transposed.append([row[i] for row in matrix])

# print(transposed)

# with comprihension statment:
# print([[row[i] for row in matrix] for i in range(4)])

# ========================LAB TASKS(week03 pdf)=================================
# Q1:
# def disp(lis):
#     for i in lis:
#         if type(i)==int:
#             print(i, end=" ")
# l=[1.0,2,3,4,5,"hello world",8.8,9,[1,2,3],['Hello']]
# disp(l)


# Q2:
# def disp(lis):
#     for i in lis:
#         if type(i)==list:
#             print(i, end=" ")
# l=[1.0,2,3,4,5,"hello world",8.8,9,[1,2,3],['Hello'],['world']]
# disp(l)


# Q3:
# x = [1, 2, 3, 6, 6, 6]
# squares = [x[i] for i in range(len(x))]
# print(squares)


# Q4:
# matrix=[
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12]
#     ]

# #with loop:
# transposed = []
# for i in range(4):
#     transposed.append([row[i] for row in matrix])
# print(transposed)

# #with comprihension statment:
# print([[row[i] for row in matrix] for i in range(4)])


# Q5:
# def getLength():
#     """gets rectangle's length and then return that value as a double."""
#     return float(input('Enter length: '))


# def getWidth():
#     """gets rectangle's width and then return that value as a double."""
#     return float(input('Enter width: '))


# def getArea(a, b):
#     """takes length and width as arguments and return the area"""
#     return a*b


# def displayData(len, wid, area):
#     """takes length, width, and area as arguments and display them properly using f'string."""
#     print(
#         f"The length of rectangle is {len}, width is {wid} and the area is {area}.")


# a = getLength()
# b = getWidth()
# c = getArea(a, b)
# displayData(a, b, c)
