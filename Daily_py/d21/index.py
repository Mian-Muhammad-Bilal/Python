# default arguments
# def avg(a=1, b=1):
#     print("The average is:", (a+b)/2)
#     print("A is", a)
#     print("B is", b)


# avg(b=3)  # agar koi value na dy to default he chly gi ni to jo value dy gy to wo overwrite go jay gi

# keyword argument
# avg(b=3, a=8)  # agr order ki parwah na kry to isy keyword argument khy gy

# required argument:agar function definition ma a ki value na dy to call krty time dani he pry gi
# def avg(a,b=6)#a ki value kam sy kam dani pry gi

# veriable length argument:


def avgt(*num):  # num as a tuple
    sun = 0
    for i in num:
        sun = sun+i
    print(type(num))
    print("The avgt is: ", sun/len(num))


avgt(6, 5)  # tuple ki wja sy jitny mrzi number lo
