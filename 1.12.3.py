first = float(input('Введите первое число '))
second = float(input('Введите второе число '))
oper = input('Действие (+,-,*,/,**,//,%): ')
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
elif oper == '%':
    if second == 0:
        print('Деление на 0!')
    else:
        print(first % second)
elif oper == '//':
    if second == 0:
        print('Деление на 0!')
    else:
        print(first // second)
elif oper == '**':
    print(first ** second)
else:
    print('Введите допустимое действие')