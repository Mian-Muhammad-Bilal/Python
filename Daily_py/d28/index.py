def fac(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n * fac(n-1)


def fib(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return (n-1) + fib(n-1)


print(fib(0))
print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))
print(fib(6))
