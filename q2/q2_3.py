n = int(input())
a = [1]
print(*a)
for i in range(n):
    a = [0] + a + [0]
    b = []
    for j in range(len(a) - 1):
        b.append(a[j] + a[j + 1])
    a = b
    print(*a)