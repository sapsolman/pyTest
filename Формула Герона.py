a = int(input())
b = int(input())
c = int(input())
p = ((a + b + c) / 2)
cr = (p * (p - a) * (p - b) * (p - c))
print(cr ** 0.5)
