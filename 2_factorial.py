def factorial(n):
    x = 1
    for i in range(1, n + 1):
        x = x * i

    return x


# Tester
print(factorial(4))
print(factorial(9))
print(factorial(0))
