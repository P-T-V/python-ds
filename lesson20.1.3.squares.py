num = int(input('Введите целое число: '))
num_dict = dict()
for i_num in range(1, num + 1):
    num_dict[i_num] = i_num ** 2
print('Результат:', num_dict)
