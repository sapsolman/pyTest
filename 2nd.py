N = int(input())
H = N // 60
H1 = H // 24
print((H1 - H) // 60 + H, N % 60)

