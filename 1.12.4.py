type = str(input())
if type == 'треугольник':
    a = int(input())
    b = int(input())
    c = int(input())
    p = ((a + b + c) / 2)
    cr = (p * (p - a) * (p - b) * (p - c))
    print(cr ** 0.5)
elif type == 'круг':
    a = int(input())
    print(3.14 * pow(a, 2))
elif type == 'прямоугольник':
    a = int(input())
    b = int(input())
    print(a * b)
else:
    print('Введите допустимое действие')
