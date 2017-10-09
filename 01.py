def arithmetic(a, b, o):
    if o == '+':
     return a + b
    elif o == '-':
     return a - b
    elif o == '*':
     return a * b
    elif o == '/':
     return a / b
    else:
     print ('unknown operation')
a, b, o = input().split()
a = int(a)
b = int(b)
x = arithmetic(a, b, o)
if  x % int(x) == 0 : print(int(x))
else  : print(x)