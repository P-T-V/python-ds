def symmetry(numbers_check):
    symmetry_list = numbers_check[::-1]
    if numbers_check == symmetry_list:
        return True
    else:
        return False


# n = int(input('Кол-во чисел: '))
numbers = [1, 2, 3, 4, 5]
numbers_add = []

# for _ in range(n):
#     numbers.append(int(input('Число: ')))

print('\nПоследовательность:', end=' ')
for i in range(len(numbers)):
    print(numbers[i], end=' ')
print()

for i_n in range(len(numbers)):
    if symmetry(numbers[i_n:len(numbers)]):
        numbers_add = numbers[i_n-1::-1]

print('Нужно приписать чисел:', len(numbers_add))
print('Сами числа:', end=' ')
for k in range(len(numbers_add)):
    print(numbers_add[k], end=' ')
