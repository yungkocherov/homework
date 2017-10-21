def f(x):
    if x == 1:
        return 1
    else:
        return (x) * f(x - 1)


x = int(input())
print(f(x))
