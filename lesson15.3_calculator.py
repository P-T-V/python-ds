command = input('Выберите операцию (+,-,*,/): ')
while True:
    if command != '+' and command != '-' and command != '*' and command != '/':
        print('Ошибка: такой операции не существует. Попробуйте ещё раз.')
        command = input()
    else:
        n = int(input('Сколько операндов?: '))
        print('Введите операнд', 1, ': ', end = '')
        op = int(input())
        summary = str(op) + ' ' + command + ' '
        summ = op
        for a in range(2, n + 1):
            print('Введите операнд', a, ': ', end = '')
            op = int(input())
            if command == '+':
                summ += op
                summary += str(op)
            elif command == '-':
                summ -= op
                summary += str(op)
            elif command == '*':
                summ *= op
                summary += str(op)
            else:
                summ /= op
                summary += str(op)
            
            if a < n:
                summary += ' '+ command + ' '
        print(summary, '=', summ)
        break