a = int(input())
b = int(input())
c = int(input())
if a >= b and b >= c:
    print(a)
    print(c)
    print(b)
elif a >= b and b <= c and a <= c:
    print(c)
    print(a)
    print(b)
elif a >= b and b <= c and a <= c:
    print(a)
    print(b)
    print(c)
elif a >= b and b <= c and a >= c:
    print(c)
    print(b)
    print(a)
