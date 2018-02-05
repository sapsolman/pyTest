first = float(input('Введите первое число '))
second = float(input('Введите второе число '))
oper = input('Действие (+,-,*,/,**,//,%): ')
if oper != '+' or oper != '-' or oper != '*' or oper != '/' or oper != '**' or oper != '//' or oper != '%':
    print('Введите действие')
else:
    if second == 0 and oper == '/' or oper == '%' or oper == '//':
        print('Деление на 0!')
    elif oper == '+':
        print(first + second)
    elif oper == '-':
        print(first - second)
    elif oper == '*':
        print(first * second)
    elif oper == '/':
        print(first / second)
    elif oper == '%':
        print(first % second)
    elif oper == '//':
        print(first // second)
    elif oper == '**':
        print(first ** second)
