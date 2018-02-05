first = float(input())
second = float(input())
oper = input("Знак (+,-,*,/): ")
if second == 0 and oper == '/':
    print('Деление на 0!')
elif oper == '+':
    print(first + second)
elif oper == '-':
    print(first - second)
elif oper == '*':
    print(first * second)
elif oper == '/':
    print(first / second)
