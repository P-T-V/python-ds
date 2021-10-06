N = int(input('Кол-во чисел в списке: '))
numbers_list = []
for i in range(N):
    print('Введите', i + 1, 'число: ', end=' ')
    number = int(input())
    numbers_list.append(number)

K = int(input('\nВведите делитель: '))
print()

counter = 0
summ_counter = 0
for id in numbers_list:
    if id % K == 0:
        print('Индекс числа', id, ':', counter)
        summ_counter += counter
    counter += 1

print('Сумма индексов: ', summ_counter)
