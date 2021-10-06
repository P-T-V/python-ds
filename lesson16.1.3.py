n = int(input('Введите кол-во сотрудников: '))
numbers_ID = []
flag = True
for _ in range(n):
    id = int(input('Введите ID номер сотрудника: '))
    numbers_ID.append(id)

search_ID = int(input('Какой ID ищем?: '))
for id in numbers_ID:
    if id == search_ID:
        print('Сотрудник на месте!')
        flag = False
        break
if flag:
    print('Сотрудник не работает!')
