first = float(input())
second = float(input())
oper = input()
if oper == '+':
    print(first + second)
elif oper == '-':
    print(first - second)
elif oper == '*':
    print(first * second)
elif oper == '/':
    if second == 0:
        print('Деление на 0!')
    else:
        print(first / second)
elif oper == 'mod':
    if second == 0:
        print('Деление на 0!')
    else:
        print(first % second)
elif oper == 'div':
    if second == 0:
        print('Деление на 0!')
    else:
        print(first // second)
elif oper == 'pow':
    print(first ** second)
else:
    print('Введите допустимое действие')
