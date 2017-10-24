def del0(x):
    a = []
    for i in range(1, x + 1):
        if x % i == 0: a.append(i)
    return a


if __name__ == "__main__":
    x = int(input())
    print(*del0(x))
