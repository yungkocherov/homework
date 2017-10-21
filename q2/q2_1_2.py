def f(x):
    p = 1
    for i in range(1, x + 1):
        p *= i
    return p


x = int(input())
print(f(x))
