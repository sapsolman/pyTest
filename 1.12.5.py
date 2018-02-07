A = int(input())
B = int(input())
C = int(input())
if A >= B and B >= C:
    print(A)
    print(B)
    print(C)
elif A >= B and A <= C:
    print(C)
    print(A)
    print(B)
else:
    print(B)
    print(C)
    print(A)
