first = int(input())
second = int(input())
oper = str(input())
#answer = str
if second == 0 and oper == '/':
    print('Деление на 0! повторите ввод')
else:
    answer = first, oper, second
    print(answer)
