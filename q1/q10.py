a = list(input().split())
b = []
if a != []:
    b += a[-1]
    for i in range(len(a) - 1):
        b.append(a[i])
print(*b)