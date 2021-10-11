n = int(input('Кол-во сотрудников: '))
employee = []
k = 0

for i in range(n):
    print('Зарплата', i + 1, 'сотрудника:', end=' ')
    employee.append(int(input()))

while n != 0:
    if employee[n-1] == 0:
        employee.remove(employee[n-1])
    n -= 1

print('\nОсталось сотрудников:', len(employee))
print('Зарплаты:', employee)
print('\nМаксимальная зп:', max(employee))
print('Минимальная зп:', min(employee))
