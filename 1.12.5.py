A = int(input())
B = int(input())
C = int(input())
if A >= B and B >= C:
    print(A)
    print(C)
    print(B)
elif A >= B and A <= C:
    print(C)
    print(B)
    print(A)
elif A <= B and A <= C:
    print(C)
    print(A)
    print(B)
else:
    print(B)
    print(A)
    print(C)
