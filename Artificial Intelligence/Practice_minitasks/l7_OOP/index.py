# class Myclass:
#     """A simple Class"""

#     def __init__(self):
#         print("Object created")
#     i = 12345

#     def f(self):
#         return 'hello world'


# x = Myclass()
# print(x.i)
# print(x.f())

def f1(self, x):
    """You can pmake a function outside of class and then save it in an variable in class and use it"""
    return x, 'Func outside of class'


class Myclass:
    """This is just a simple Class"""

    i = 12345
    f2 = f1

    def f(self):
        return 'hello world'

    def __init__(self, i):
        print("Object created")
        self.i = i

    def setI(self, i):
        self.i = i
        return f"setter called and assigned {self.i} to I"

    def getI(self):
        return self.i


x = Myclass(33)
print(f"The doc_string of class is \"{x.__doc__}\"")
print(x.i)
x.i = 3321
x.new_datamember = "New datamember, Created at run time "
print(x.i)
print(Myclass.i)  # can access datamember by class
# print(Myclass.f()) #can access datamember by class name but not function
print(x.new_datamember)
del x.new_datamember
print(x.f())
print(x.setI(6))
print(x.getI())
d = Myclass('fil')  # can creat objects like this
print(d.i)
print(x.f2(22))
print(x.f2.__doc__)
